from odoo import models, fields



class SportLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name', required=True, translate=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    sport_id = fields.Many2one(comodel_name='sport.sport', string='Sport')
    sport_league_ids = fields.One2many(comodel_name='sport.league.line', inverse_name='league_id', string='League Lines')

    def set_score(self):
        for record in self.sport_league_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('sinner_team_id', '=', team.id)]).mapped('score_winning')
            record.points = sum(score_points)
    

    def cronsetscore(self):
        leagues = self.search([])
        leagues.set_score()
    
