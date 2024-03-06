from odoo import fields,api,models

class SportMatch(models.Model):
    _name = 'sport.match'
    _description = 'Sport Match'

    sport_id = fields.Many2one(comodel_name='sport.sport', string='Sport')
    date = fields.Datetime('Date')
    winner_team_id = fields.Many2one(comodel_name='sport.team', compute="_compute_winner_team_id", store=True)
    score_winner_team = fields.Integer(default=3)
    match_line_ids = fields.One2many(
        comodel_name='sport.match.line', 
        inverse_name='match_id', 
        string='Match Lines'
    )

    @api.depends('match_line_ids.score')
    def _compute_winner_team_id(self):
        for record in self:
            winner = record.match_line_ids.sorted(key=lambda r: r.score, reverse=True)
            record.winner_team_id = winner[0].team_id.id if winner else False
