from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SportLeague(models.Model):
    _name = "sport.league"
    _description = "Sport League"

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_line_ids = fields.One2many('sport.league.line', 'league_id', string='League Lines')
    match_ids = fields.One2many('sport.match', 'league_id', string='Calendar')
    num_matches = fields.Integer(string='Number of matches', compute='_compute_num_matches')

    # _sql_constraints = [
    #     ('start_date_greater', 'check(start_date >= end_date)', "The league end date must be after the start date.")
    # ]

    @api.depends('match_ids')
    def _compute_num_matches(self):
        for record in self:
            record.num_matches = len(record.match_ids)

    @api.constrains('end_date', 'start_date')
    def _verify_dates(self):
        for record in self:
            if record.end_date <= record.start_date:
                raise ValidationError(_("The league end date must be after the start date."))
                
    def action_view_matches(self):
        return {
            'name': 'Matches',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.match',
            'view_mode': 'tree,form',
            'domain': [('league_id', '=', self.id)]
        }

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
    _sql_constraints = [('team_unique_in_league', 'UNIQUE(league_id, team_id)', 'Team must be unique in match')]

    team_id = fields.Many2one('sport.team', string='Team')
    points = fields.Integer(string='Points')
    league_id = fields.Many2one('sport.league', string='League')
    
    
