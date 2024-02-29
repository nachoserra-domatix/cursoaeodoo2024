from odoo import models, fields

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = "Sport Player"

    name = fields.Char(string='Name', required=True)
    bird_date = fields.Date(string='Bird Date')
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team',string='Team')
    regular = fields.Boolean(string='Regular')

    def action_mark_regular(self):
        for record in self:
            record.regular = True;

    def action_unmark_regular(self):
        for record in self:
            record.regular = False;