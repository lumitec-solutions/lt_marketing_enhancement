##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
from odoo import fields, models


class Project(models.Model):
    _inherit = 'project.project'

    campaign_id = fields.Many2one('utm.campaign', string='Campaign', readonly=1)

