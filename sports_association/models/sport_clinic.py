# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportClinic(models.Model):
    _name = 'sport.clinic'
    _description = "Sport Clinic"

    #=== FIELDS ===#
    
    name = fields.Char(string="Name", required=True)  

    issues_id = fields.One2many('sport.issue', 'clinic_id')