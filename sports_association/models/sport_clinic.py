from odoo import models, fields

class SportClinic(models.Model):
    _name = "sport.clinic"
    _description = "Sport Clinic"

    name = fields.Char(
        string='name',
        required=True
    )
    phone = fields.Char(
        string='phone',
    )
    email = fields.Char(
        string='email',
    )
    issue_ids = fields.One2many(
        string='Issues',
        comodel_name='sport.issue',
        inverse_name='clinic_id',
    )
    available = fields.Boolean(
        string='Available',
    )
   
    
    def action_check_assistance(self):
        for record in self:
            for issue in record.issue_ids:
                issue.assistance = True