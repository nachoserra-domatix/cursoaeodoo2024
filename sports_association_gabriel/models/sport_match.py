from odoo import models, fields, api


class SportMatch(models.Model):
    _name = "sport.match"
    _description = "Sport Match"
    _rec_name = "sport_id"

    name = fields.Char(string='Match', compute='_compute_name', store=True)
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_id = fields.Many2one('sport.league', string='League')
    match_date = fields.Datetime(string='Match Date')
    match_winner = fields.Many2one('sport.team', string='Match Winner', compute='_compute_match_winner', store=True)
    points = fields.Integer(string='Points for the winner', default=3)
    match_line_ids = fields.One2many('sport.match.line', 'match_id', string='Match Lines')

    @api.depends('match_line_ids.score')
    def _compute_match_winner(self):
        for record in self:
            winner = record.match_line_ids.sorted(key=lambda r: r.score, reverse=True)
            record.match_winner = winner[0].team_id.id if winner else False

    @api.depends('match_line_ids.team_id')
    def _compute_name(self):
        for record in self:
            try:
                teams = []
                for line in record.match_line_ids:
                    teams.append(line.team_id)
                record.name = teams[0].name + " - " + teams[1].name
            except:
                continue            


class SportMatchLine(models.Model):
    _name = "sport.match.line"
    _description = "Sport Match Line"
    _sql_constraints = [('team_unique_in_match', 'UNIQUE(match_id, team_id)', 'Team must be unique in match')]

    team_id = fields.Many2one('sport.team', string='Team')
    score = fields.Integer(string='Score')
    match_id = fields.Many2one('sport.match', string='Match')
