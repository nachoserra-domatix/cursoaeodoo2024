# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api

class SportLeague(models.Model):
    _name ='sport.league'
    _description = 'Sport League'
    
    name = fields.Char('Name', required=True)
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    sport_league_ids = fields.One2many('sport.league.line', 'league_id', string='League lines')
    match_ids = fields.One2many('sport.match', 'league_id', string='Matches')
    match_count = fields.Integer('Match Count', compute='_compute_match_count')
    
    def _compute_match_count(self):
        for record in self:
            record.match_count = len(record.match_ids)

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date > record.end_date:
                raise models.ValidationError('The league start date must be before its end date.')

    def set_score(self):
        for record in self.sport_league_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('winner_team_id', '=', team.id)]).mapped('score_winning')
            record.points = sum(score_points)
    
    def _cron_set_score(self):
        leagues = self.search([])
        leagues.set_score()
    
    # Smart button for matches
    def action_view_match(self):
        # action = self.env.ref('sports_association.action_sport_match').read()[0]
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
    _name ='sport.league.line'
    _description = 'Sport League Line'
    _order = 'points desc'
    
    league_id = fields.Many2one('sport.league', string='League')
    team_id = fields.Many2one('sport.team', string='Team')
    points = fields.Integer('Points')