from odoo import models, fields, api

class SportsCreateIssue(models.TransientModel):
    _name = 'sports.create.issue'
    _description = 'Create Issue'

    # def _get_default_clinic(self):
    #     if self.env.context.get('active_model') == 'sports.clinic':
    #         return self.env.context.get('active_id')
    #     else:
    #         return False

    name = fields.Char(string='Name', required=True)
    clinic_id = fields.Many2one('sports.clinic', string='Clinic')

    def create_issue(self):
        vals={
            'name': self.name,
            'clinic_id': self.clinic_id.id
            }
        issue=self.env['sports.issue'].create(vals)
        return {'name': 'Issues', 'type': 'ir.actions.act_window', 'res_model': 'sports.issue', 'view_mode': 'form', 'target': 'current','res_id': issue.id}
    
   