from odoo import fields, models, api, Command

class SportLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name', required=True)
    begin_date = fields.Date(string='Begin Date', required=False)
    end_date = fields.Date(string='End Date', required=False)
    sport_id = fields.Many2one('sport.sport', string='Sport')
    sport_league_ids = fields.One2many('sport.league.line', 'sport_league_id', string='Leagues Lines')

    def set_score(self):
        for record in self.sport_league_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('winner_id', '=', team.id)]).mapped('score_winner')
            record.points = sum(score_points)