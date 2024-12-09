from odoo import fields, models, api, _


class SportTeam(models.Model):
    _name = "sport.team"

    name = fields.Char(string=_("Name"), required=True)
    image_1920 = fields.Image(string=_("Image"), max_width=1920, max_height=1920)
    player_ids = fields.One2many(
        comodel_name="sport.player", inverse_name="team_id", string=_("Players")
    )
    sport_id = fields.Many2one(
        comodel_name="sport.sport", string=_("Sport"), required=True
    )
    trainer_id = fields.Many2one(comodel_name="res.partner", string=_("Trainer"))
    player_count = fields.Integer(
        compute="_compute_player_count", string=_("Players Count"), store=True
    )

    @api.depends("player_ids")
    def _compute_player_count(self):
        for record in self:
            record.player_count = len(record.player_ids)

    def action_headline_player(self):
        return {
            "name": self.name + "headlines",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.change.headline.player",
            "context": {"default_player_ids": self.player_ids.ids},
            "target": "new",
        }

    def action_add_player_in_team(self):
        for record in self:
            player_ids = self.env["sport.player"].search([("age", "<", 30)])
            if player_ids:
                record.write(
                    {
                        "player_ids": [(6, 0, player_ids.ids)],
                    }
                )
