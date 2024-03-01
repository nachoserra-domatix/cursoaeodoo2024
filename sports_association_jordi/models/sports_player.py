from odoo import models, fields

class SportsPlayer(models.Model):
    _name = 'sports.player'
    _description = 'Sports Player'

    name = fields.Char(string='Name',required=True)
    age = fields.Integer(string='Age')
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sports.team',string='Team')
    starter = fields.Boolean(string='Starter')

    def make_starter(self):
        self.starter = True
        return True
    
    def make_substitute(self):
        self.starter = False
        return True


   