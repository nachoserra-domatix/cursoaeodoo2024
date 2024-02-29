from odoo import models, fields

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team', string='Team')
    headline = fields.Boolean(string='Headline')