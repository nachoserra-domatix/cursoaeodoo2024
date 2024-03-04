# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string='Nombre', required=True)
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    coach_id = fields.Many2one('res.partner', string='Coach')
    logo = fields.Image('Logo')    
    total_players = fields.Integer(compute="_compute_total_players")

    @api.depends("player_ids")
    def _compute_total_players(self):
        for record in self:
            record.total_players = len(record.player_ids)
    
    #=== METHODS ===#

    def action_all_starters (self):
        for rec in self.player_ids:            
                rec.action_starter()