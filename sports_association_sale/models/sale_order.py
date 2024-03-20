# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sport_ticket_ids = fields.One2many('sport.ticket', 'sale_order_id', string='Sport Tickets')

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