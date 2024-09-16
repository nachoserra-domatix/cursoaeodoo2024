from odoo import fields, models, api, Command

class SportMatch(models.Model):
    _name = 'sport.match'
    _description = 'Sport Match'

    sport_id = fields.Many2one('sport.sport', string='Sport')
    start_date = fields.Datetime(string='Date', required=False)
    winner_id = fields.Many2one('sport.team', string='Winner', compute='_compute_winner', store=True)
    score_winner = fields.Integer(string='Score Winner', required=False, default=3)
    sport_match_line_ids = fields.One2many('sport.match.line', 'sport_match_id', string='Match Lines')

    @api.depends('sport_match_line_ids.score')
    def _compute_winner(self):
        for match in self:
            winner = False
            highest_score = 0
            for line in match.sport_match_line_ids:
                if line.score > highest_score:
                    highest_score = line.score
                    winner = line.team_id
            match.winner_id = winner