##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    send_double_opt_in = fields.Boolean(string="Send Double Opt in",
                                        config_parameter='lt_double_opt_in.send_double_opt_in')
