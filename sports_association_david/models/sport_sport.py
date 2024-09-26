from odoo import models, fields

class SportSport(models.Model):
    _name = 'sport.sport'
    _description = 'Sport'

    name = fields.Char(string="Name", required=True)
    description = fields.Char(string='Description')