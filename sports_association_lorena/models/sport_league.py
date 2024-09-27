from odoo import models, fields

class SportLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name')
    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_line = fields.One2many('sport.league.line', 'league_id', string='League line')

    def set_score(self):
        for record in self.sport_league_ids:
            team = record.team_id
            score_points = self.env['sport.']
            
    def _cron_set_score(self):
        leagues = self.search([])
        leagues.set_score()