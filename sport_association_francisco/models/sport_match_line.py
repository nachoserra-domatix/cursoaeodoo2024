from odoo import models, fields, api, Command

class SportMatchLine(models.Model):

    _name = 'sport.match.line'
    _description = 'Sport Match Line'

    team_id = fields.Many2one('sport.team', string='Team')
    total_score = fields.Integer('Total Score')
    match_id = fields.Many2one('sport.match', string='Match')
    