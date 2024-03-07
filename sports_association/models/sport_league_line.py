from odoo import models, fields

class SportLeagueLine(models.Model):
    _name = "sport.league.line"
    _description = "Sport League Line"
    _order ="points desc"

    
    team_id = fields.Many2one(string='Team', comodel_name='sport.team')
    points = fields.Integer(string="Points")
    league_id = fields.Many2one(
        string='League',
        comodel_name='sport.league',
    )
