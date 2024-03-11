# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class SportLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name')
    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Fecha de fin')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    league_line_ids = fields.One2many('sport.league.line', 'league_id', string='League Lines')

    #=== METHODS ===#
    
    def set_score(self):
        for record in self.league_line_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('winner_team_id', '=', team.id)]).mapped('win_score')
            record.points = sum(score_points)