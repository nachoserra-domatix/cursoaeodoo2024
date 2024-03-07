from odoo import models, fields

class SportMatch(models.Model):
    _name = 'sport.match'
    _description = 'Sport Match'

    sport_id = fields.Many2one('sport.sport', string='Sport')
    date_time = fields.Datetime(string='Date')
    winner = fields.Many2one('sport.team', string='Winner')
    matchpoints = fields.Integer(string='Points', default='3')
    match_result_ids = fields.One2many('sport.match.result', 'result_id', string='Result')

    #league_id = related

class SportMatchResult(models.Model):
    _name = 'sport.match.result'
    _description = 'Sport Match Result'

    team_id = fields.Many2one('sport.team', string='Team')
    score = fields.Integer(string='Score')
    result_id = fields.Many2one('sport.match', string='Match')
