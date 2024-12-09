from odoo import models, fields

class SportMatch(models.Model):
    _name = 'sport.match'
    _description = 'Sport Match'

    sport = fields.Many2many('sport.sport', string='Sport')
    match_day = fields.Datetime(string='Match day')
    winner_team = fields.Many2one('sport.team', string='Winner team')
    rating = fields.Integer(string='Rating', default=3)
    match_line = fields.One2many('sport.match.lines', 'match_id', string='Match line')