from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sport_ticket_ids = fields.One2many('sport.ticket', 'sale_order_id', string='Sport Ticket')

    def action_cancel(self):
        res = super().action_cancel()
        self.sport_ticket_ids.unlink()
        return res
    
    def create_sport_ticket(self):
        vals = {
            'name': self.name,
            'partner_id': self.partner_id.id,
            'sale_order_id': self.id,
        }
        self.env['sport.ticket'].create(vals)

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            # Para crear un único ticket independientemente del número de productos marcados como tickets.
            if order.order_line.filtered(lambda l: l.product_id.is_ticket):
                order.create_sport_ticket()
            # Para crear un ticket por cada producto marcado como tal.
            # ticket_products =  order.order_line.filtered(lambda l: l.product_id.is_ticket)
            # for product in ticket_products:
            #     order.create_sport_ticket()
        return res