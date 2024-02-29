from odoo import models, fields

class SportPlayer(models.Model):

    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string="Name")
    age = fields.Integer(string='Age')
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team', string='Team')
    titular = fields.Boolean(string='Titular')

    def mark_as_titular(self):
        self.write({
            "titular": True
        })

    def unmark_as_titular(self):
        self.write({
            "titular": False
        })
