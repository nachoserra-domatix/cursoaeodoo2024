# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportMatch(models.Model):
    _name ='sport.match'
    _description = 'Sport Match'
    
    sport_id = fields.Many2one('sport.sport', string='Sport')
    date_match = fields.Datetime('Date Match')
    winner = fields.Char('Winner')
    points = fields.Integer('Points', default='3')
    match_line_ids = fields.One2many('sport.match.line', 'match_id', string='Match Line')

class SportMatchLine(models.Model):
    _name ='sport.match.line'
    _description = 'Sport Match Line'
    
    match_id = fields.Many2one('sport.match', string='Match')
    team_id = fields.Many2one('sport.team', string='Team')
    points = fields.Integer('Points')