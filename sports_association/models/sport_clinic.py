from odoo import models, fields



class SportClinic(models.Model):
    _name = 'sport.clinic'
    _description = 'Sport Clinic'

    name = fields.Char(string='Name', required=True)
    phone = fields.Integer(string='phone')
    email = fields.Char(string='email')
    available = fields.Boolean(string='Available')
    
    
    issue_ids = fields.One2many(comodel_name='sport.issue', inverse_name='clinic_id', string='Issues')

    def action_check_assistance(self):
        self.issue_ids.write({'assistance': True})

    
    
