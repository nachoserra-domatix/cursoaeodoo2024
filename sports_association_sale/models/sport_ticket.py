from odoo import fields, models


class SportTicket(models.Model):
    _inherit = "sport.ticket"

    sale_order_id = fields.Many2one(
        string="Sale Order",
        comodel_name="sale.order",
    )