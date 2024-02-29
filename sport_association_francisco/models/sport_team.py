from odoo import models, fields

class SportTeam(models.Model):

    _name = 'sport.team'
    _description = 'Sport team'

    name = fields.Char(string="Name")
    logo = fields.Binary('Logo')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')

    def mark_all_as_titular(self):
        self.player_ids.write({
            "titular": True
        })

    def unmark_all_as_titular(self):
        self.player_ids.write({
            "titular": False
        })
