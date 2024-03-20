from odoo import models, fields

class SportsTicket(models.Model):
    _name = 'sports.ticket'
    _description = 'Sports Ticket'

    name = fields.Char(string='Name',required=True)
    partner_id = fields.Many2one('res.partner',string='Partner')
    match_id = fields.Many2one('sports.match',string='Match')