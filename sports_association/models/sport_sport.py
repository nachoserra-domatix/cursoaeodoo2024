# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportSport(models.Model):
    _name = 'sport.sport'
    _description = 'Sports'

    name = fields.Char(string='Sport Name', required=True)
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image')