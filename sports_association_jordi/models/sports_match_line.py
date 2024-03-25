from odoo import models, fields

class SportsMatchLine(models.Model):
    _name = 'sports.match.line'
    _description = 'Sports Match Line'

    match_id = fields.Many2one('sports.match',string='Match')
    team_id = fields.Many2one('sports.team',string='Team')
    score = fields.Integer(string='Score')