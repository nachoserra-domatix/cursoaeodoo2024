# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class SportLeagueMatch(models.TransientModel):
    _name = 'sport.league.match'
    _description = 'Create Matchs'

    team_ids = fields.Many2many('sport.team', string='Teams')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    date = fields.Datetime(string='Match date')

    def create_matchs(self):
        vals = {
        'date': self.date,            
        'sport_id': self.sport_id.id,
        'match_line_ids': [(0, 0, {'team_id': team.id}) for team in self.team_ids]
        }
        match = self.env['sport.match'].create(vals)

        return {
            'name': 'Match',
            'view_mode': 'form',
            'res_model': 'sport.match',
            'res_id': match.id,
            'type': 'ir.actions.act_window',
            'target': 'current',}