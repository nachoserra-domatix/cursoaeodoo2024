from odoo import models, fields



class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string='Name', required=True, translate=True)
    age = fields.Integer(string='Age')
    position = fields.Char(string='Positionn', required=True, translate=True)
    team_id = fields.Many2one(comodel_name='sport.team', string='Equipo')
    starter = fields.Boolean(string='Starter')    
    
    def set_starter(self):
        self.starter = True
    
    def set_substitute(self):
        self.starter = False