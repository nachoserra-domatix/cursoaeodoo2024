from odoo import models, fields

class SportsTeam(models.Model):
    _name = 'sports.team'
    _description = 'Sports Team'

    name = fields.Char(string='Name',required=True)
    logo = fields.Image(string='Logo')
    players_ids = fields.One2many('sports.player','team_id',string='Players')
    sport_id = fields.Many2one('sports.sport',string='Sport')


    def all_marked(self):
        for player in self.players_ids:
            player.make_starter()
        return True
    
    def all_substitute(self):
        for player in self.players_ids:
            player.make_substitute()
        return True