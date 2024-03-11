from odoo import models, fields

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Player'

    name = fields.Char(string='Player Name', required=True)
    age = fields.Integer()
    position = fields.Char()
    team_id = fields.Many2one(comodel_name='sport.team')
    is_starter = fields.Boolean(default=True)
    sport_name = fields.Char(related='team_id.sport_id.name', store=True)

    def action_starter (self):
        self.is_starter=True
    
    def action_reserve (self):
        self.is_starter=False