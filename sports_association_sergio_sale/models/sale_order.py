from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sport_ticket_ids = fields.One2many('sport.ticket', 'sale_order_id', string='Sport Tickets')


    def action_cancel(self):
        # import pdb; pdb.set_trace()
        for order in self:
            order.sport_ticket_ids.unlink()
        return super().action_cancel()
    
    def create_sport_ticket(self):       
        self.env['sport.ticket'].create({
            'name': self.name,
            'partner_id': self.partner_id.id,
            'sale_order_id': self.id
        })
        return True