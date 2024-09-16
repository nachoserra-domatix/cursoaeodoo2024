from odoo import models, fields, api

class SportCreateIssue(models.TransientModel):
    _name = 'sport.create.issue'
    _description = 'Create issue'

    name = fields.Char('Issue name')
    clinic_id = fields.Many2one('sport.clinic', string='Clinic', default=lambda self: self.env.context.get('active_id'))

    def create_issue(self):
        vals = {
            'name': self.name,
            'clinic_id': self.clinic_id.id,
        }
        issue = self.env['sport.issue'].create(vals)
        return {
            'type': 'ir.actions.act_window', 
            'name': 'Issue', 
            'res_model': 'sport.issue', 
            'res_id': issue.id, 
            'view_mode': 'form', 
            'target': 'current', }
        