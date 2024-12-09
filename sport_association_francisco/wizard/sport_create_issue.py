from odoo import fields, api, models

class SportCreateIssue(models.TransientModel):
    _name = 'sport.create.issue'
    _description = "Create issue"

    name = fields.Char('Name')
    clinic_id = fields.Many2one('sport.clinic', string='Clinic')
    player_id = fields.Many2one('sport.player', string='Player')

    def create_issue(self):
        self.ensure_one()
        active_id = self.env.context.get('active_id')
        model = self.env.context.get('active_model')
        issue = self.env['sport.issue'].create({
            'name':self.name,
            'clinic_id': self.clinic_id.id,
            'player_id': self.player_id.id
            })
        return {
            'name':'Issue',
            'view_mode': 'form',
            'res_model':'sport.issue',
            'res_id':issue.id,
            'type':'ir.actions.act_window',
            'target':'current',
        }
        
       

