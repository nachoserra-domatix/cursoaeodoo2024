from odoo import models, fields

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Player'

    active = fields.Boolean(default=True, copy=False)
    name = fields.Char(string='Player Name', required=True, copy=False)
    age = fields.Integer(copy=False)
    position = fields.Char(copy=False)
    team_id = fields.Many2one(comodel_name='sport.team')
    is_starter = fields.Boolean(default=True, copy=False)
    sport_name = fields.Char(related='team_id.sport_id.name', store=True, copy=False)

    def action_starter (self):
        self.is_starter=True
    
    def action_reserve (self):
        self.is_starter=False