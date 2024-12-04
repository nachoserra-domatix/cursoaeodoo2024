from odoo import _, api, fields, models



class SportTicket(models.Model):
    _inherit = 'sport.ticket'

    name = fields.Char(string='Name',required=True,) 
    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Sale Order')
    match_id = fields.Many2one(comodel_name='sport.match', string='Match')
