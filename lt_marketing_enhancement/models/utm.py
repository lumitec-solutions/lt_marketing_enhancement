##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
from odoo import fields, models, _


class UtmCampaign(models.Model):
    _inherit = 'utm.campaign'

    project_count = fields.Integer('Project Count',
                                   compute='_compute_project_count')
    meeting_count = fields.Integer('Meeting Count',
                                   compute='_compute_meeting_count')
    event_count = fields.Integer('Event Count',
                                 compute='_compute_event_count')

    def _compute_project_count(self):
        """This function computes the project count."""
        for rec in self:
            count = self.env['project.project'].search_count(
                [('campaign_id', '=', rec.id)])
            rec.project_count = count

    def _compute_meeting_count(self):
        """This function computes the meeting count."""
        for rec in self:
            count = self.env['calendar.event'].search_count(
                [('campaign_id', '=', rec.id)])
            rec.meeting_count = count

    def _compute_event_count(self):
        """This function computes the event count."""
        for rec in self:
            count = self.env['event.event'].search_count(
                [('campaign_id', '=', rec.id)])
            rec.event_count = count

    def action_view_projects(self):
        """This function opens the project view."""
        return {
            'name': _('Projects'),
            'type': 'ir.actions.act_window',
            'res_model': 'project.project',
            'view_mode': 'kanban,form',
            'target': 'current',
            'domain': [('campaign_id', '=', self.id)],
            'context': {'default_campaign_id': self.id}
        }

    def action_view_meetings(self):
        """This function opens the meeting view."""
        return {
            'name': _('Meetings'),
            'type': 'ir.actions.act_window',
            'res_model': 'calendar.event',
            'view_mode': 'calendar,tree,form',
            'target': 'current',
            'domain': [('campaign_id', '=', self.id)],
            'context': {'default_campaign_id': self.id}
        }

    def action_view_events(self):
        """This function opens the event view."""
        return {
            'name': _('Events'),
            'type': 'ir.actions.act_window',
            'res_model': 'event.event',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('campaign_id', '=', self.id)],
            'context': {'default_campaign_id': self.id}
        }
