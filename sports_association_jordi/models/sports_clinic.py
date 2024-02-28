from odoo import models, fields

class SportsClinic(models.Model):
    _name = 'sports.clinic'
    _description = 'Sports Clinic'

    name = fields.Char(string='Name',required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    issue_ids = fields.One2many('sports.issue', 'clinic_id', string='Issues')

    def action_check_assistance(self):
        for record in self:
            for issue in record.issue_ids:
                issue.assistance = True
        return True
