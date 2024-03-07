# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class SportMatch(models.Model):
    _name = 'sport.match'
    _description = 'Sport Matchs'

    sport_id = fields.Many2one('sport.sport', string='Sport') 
    date = fields.Datetime(string='Match date and time')
    winner_team_id = fields.Many2one('sport.team', string='Team')
    win_score = fields.Integer(string='Score to win', default=3)
    match_line_ids = fields.One2many('sport.match.line', 'match_id', string='Match lines')

# Match Lines Model

class SportMatchLine(models.Model):
    _name = 'sport.match.line'
    _description = 'Sport Matchs Line'

    match_id = fields.Many2one('sport.match', string='Match')
    team_id = fields.Many2one('sport.team', string='Team')
    score = fields.Integer(string='Score')