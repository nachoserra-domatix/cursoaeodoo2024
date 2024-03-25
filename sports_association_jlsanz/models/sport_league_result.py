from odoo import models, fields

class SportLeageResult(models.Model):
    _name = 'sport.league.result'
    _description = 'Sport League Result'
    _order = 'team_points desc'

    team_id = fields.Many2one('sport.team', string='Name', required=True)
    team_points = fields.Integer(string='Points')
    league_id = fields.Many2one('sport.league',string='League')
