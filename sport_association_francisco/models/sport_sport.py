from odoo import models, fields, api

class SportSport(models.Model):

    _name = 'sport.sport'
    _description = 'Sport Sport'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
