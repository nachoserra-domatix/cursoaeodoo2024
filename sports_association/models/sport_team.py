# Copyright NuoBiT Solutions - Kilian Niubo <kniubo@nuobit.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)
from odoo import fields, models


class SportTeam(models.Model):
    _name = "sport.team"
    _description = "Sport Team"
    _inherit = "image.mixin"

    name = fields.Char(
        required=True,
    )
    player_ids = fields.One2many(
        comodel_name="sport.player",
        inverse_name="team_id",
    )
    sport_id = fields.Many2one(comodel_name="sport.sport")

    def set_true_titular_players(self):
        self.ensure_one()
        for player in self.player_ids:
            player.set_true_titular_players()
