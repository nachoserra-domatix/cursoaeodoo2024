from odoo import models, fields

class SportLeagueLine(models.Model):
    _name = 'sport.league.line'
    _description = 'Sport League Line'
    _order = 'points desc'

    league_id = fields.Many2one('sport.league', string='League')
    team_id = fields.Many2one('sport.team', string='Team')
    points = fields.Integer(string='Points', default=0)
    goals_for = fields.Integer(string='Goals For', default=0)
    goals_against = fields.Integer(string='Goals Against', default=0)
    goals_difference = fields.Integer(string='Goals Difference', compute='_compute_goals_difference', store=True)

    def _compute_goals_difference(self):
        for record in self:
            record.goals_difference = record.goals_for - record.goals_against

