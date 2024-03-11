from odoo import models, fields

class SportLeague(models.Model):
    _name = 'sport.league'
    _description = "Sport League"

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_line_ids = fields.One2many('sport.league.line', 'league_id', string='League Lines')
    game_ids = fields.One2many('sport.game', 'league_id', string='Games')

    def set_score(self):
        for record in self.league_line_ids:
            team = record.team_id
            score_points = self.env['sport.game'].search([('winner_team_id','=',team.id)]).mapped('winner_points')
            record.points = sum(score_points)

    def _cron_set_score(self):
        leagues = self.search([])
        leagues.set_score()
