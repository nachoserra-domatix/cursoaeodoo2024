from odoo import models, fields, api

class SportMatch(models.Model):
    _name = 'sport.match'
    _description = 'Sport Match'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']

    sport_id = fields.Many2one('sport.sport', string='Sport')
    date_time = fields.Datetime(string='Date')
    winner = fields.Many2one('sport.team', string='Winner', compute="_compute_winner_team_id", store=True)
    matchpoints = fields.Integer(string='Points', default='3')
    match_result_ids = fields.One2many('sport.match.result', 'result_id', string='Result')

    #league_id = related
    league_id = fields.Many2one('sport.league', string='League')

    @api.depends('match_result_ids.score')
    def _compute_winner_team_id(self):
        for record in self:
            winner = record.match_result_ids.sorted(key=lambda r: r.score, reverse=True)
            record.winner = winner[0].team_id.id if winner else False

class SportMatchResult(models.Model):
    _name = 'sport.match.result'
    _description = 'Sport Match Result'

    team_id = fields.Many2one('sport.team', string='Team')
    score = fields.Integer(string='Score')
    result_id = fields.Many2one('sport.match', string='Match')
