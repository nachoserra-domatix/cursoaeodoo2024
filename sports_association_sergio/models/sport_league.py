from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class SportLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_line_ids = fields.One2many('sport.league.line', 'league_id', string="League Lines")
    match_ids = fields.One2many('sport.match', 'league_id', string="Matches")
    match_count = fields.Integer(string='Match Count', compute='_compute_match_count')

    # _sql_constraints = [('end_date_greater_start_date', 'CHECK (end_date >= start_date)', 'End date must be equal or greater than Start date')]

    def _compute_match_count(self):
        for record in self:
            record.match_count = len(record.match_ids)
    
    def set_score(self):
        for record in self.league_line_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('winner_id', '=', team.id)]).mapped('won_points')
            record.points = sum(score_points)

    def _cron_set_score(self):
        leagues = self.env['sport.league'].search([])
        leagues.set_score()

    @api.constrains('end_date', 'start_date')
    def _check_end_date(self):
        for record in self:
            if record.end_date < record.start_date:
                raise ValidationError(_('End date must be equal or greater than Start date'))
            
    def action_view_matches(self):
        # action = self.env.ref('sports_association_sergio.action_sport_match').read()[0]
        # action['domain'] = [('league_id', '=', self.id)]
        # return action

        return {
            'name': 'Matches',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.match',
            'view_mode': 'tree,form',
            'domain': [('league_id', '=', self.id)],
        }            

class SportLeagueLine(models.Model):
    _name = 'sport.league.line'
    _description = 'Sport League Line'
    _order = 'points desc'

    league_id = fields.Many2one('sport.league', string='League')
    team_id = fields.Many2one('sport.team', string='Team')
    points = fields.Integer(string='Points')