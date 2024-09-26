from odoo import models, fields, api

class SportTicket(models.Model):
    _name = 'sport.ticket'
    _description = "Sport Ticket"

    name = fields.Char('Name', required=True)
    partner_id = fields.Many2one('res.partner', string='Client')
    game_id = fields.Many2one('sport.game', string='Game')
