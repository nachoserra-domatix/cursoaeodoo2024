# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class SportLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sport League Line'

    name = fields.Char(string='Name')
    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Fecha de fin')
    #sport = fields.Char('sport', related='sport.sport.name')
    league_line_ids = fields.One2many('sport.league.line', 'league_id', string='League Lines')