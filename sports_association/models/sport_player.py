# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Player'

    name = fields.Char(string='Player Name', required=True)
    age = fields.Integer(string='Age')
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team', string='Team')
    is_starter = fields.Boolean(string='Starter')

    #=== METHODS ===#

    def action_starter (self):
        self.is_starter=True
    
    def action_reserve (self):
        self.is_starter=False