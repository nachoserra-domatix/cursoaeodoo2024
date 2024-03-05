from odoo import fields, models

class SportSport(models.Model):
    _name = 'sport.sport'
    _description = 'Sport Description'
  
    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
    image = fields.Image(string='Image', max_width=100, max_height=100)
