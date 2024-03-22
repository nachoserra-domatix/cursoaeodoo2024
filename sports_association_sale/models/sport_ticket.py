# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class SportTicket(models.Model):
    _inherit = "sport.ticket"

    sale_order_id = fields.Many2one(
        "sale.order", string="Sales Order", ondelete="cascade", copy=False
    )
