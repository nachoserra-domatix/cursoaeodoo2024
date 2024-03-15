# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields
from odoo.exceptions import ValidationError


class SportLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name')
    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Fecha de fin')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_line_ids = fields.One2many('sport.league.line', 'league_id', string='League Lines')
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

    #=== METHODS ===#
    
    def set_score(self):
        for record in self.league_line_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('winner_team_id', '=', team.id)]).mapped('win_score')
            record.points = sum(score_points)
    
    def action_view_match(self):
        # action = self.env.ref('sports_association_nacho.action_sport_match').read()[0]
        # action['domain'] = [('league_id', '=', self.id)]
        # return action
        return {
            'name': 'Matches',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.match',
            'view_mode': 'tree,form',
            'domain': [('league_id', '=', self.id)],
        }