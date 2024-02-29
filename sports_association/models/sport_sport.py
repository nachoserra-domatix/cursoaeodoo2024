from odoo import models, fields

class SportSport(models.Model):
    _name = "sport.sport"
    _description = "Sport"

    
    name = fields.Char(
        string='Name',
    )
    
    description = fields.Text(
        string='Description',
    )
    
    image = fields.Binary(
        string='Image',
    )
    