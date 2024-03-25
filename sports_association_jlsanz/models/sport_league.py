from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SportLeage(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    sport_id = fields.Many2one('sport.sport', string='sport')

    league_result_ids = fields.One2many('sport.league.result', 'league_id', string='League Results')

    match_ids = fields.One2many('sport.match', 'league_id', string='Matches')

    match_count = fields.Integer('Match Count', compute='_compute_match_count')

    def _compute_match_count(self):
        for record in self:
            record.match_count = len(record.match_ids)

    def set_score(self):
        for record in self.league_result_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('winner', '=', team.id)]).mapped('matchpoints')
            record.team_points = sum(score_points)

    def _cron_set_score(self):
        leagues = self.search([])
        leagues.set_score()

    # _sql_constraints = [
    #   ('start_date_greater', 'check(start_date > end_date)', "The league start date must be before its end date.")
    # ]

    @api.constrains('end_date', 'start_date')
    def _verify_dates(self):
        for record in self:
            if record.start_date > record.end_date:
                raise ValidationError(_("The end date must be after start date."))

    def action_view_match(self):
        return {
            'name': 'Matches',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.match',
            'view_mode': 'tree,form',
            'domain': [('league_id', '=', self.id)],
        }