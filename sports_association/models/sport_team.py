from odoo import models, fields



class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string='Name', required=True, translate=True)
    logo = fields.Image(string='Logo')
    player_ids = fields.One2many(comodel_name='sport.player', inverse_name='team_id', string='Jugadores')
    sport_id = fields.Many2one(comodel_name='sport.sport', string='Sport')
    
    def set_starters(self):
        for player in self.player_ids:
            player.set_starter()
    
    def set_substitutes(self):
        for player in self.player_ids:
            player.set_substitute()
    
    
