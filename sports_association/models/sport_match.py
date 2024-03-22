# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class SportMatch(models.Model):
    _name = "sport.match"
    _description = "Sport Match"

    sport_id = fields.Many2one("sport.sport", string="Sport")
    date = fields.Datetime(string="Match date and time")
    winner_team_id = fields.Many2one(
        "sport.team",
        string="Winner Team",
        compute="_compute_winner_team_id",
        store=True,
    )
    win_score = fields.Integer(string="Score to win", default=3)
    match_line_ids = fields.One2many(
        "sport.match.line", "match_id", string="Match lines"
    )
    league_id = fields.Many2one("sport.league", string="League")

    @api.depends("match_line_ids.score")
    def _compute_winner_team_id(self):
        for record in self:
            winner = record.match_line_ids.sorted(key=lambda r: r.score, reverse=True)
            record.winner_team_id = winner[0].team_id.id if winner else False
            # with filtered
            # winner = record.match_line_ids.filtered(lambda r: r.score == max(record.match_line_ids.mapped('score')))


# Match Lines Model


class SportMatchLine(models.Model):
    _name = "sport.match.line"
    _description = "Sport Match Line"

    match_id = fields.Many2one("sport.match", string="Match")
    team_id = fields.Many2one("sport.team", string="Team")
    score = fields.Integer(string="Score")
