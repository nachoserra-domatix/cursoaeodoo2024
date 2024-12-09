from odoo import Command, api, fields, models


class SportLeagueCreateGames(models.TransientModel):
    _name = "sport.league.create.games"
    _description = "Sport League Create Games"

    league_id = fields.Many2one(
        string="League",
        comodel_name="sport.league",
    )
    date = fields.Datetime(
        string="Start Date",
        default=fields.Datetime.now(),
    )
    team_ids = fields.Many2many(
        string="Teams",
        comodel_name="sport.team",
    )
    allowed_team_ids = fields.Many2many(
        "sport.team",
        relation="sport_game_team_rel",
        string="Allowed Teams",
        compute="_compute_allowed_team_ids",
        store=True,
    )

    @api.depends("league_id")
    def _compute_allowed_team_ids(self):
        for record in self:
            record.allowed_team_ids = self.league_id.league_line_ids.team_id.ids

    def create_games(self):
        vals = {
            "league_id": self.league_id.id,
            "date": self.date,
            "game_line_ids": [
                Command.create({"team_id": team.id}) for team in self.team_ids
            ],
        }
        game = self.env["sport.game"].create(vals)
        game.message_post_with_source(
            "mail.message_origin_link",
            render_values={"self": game, "origin": self.league_id},
            subtype_xmlid="mail.mt_note",
        )
        return {
            "name": "Game",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "sport.game",
            "res_id": game.id,
            "target": "current",
        }
