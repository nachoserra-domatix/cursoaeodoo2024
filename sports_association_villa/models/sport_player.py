from odoo import fields, models, api
from datetime import datetime
import wdb


class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char('Name', required=True)
    birtday = fields.Date(string ='Birthday')
    age = fields.Integer(string = 'Age', compute='_compute_age', store=True)
    position = fields.Char('Position')
    team_id = fields.Many2one('sport.team', string='Team')
    starting_player = fields.Boolean(string='Starting Player')
    sport = fields.Char('Sport', related='team_id.sport_id.name', store=True)
    color = fields.Integer(string ='Color', default=0)

    @api.depends('birtday')
    def _compute_age(self):
        # import pdb; pdb.set_trace()
        for record in self:
            if record.birtday:
                record.age = (fields.Date.today() - record.birtday).days // 365
                # wdb.set_trace()
            else:
                record.age = 0