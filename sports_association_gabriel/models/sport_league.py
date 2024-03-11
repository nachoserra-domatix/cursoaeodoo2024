from odoo import models, fields


class SportLeague(models.Model):
    _name = "sport.league"
    _description = "Sport League"

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_line_ids = fields.One2many('sport.league.line', 'league_id', string='League Lines')

    def action_calculate_points(self):
        for record in self:
            for line in record.league_line_ids:
                match_won_ids = self.env['sport.match'].search([('match_winner', '=', line.team_id.id)])
                for match_won in match_won_ids:
                    line.points += match_won.points

    def _cron_set_points(self):
        leagues = self.search([])
        leagues.action_calculate_points()


class SportLeagueLine(models.Model):
    _name = "sport.league.line"
    _description = "Sport League Line"
    _order = 'points desc'

    team_id = fields.Many2one('sport.team', string='Team')
    points = fields.Integer(string='Points')
    league_id = fields.Many2one('sport.league', string='League')
    
    
