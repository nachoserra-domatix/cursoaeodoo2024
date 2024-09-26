from odoo import models, fields, api



class SportMatch(models.Model):
    _name = 'sport.match'
    _description = 'Sport Match'

    sport_id = fields.Many2one(comodel_name='sport.sport', string='Sport')
    date_and_time = fields.Datetime(string='Date and time')
    winner_team_id = fields.Many2one(comodel_name='sport.team', string='Winner')
    score_winning = fields.Integer('Score Winning', default=3)
    match_line_ids = fields.One2many(comodel_name='sport.match.line', inverse_name='match_id', string='Match Lines')

    league_id = fields.Many2one(comodel_name='sport.league', string='League')

    @api.depends('match_line_ids.score')
    def set_score(self):
        for record in self.sport_league_ids:
            team = record.team_id
            score_points = self.env['sport. match'].search([('sport_id', '=', self.sport_id.id), ('winner_team_id', '=', team.id)]).mapped('score_winning')
            record.points = sum(score_points)

    
    
    
    
    
