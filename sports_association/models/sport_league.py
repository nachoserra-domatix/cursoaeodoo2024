from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SportLeague(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name', required=True, translate=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    sport_id = fields.Many2one(comodel_name='sport.sport', string='Sport')
    sport_league_ids = fields.One2many(comodel_name='sport.league.line', inverse_name='league_id', string='League Lines')

    match_ids = fields.One2many(comodel_name='sport.match', inverse_name='league_id', string='Matches')

    match_count = fields.Integer(string='Match count', compute='_compute_match_count')

    # SI EL CONSTRAINT NO SE CUMPLE EN LOS REGISTROS YA CREADOS (INCLUIDOS LOS ARCHIVADOS) EL CONSTRAINT NO FUNCIONARÁ
    # _sql_constraints = [
    #     ('_league_date_greater', 'check(end_date >= date_start)', 'Start Date cannot be after End Date.')
    # ]

    @api.constrains('start_date','end_date')
    def _check_start_date_is_before_end_date(self):
        for record in self:
            if record.start_date and record.end_date and record.start_date > record.end_date:
                raise ValidationError("Start Date cannot be after End Date.")

    def _compute_match_count(self):
        for record in self:
            record.match_count = len(record.match_ids)


    def set_score(self):
        for record in self.sport_league_ids:
            team = record.team_id
            score_points = self.env['sport.match'].search([('sport_id', '=', self.sport_id.id), ('sinner_team_id', '=', team.id)]).mapped('score_winning')
            record.points = sum(score_points)
    

    def cronsetscore(self):
        leagues = self.search([])
        leagues.set_score()
    
    def action_view_matches(self):

        return {
            'name': 'Matches',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.match',
            'view_mode': 'tree,form',
            'domain': [('league_id', '=', self.id)]
        }