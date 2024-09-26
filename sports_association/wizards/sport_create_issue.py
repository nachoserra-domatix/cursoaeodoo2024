from odoo import models, fields, api, Command, _
#from datetime import date


class SportCreateIssue(models.TransientModel):
    _name = 'sport.create.issue'
    _description = "Create Issue"

    name = fields.Char(string='Name', required=True)
    clinic_id = fields.Many2one('sport.clinic', string='Clinic', default= lambda self: self.env.context.get('active_id') if self.env.context['active_model'] == 'sport.clinic' else False)
    player_id = fields.Many2one('sport.player', string='Player', default= lambda self: self.env.context.get('active_id') if self.env.context['active_model'] == 'sport.player' else False)
    
    def create_issue(self):
        # if self.env.context['active_model'] == 'sport.clinic':
        #     clinic = self.env.context.get('active_id')
        #     self.clinic_id = clinic
        # else:
        #     player = self.env.context.get('active_id')
        #     self.player_id = player

        vals = {
            'name': self.name,
            'clinic_id': self.clinic_id.id,
            'player_id': self.player_id.id
            }
        issue = self.env['sport.issue'].create(vals)
        return {
            'name': 'Issue',
            'view_mode': 'form',
            'res_model' : 'sport.issue',
            'res_id': issue.id,
            'type': 'ir.actions.act_window',
            'target': 'current'
        }