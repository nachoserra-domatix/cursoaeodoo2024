# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string='Nombre', required=True)
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    coach_id = fields.Many2one('res.partner', string='Coach')

    #=== METHODS ===#

    def action_all_starters (self):
        for rec in self.player_ids:            
                rec.action_starter()