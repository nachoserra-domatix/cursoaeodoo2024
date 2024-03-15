from odoo import fields, models

class SportSport(models.Model):
    _name = 'sport.sport'
    _description = 'Sport Sport'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')