from odoo import models, fields

class SportLeagueLine(models.Model):
    _name = 'sport.league.line'
    _description = "Sport League Line"
    _order = 'points desc'

    team_id = fields.Many2one('sport.team', string='Team')
    points = fields.Integer('Points')
    league_id = fields.Many2one('sport.league', string='League')