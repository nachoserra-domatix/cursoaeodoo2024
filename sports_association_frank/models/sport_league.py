from odoo import models, fields

class SportLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    sport_league_ids = fields.One2many(
        comodel_name='sport.league.line',
        inverse_name='league_id',
        string='League Lines'
    )

    def set_score(self):
        for rec in self.sport_league_ids:
            rec.points = sum(self.env['sport.match'].search([
                ('sport_id', '=', self.sport_id.id),
                ('winner_team_id', '=', rec.team_id.id),
            ]).mapped('score_winning'))

    def _cron_set_score(self):
        leagues = self.search([])
        leagues.set_score()
        return True
