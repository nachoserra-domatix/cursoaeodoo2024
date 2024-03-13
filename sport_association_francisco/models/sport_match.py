from odoo import models, fields, api, Command

class SportMatch(models.Model):

    _name = 'sport.match'
    _description = 'Sport Match'
    _rec_name = 'sport_id'

    sport_id = fields.Many2one('sport.sport', string='Sport')
    match_date = fields.Datetime('Match Date')
    winner_team_id = fields.Many2one('sport.team', string='Winner team', compute="compute_winner_team", store=True)
    up_score = fields.Integer('Up score', default=3)
    match_line_ids = fields.One2many('sport.match.line', 'match_id', string='Match Lines')
    color = fields.Integer(string='Color')

    @api.depends('match_line_ids')
    def compute_winner_team(self):
        for rec in self:
            if rec.match_line_ids:
                winner_team = rec.match_line_ids[0].team_id
                rec.winner_team_id = winner_team

    