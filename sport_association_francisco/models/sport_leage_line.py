from odoo import models, fields, api, Command

class SportleageLine(models.Model):

    _name = 'sport.leage.line'
    _description = 'Sport Leage Line'

    team_id = fields.Many2one('sport.team', string='Team')
    leage_id = fields.Many2one('sport.leage', string='Leage')
    score = fields.Integer(string="Score")
