from odoo import models, fields

class SportTicket(models.Model):

    _name = 'sport.ticket'
    _description = 'Sport Ticket'

    name = fields.Char(string="Name")
    client_id = fields.Many2one('res.partner', string='Client')
    match_id = fields.Many2one('sport.match', string='Match')
