# Copyright 2024 potxolate
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models, fields

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Player'

    name = fields.Char(string='Player Name', required=True)
    birthdate = fields.Date('Birthdate')
    age = fields.Integer('Age', compute='_compute_age', store=True)
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team', string='Team')
    is_starter = fields.Boolean(string='Starter', default=True)
    photo = fields.Image(string="Photo")
    sport_name = fields.Char('Sport', related='team_id.sport_id.name')

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = (fields.Date.today() - record.birthdate).days / 365
            else:
                record.age = 0
    
    #=== METHODS ===#

    def action_starter (self):
        self.is_starter=True
    
    def action_reserve (self):
        self.is_starter=False