from odoo import fields,api,models

class SportMatchLine(models.Model):
    _name = 'sport.match.line'
    _description = 'Sport Match Line'
    _order = 'score desc'

    team_id = fields.Many2one('sport.team', string='Team')
    score = fields.Integer('Score')
    match_id = fields.Many2one('sport.match', string='Match')
