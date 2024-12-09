from odoo import models, fields

class SportClinic(models.Model):
    _name = 'sport.clinic'
    _description = 'Sport Clinic'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    issue_ids = fields.One2many('sport.issue', 'clinic_id', string='Issues')
    available = fields.Boolean(string='Available')
    issues_count = fields.Integer(string='Issues')

    def action_check_assistance(self):
        # import pdb; pdb.set_trace()
        for record in self.issue_ids:
            record.assistance = True

    def action_view_issues(self):
        return {
            'name': 'Issues',
            'type': 'ir.actions.act_windows',
            'res_model': 'sport_issue',
            'view_mode': 'tree,form',
            'domain': [('clinic_id', '=', self.id)],
        }
