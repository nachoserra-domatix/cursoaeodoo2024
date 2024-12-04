from odoo import models, fields



class SportClinic(models.Model):
    _name = 'sport.clinic'
    _description = 'Sport Clinic'

    name = fields.Char(string='Name', required=True)
    phone = fields.Integer(string='phone')
    email = fields.Char(string='email')
    available = fields.Boolean(string='Available')
    issue_count = fields.Integer(string='Issue count', compute='_compute_issue_count')
    
    
    issue_ids = fields.One2many(comodel_name='sport.issue', inverse_name='clinic_id', string='Issues')

    def _compute_issue_count(self):
        for record in self:
            self.issue_count = len(self.issue_ids)

    def action_check_assistance(self):
        self.issue_ids.write({'assistance': True})

    def action_view_issues(self):

        return {
            'name': 'Issues',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.issue',
            'view_mode': 'tree,form',
            'domain': [('clinic_id', '=', self.id)]
        }
    
