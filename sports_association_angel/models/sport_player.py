from odoo import models, fields

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    position = fields.Char(string='Position')
    starter = fields.Boolean(string='Starter')
    team_id = fields.Many2one('sport.team', string='Team')

    def action_markself_starter(self):
        self.starter=True
    
    def action_unmarkself_starter(self):
        self.starter=False