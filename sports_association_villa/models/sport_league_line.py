from odoo import fields, models, api, Command

class SportLeagueLine(models.Model):
    _name = 'sport.league.line'
    _description = 'Sport League Line'
    _order = 'points desc'

    team_id = fields.Many2one('sport.team', string='Team', required=True)
    points = fields.Integer(string='Points', required=False)
    sport_league_id = fields.Many2one('sport.league', string='League')