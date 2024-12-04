from odoo import fields, models, api

class SportCreateIssue(models.TransientModel):
    _name = 'sport.create.issue'
    _description = 'Create Issue'

    name = fields.Char('Issue name')
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    player_id = fields.Many2one('sport.player', string='Player')

    def create_issue(self):
        vals = {
            'name': self.name,
            'clinic_id': self.clinic_id.id,
            'player_id': self.player_id.id,
        }
        issue = self.env['sport.issue'].create(vals)

        return {
            'name': 'Issue',
            'view_mode': 'form',
            'res_model': 'sport.issue',
            'res_id': issue.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

