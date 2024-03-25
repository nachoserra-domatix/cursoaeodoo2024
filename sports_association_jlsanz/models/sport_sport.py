from odoo import models, fields

class SportSport(models.Model):
    _name = 'sport.sport'
    _description = 'Sport Sport'

    name = fields.Char('Name', required=True)
    description = fields.Char(string='Description')

    team_ids = fields.One2many('sport.team' ,'sport_id', string='Team')
