# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportLeagueLine(models.Model):
    _name = 'sport.league.line'
    _description = 'Sport League Line'

    team_id = fields.Many2one('sport.team', string='Team')
    league_id = fields.Many2one('sport.league', string='League')
    score = fields.Integer(string='Score')