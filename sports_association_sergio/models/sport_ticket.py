from odoo import models, fields

class SportTicket(models.Model):
    _name = 'sport.ticket'
    _description = 'Sport Ticket'

    name = fields.Char(string='Name', required=True)
    match_id = fields.Many2one('sport.match', string='Match')
    partner_id = fields.Many2one('res.partner', string='Customer')