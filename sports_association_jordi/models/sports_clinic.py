from odoo import models, fields

class SportsClinic(models.Model):
    _name = 'sports.clinic'
    _description = 'Sports Clinic'

    name = fields.Char(string='Name',required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    issue_ids = fields.One2many('sports.issue', 'clinic_id', string='Issues')
    available = fields.Boolean(string='Available')
    issue_count = fields.Integer(string='Issue Count', compute='_compute_issue_count')

    def action_check_assistance(self):
        import pdb;pdb.set_trace()
        for record in self:
            for issue in record.issue_ids:
                issue.assistance = True
        return True

    def action_show_issues(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Issues',
            'res_model': 'sports.issue',
            'view_mode': 'tree,form',
            'domain': [('clinic_id', '=', self.id)],
        }
    
    def _compute_issue_count(self):
        for record in self:
            record.issue_count = len(record.issue_ids)
    
