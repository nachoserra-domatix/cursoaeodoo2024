from odoo import _, api, fields, models



class SportTicket(models.Model):
    _name = 'sport.ticket'
    _description = 'Sport Ticket'

    name = fields.Char(string='')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')
    match_id = fields.Many2one(comodel_name='sport.match', string='Match')
    
    
    