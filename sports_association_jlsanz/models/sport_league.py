from odoo import models, fields

class SportLeage(models.Model):
    _name = 'sport.league'
    _description = 'Sport League'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    sport_id = fields.Many2one('sport.sport', string='sport')

    league_result_ids = fields.One2many('sport.league.result', 'league_id', string='League Results')
