##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
import hashlib
import hmac
import uuid
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class MailingToken(models.Model):
    _name = "mailing.contact.token"
    _description = "Mailing Contact Token"

    access_token = fields.Char('Security Token',
                               compute='_compute_access_token', store=True,
                               readonly=True,
                               copy=False)
    token_generation_date = fields.Date('Token Generation Date',
                                        compute='_compute_access_token',
                                        store=True,
                                        readonly=True, copy=False)
    mailing_contact_id = fields.Many2one('mailing.contact',
                                         string='Mailing Contact',
                                         required=True, readonly=True,
                                         copy=False)
    action = fields.Selection([('double_opt_in', 'Double Opt-In')],
                              string="Action", default='double_opt_in',
                              required=True, readonly=True, copy=False)

    @api.depends('mailing_contact_id', 'action')
    def _compute_access_token(self):
        """This method computes the access token."""
        secret = self.env['ir.config_parameter'].sudo().get_param(
            "database.secret")
        dbname = self.env.cr.dbname
        for record in self:
            token = (dbname, record.id, str(uuid.uuid4()))
            access_token = hmac.new(secret.encode('utf-8'),
                                    repr(token).encode('utf-8'),
                                    hashlib.sha512).hexdigest()
            record.access_token = access_token
            record.token_generation_date = fields.Date.today()

    def get_url(self):
        """For getting the url"""
        if not self.access_token:
            ValidationError(
                _('The mailing.contact.token must have set a access token for get the url.'))
        return '%s/mailing/manage?access_token=%s' % (
        self.get_base_url(), self.access_token)

    @api.model
    def cron_delete_token(self, months=2, days=0):
        """Scheduled action for deleting the token"""
        deletion_date = date.today() - relativedelta(months=months, days=days)
        records = self.search([('token_generation_date', '<', deletion_date)])
        records.unlink()

    _sql_constraints = [('access_token_uniq', 'unique(access_token)',
                         'Every access token must be unique!')]
