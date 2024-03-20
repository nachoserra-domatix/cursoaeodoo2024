from odoo import models,fields


class SportTicket(models.Model):
    _name = 'sport.ticket'
    _description = 'Sport Ticket'


    name = fields.Char(
        string='Name',
        required=True,
    )    
    partner_id = fields.Many2one(
        string='Partner',
        comodel_name='res.partner',
    )
    game_id = fields.Many2one(
        string='Game',
        comodel_name='sport.game',
    )
