from odoo import fields, models


class SportTicket(models.Model):
    _name = "sport.ticket"
    _description = "Sport Ticket"

    name = fields.Char(string="Name", readonly=True)
    partner_id = fields.Many2one(string="Partner", comodel_name="res.partner")
    game_id = fields.Many2one(string="Game", comodel_name="sport.game")

    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code("sport.ticket")
        res = super().create(vals)
        return res
