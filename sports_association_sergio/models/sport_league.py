from odoo import models, fields

class SportLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_line_ids = fields.One2many('sport.league.line', 'league_id', string="League Lines")

    def set_score(self):
        for record in self.league_line_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('winner_id', '=', team.id)]).mapped('won_points')
            record.points = sum(score_points)

class SportLeagueLine(models.Model):
    _name = 'sport.league.line'
    _description = 'Sport League Line'
    _order = 'points desc'

    league_id = fields.Many2one('sport.league', string='League')
    team_id = fields.Many2one('sport.team', string='Team')
    points = fields.Integer(string='Points')