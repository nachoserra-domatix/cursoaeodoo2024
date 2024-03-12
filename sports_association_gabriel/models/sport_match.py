from odoo import models, fields, api


class SportMatch(models.Model):
    _name = "sport.match"
    _description = "Sport Match"
    _rec_name = "sport_id"

    sport_id = fields.Many2one('sport.sport', string='Sport')
    match_date = fields.Datetime(string='Match Date')
    match_winner = fields.Many2one('sport.team', string='Match Winner', compute='_compute_match_winner', store=True)
    points = fields.Integer(string='Points for the winner', default=3)
    match_line_ids = fields.One2many('sport.match.line', 'match_id', string='Match Lines')

    @api.depends('match_line_ids.score')
    def _compute_match_winner(self):
        for record in self:
            winner = record.match_line_ids.sorted(key=lambda r: r.score, reverse=True)
            record.match_winner = winner[0].team_id.id if winner else False


class SportMatchLine(models.Model):
    _name = "sport.match.line"
    _description = "Sport Match Line"

    team_id = fields.Many2one('sport.team', string='Team')
    score = fields.Integer(string='Score')
    match_id = fields.Many2one('sport.match', string='Match')
