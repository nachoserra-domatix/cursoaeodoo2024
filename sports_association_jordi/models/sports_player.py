from odoo import models, fields,api
from datetime import datetime

class SportsPlayer(models.Model):
    _name = 'sports.player'
    _description = 'Sports Player'

    name = fields.Char(string='Name',required=True)
    age = fields.Integer(string='Age',compute='_compute_age',store=True,copy=False)
    position = fields.Char(string='Position',copy=False)
    team_id = fields.Many2one('sports.team',string='Team')
    starter = fields.Boolean(string='Starter',default=True,copy=False)
    sport_name = fields.Char(string="Sport Name",related='team_id.sport_id.name', store=True)
    date_of_birth = fields.Date(string='Date of Birth',copy=False)
    active = fields.Boolean(string='Active',default=True,copy=False)

    def make_starter(self):
        self.starter = True
        return True
    
    def make_substitute(self):
        self.starter = False
        return True
    @api.depends('date_of_birth')    
    def _compute_age(self):
        for player in self:
            if player.date_of_birth:
                player.age = (datetime.today().date() - player.date_of_birth).days / 365
            else:
                player.age = 0

   