from odoo import models, fields

class SportMatchLines(models.Model):
    _name = 'sport.match.lines'
    _description = 'Sport Match Lines'

    team_id = fields.Many2one('sport.team', string='Team')
    rating = fields.Integer(string='Rating')
    match_id = fields.Many2one('sport.match', string='Match')