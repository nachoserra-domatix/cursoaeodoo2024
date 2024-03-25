from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sport_ticket_ids = fields.One2many(
        "sport.ticket", "sale_order_id", string="Sport Tickets"
    )

    def action_cancel(self):
        res = super().action_cancel()
        self.sport_ticket_ids.unlink()
        return res

    def create_sport_ticket(self):
        vals = {
            "partner_id": self.partner_id.id,
            "sale_order_id": self.id,
        }
        self.env["sport.ticket"].create(vals)

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            for line in order.order_line:
                if line.product_id.is_ticket:
                    vals = {
                        "partner_id": self.partner_id.id,
                        "sale_order_id": self.id,
                        "game_id": line.product_id.game_id.id,
                    }
                    self.env["sport.ticket"].create(vals)
        return res
