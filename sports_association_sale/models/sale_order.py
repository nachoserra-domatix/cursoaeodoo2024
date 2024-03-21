from odoo import _, api, fields, models, Command





class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sport_ticket_ids = fields.One2many(comodel_name='sport.ticket', inverse_name='sale_order_id', string='Sport Tickets')
    
    def action_cancel(self):
        res = super().action_cancel()
        self.sport_tickets_id.unlink()
        return res

    def create_sport_ticket(self):
        for rec in self:
            rec.write({
                'sport_ticket_ids': [Command.create({'sale_order_id': rec.id})]
            })