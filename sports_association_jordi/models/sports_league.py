from odoo import models, fields

class SportsLeague(models.Model):
    _name = 'sports.league'
    _description = 'Sports League'

    name = fields.Char(string='Name',required=True)
    sport_id = fields.Many2one('sports.sport',string='Sport')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    league_lines = fields.One2many('sports.league.line','league_id',string='League Lines')
    
    def action_recalculate_points(self):
        for record in self.league_lines:
            team =record.team_id
            score_points=self.env['sports.match'].search([('winner_team_id','=',team.id)]).mapped('winner_score')
            record.points = sum(score_points)

    def _cron_set_score(self):
        leagues = self.env['sports.league'].search([])
        for league in leagues:
            league.action_recalculate_points()