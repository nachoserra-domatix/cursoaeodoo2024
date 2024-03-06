from odoo import models, fields

class SportsClinic(models.Model):
    _name = 'sports.clinic'
    _description = 'Sports Clinic'

    name = fields.Char(string='Name',required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    issue_ids = fields.One2many('sports.issue', 'clinic_id', string='Issues')
    available = fields.Boolean(string='Available')

    def action_check_assistance(self):
        import pdb;pdb.set_trace()
        for record in self:
            for issue in record.issue_ids:
                issue.assistance = True
        return True
