from odoo import models, fields, api

class SportMatch(models.Model):
    _name = 'sport.match'
    _description = 'Sport Match'

    name = fields.Char(string='Name', required=True)
    match_datetime = fields.Datetime(string='Match Datetime')
    winner_id = fields.Many2one('sport.team', string='Winner', compute='_compute_winner', store=True)
    won_points = fields.Integer(string='Won Points', default=3)
    match_line_ids = fields.One2many('sport.match.line', 'match_id', string="Match Lines")
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_id = fields.Many2one('sport.league', string='League')


    @api.depends('match_line_ids.score')
    def _compute_winner(self):
        for record in self:
            if record.match_line_ids:
                record.winner_id = record.match_line_ids.sorted(key=lambda r: r.score, reverse=True)[0].team_id
            else:
                record.winner_id = False
    

class SportMatchLine(models.Model):
    _name = 'sport.match.line'
    _description = 'Sport Match Line'

    match_id = fields.Many2one('sport.match', string='Match')
    team_id = fields.Many2one('sport.team', string='Team')
    score = fields.Integer(string='Score')

    _sql_constraints = [('team_unique_in_match', 'UNIQUE(match_id, team_id)', 'Team must be unique in match')]