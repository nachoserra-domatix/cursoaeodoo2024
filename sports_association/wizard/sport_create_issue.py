# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class SportCreateIssue(models.TransientModel):
    _name = 'sport.create.issue'
    _description = 'Create issue'

    name = fields.Char('Issue name')
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    player_id = fields.Many2one('sport.player', string='Player')
    
    def create_issue(self):
        import pdb;pdb.set_trace()
        vals = {
            'name': self.name,
            'clinic_id': self.clinic_id.id,
            'player_id': self.player_id.id
            }
        issue = self.env['sport.issue'].create(vals)
        return {
            'name': 'Issue',
            'view_mode': 'form',
            'res_model': 'sport.issue',
            'res_id': issue.id,
            'type': 'ir.actions.act_window',
            'target': 'current',}