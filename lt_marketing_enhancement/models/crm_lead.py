##############################################################################
# Copyright (c) 2021 brain-tec AG (https://bt-group.com)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
from odoo import api, models, fields


class Lead(models.Model):
    _inherit = 'crm.lead'

    MAILING_CONTACT_FIELDS = ['email_from', 'contact_name', 'partner_name', 'country_id', 'title',
                              'lang_id', 'tag_ids']

    @api.model
    def create(self, vals):
        lead = super(Lead, self).create(vals)
        lead.update_mailing_contact()
        return lead

    def write(self, vals):
        result = super(Lead, self).write(vals)
        mailing_contact_fields_changed = False
        for changed_field in vals:
            if changed_field in self.MAILING_CONTACT_FIELDS:
                mailing_contact_fields_changed = True
        if mailing_contact_fields_changed:
            for record in self:
                record.update_mailing_contact()
        return result

    def update_mailing_contact(self):
        """This function updates the mailing contact"""
        self.ensure_one()
        category_names = self.tag_ids.mapped('name')
        self.env['mailing.contact'].merge_with(self.email_from,
                                               self.contact_name,
                                               self.partner_name,
                                               self.country_id.id,
                                               self.title.id,
                                               self.lang_id.code,
                                               category_names)
