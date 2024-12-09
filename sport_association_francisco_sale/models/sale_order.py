from odoo import models, fields, Command

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    ticket_ids = fields.One2many('sport.ticket', inverse_name="sale_order_id", string='Tickets')

    def create_ticket(self):
        for rec in self:
            rec.write({
                'ticket_ids': [Command.create({'sale_order_id': rec.id})]
            })

    def action_cancel(self):
        self.ticket_ids.unlink()
        rec = super().action_cancel()
        return rec
    