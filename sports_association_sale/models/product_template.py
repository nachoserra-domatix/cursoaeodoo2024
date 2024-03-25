from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_ticket = fields.Boolean(string="Is Ticket", default=False)
    game_id = fields.Many2one(string="Game", comodel_name="sport.game")
