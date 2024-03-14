from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SportsLeague(models.Model):
    _name = 'sports.league'
    _description = 'Sports League'

    name = fields.Char(string='Name',required=True)
    sport_id = fields.Many2one('sports.sport',string='Sport')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    league_lines = fields.One2many('sports.league.line','league_id',string='League Lines')
    match_count = fields.Integer(string='Match Count',compute='_compute_match_count')

    _sql_constraints = [
         ('start_date_end_date_check', 'CHECK (start_date <= end_date)', 'The start date must be anterior to the end date.')
    ]
    
    @api.constrains('start_date','end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date > record.end_date:
                raise ValidationError('The start date must be anterior to the end date.')
    
    def _compute_match_count(self):
        for record in self:
            league=record.id
            record.match_count = len(self.env['sports.match'].search([('league_id','=',league)]).mapped('id'))

    def action_recalculate_points(self):
        for record in self.league_lines:
            team =record.team_id
            score_points=self.env['sports.match'].search([('winner_team_id','=',team.id)]).mapped('winner_score')
            record.points = sum(score_points)

    def _cron_set_score(self):
        leagues = self.env['sports.league'].search([])
        for league in leagues:
            league.action_recalculate_points()
    
    def action_show_matches(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Matches',
            'res_model': 'sports.match',
            'view_mode': 'tree,form',
            'domain': [('league_id', '=', self.id)],
        }