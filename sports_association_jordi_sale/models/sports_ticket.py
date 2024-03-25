from odoo import models, fields, api

class SportsTicket(models.Model):
    _inherit = 'sports.ticket'

    sale_order_id = fields.Many2one('sale.order',string='Sale Order')