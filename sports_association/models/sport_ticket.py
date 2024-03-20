# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportTicket(models.Model):
    _name = 'sport.ticket'
    _description = 'ticket'

    name = fields.Char(string='ticket Name', required=True)
    partner_id = fields.Many2one('res.partner', 'Customer', required=True, index=True)
    match_id = fields.Many2one('sport.match', string='Match')
    date = fields.Text(string='Description')
    qr = fields.Binary(string='Image')