from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sport_ticket_ids = fields.One2many(
        "sport.ticket", "sale_order_id", string="Sport Tickets"
    )

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            ticket_products = order.order_line.filtered(lambda l: l.product_id.is_ticket)
            for prod in ticket_products:
                 order.create_sport_ticket()
        return res
        
    def action_cancel(self):
        res = super().action_cancel()
        self.sport_ticket_ids.unlink()
        return res

    def create_sport_ticket(self):
        vals = {
            "name": self.name,
            "partner_id": self.partner_id.id,
            "sale_order_id": self.id,
        }
        self.env["sport.ticket"].create(vals)