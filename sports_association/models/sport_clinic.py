# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportClinic(models.Model):
    _name = 'sport.clinic'
    _description = "Sport Clinic"

    #=== FIELDS ===#
    
    name = fields.Char(string="Name", required=True)  
    phone = fields.Char('phone')
    email = fields.Char('email')
    issue_ids = fields.One2many(
        comodel_name='sport.issue',
        inverse_name='clinic_id')

    #=== METHODS ===#
    
    def action_check_assistance(self):
        for record in self.issue_ids:
            record.assistance = True