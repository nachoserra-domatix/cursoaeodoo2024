from odoo import models, fields

class SportLeage(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    sport_id = fields.Many2one('sport.sport', string='sport')

    league_result_ids = fields.One2many('sport.league.result', 'league_id', string='League Results')

    def set_score(self):
        for record in self.league_result_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('winner', '=', team.id)]).mapped('matchpoints')
            record.team_points = sum(score_points)

    def _cron_set_score(self):
        leagues = self.search([])
        leagues.set_score()
