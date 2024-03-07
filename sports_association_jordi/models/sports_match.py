from odoo import models, fields,api

class SportsMatch(models.Model):
    _name = 'sports.match'
    _description = 'Sports Match'

    date = fields.Datetime(string='Date')
    sport_id = fields.Many2one('sports.sport',string='Sport')
    # league_id = fields.Many2one('sports.league',string='League')
    winner_team_id = fields.Many2one('sports.team',string='Winner Team',compute='_compute_winner_team_id',store=True)
    winner_score = fields.Integer(string='Winner Score', default=3)
    match_lines = fields.One2many('sports.match.line','match_id',string='Match Lines')

    @api.depends('match_lines.score')
    def _compute_winner_team_id(self):
        for record in self:
            highest_score = 0
            for line in record.match_lines:
                if line.score > highest_score:
                    highest_score = line.score
                    record.winner_team_id = line.team_id
