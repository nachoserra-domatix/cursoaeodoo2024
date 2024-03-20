from odoo import models, fields

class SaleOrder(models.Model):

    _inherit="sale.order"

    sport_ticket_ids = fields.One2many('sport.ticket', 'sale_order_id', string='Sport Ticket')

    def action_cancel(self):
        # res= super(SaleOrder,self).action_cancel()
        res = super().action_cancel()
        self.sport_ticket_ids.unlink()
        return res

    def create_sport_ticket(self):
        vals = {
            'name': self.name,
            'partner_id': self.partner_id.id,
            'sale_order_id': self.id
        }
        self.env['sport.ticket'].create(vals)