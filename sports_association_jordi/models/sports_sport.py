from odoo import models, fields

class SportsSport(models.Model):
    _name = 'sports.sport'
    _description = 'Sports Sport'

    name = fields.Char(string='Name',required=True,translate=True)
    description = fields.Text(string='Description')
    team_ids = fields.One2many('sports.team','sport_id',string='Teams')