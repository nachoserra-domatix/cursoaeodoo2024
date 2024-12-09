from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sports_ticket_ids = fields.One2many('sports.ticket','sale_order_id',string='Sports Tickets')

    def action_create_sports_ticket(self):
        vals = {
            'name': self.name,
            'partner_id': self.partner_id.id,
            'sale_order_id': self.id,
        }
        self.env['sports.ticket'].create(vals)
    
    def action_cancel(self):
        res= super().action_cancel()
        self.sports_ticket_ids.unlink()
        return res

    def action_confirm(self):
        res= super().action_confirm()
        import pdb; pdb.set_trace()
        for line in self.order_line:
            if line.product_id.is_sports_ticket:
                self.action_create_sports_ticket()