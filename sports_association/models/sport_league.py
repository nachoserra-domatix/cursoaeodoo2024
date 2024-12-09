from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SportLeague(models.Model):
    _name = "sport.league"
    _description = "Sport League"

    name = fields.Char(
        string="Name",
    )

    sport_id = fields.Many2one(
        string="Sport",
        comodel_name="sport.sport",
    )

    description = fields.Text(
        string="Description",
    )

    image = fields.Binary(
        string="Image",
    )

    date_start = fields.Date(
        string="Start Date",
        default=fields.Date.context_today,
    )
    date_end = fields.Date(
        string="End Date",
        default=fields.Date.context_today,
    )

    points_winner = fields.Integer(
        string="Winner Points",
    )

    points_looser = fields.Integer(
        string="Looser Points",
    )
    game_ids = fields.One2many("sport.game", "league_id", string="Game")
    game_count = fields.Integer("Games", compute="_compute_game_count")
    league_line_ids = fields.One2many(
        "sport.league.line", "league_id", string="League Classifications"
    )

    _sql_constraints = [
        (
            "date_check",
            "CHECK ( (date_start < date_end))",
            "The start date must be anterior to the end date.",
        )
    ]

    @api.depends("game_ids")
    def _compute_game_count(self):
        for record in self:
            record.game_count = len(record.game_ids)

    @api.constrains("date_start", "date_end")
    def _check_dates(self):
        for record in self:
            if record.date_start > record.date_end:
                raise ValidationError("Start date must be prior to end date")

    def action_compute_classification(self):
        for record in self:
            for line in record.league_line_ids:
                games_won = self.env["sport.game"].search(
                    [
                        ("team_winner_id", "=", line.team_id.id),
                        ("league_id", "=", self.id),
                    ]
                )
                games_lost = self.env["sport.game"].search(
                    [
                        ("team_looser_id", "=", line.team_id.id),
                        ("league_id", "=", self.id),
                    ]
                )
                line.points = sum(game["points_winner"] for game in games_won)
                line.points += sum(game["points_looser"] for game in games_lost)

    def _cron_set_classification(self):
        leagues = self.search([])
        leagues.action_compute_classification()

    def action_view_games(self):
        return {
            "name": "Games",
            "type": "ir.actions.act_window",
            "res_model": "sport.game",
            "view_mode": "tree,form",
            "domain": [("id", "in", self.game_ids.ids)],
        }
