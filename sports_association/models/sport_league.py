# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields

class SportLeague(models.Model):
    _name ='sport.league'
    _description = 'Sport League'
    
    name = fields.Char('Name', required=True)
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    sport_league_ids = fields.One2many('sport.league.line', 'league_id', string='League lines')
    
    def set_score(self):
        pass
    
class SportLeagueLine(models.Model):
    _name ='sport.league.line'
    _description = 'Sport League Line'
    _order = 'points desc'
    
    league_id = fields.Many2one('sport.league', string='League')
    team_id = fields.Many2one('sport.team', string='Team')
    points = fields.Integer('Points')