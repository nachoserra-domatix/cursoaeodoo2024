from odoo import models, fields

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'

    name = fields.Char(string='Name', required=True)
    player_ids = fields.One2many('sport.player','team_id',string='Player')
    sport_id = fields.Many2one('sport.sport',string='Sport')
    logo = fields.Image(string='Logo')

    def action_checkall_starter(self):
        for record in self.player_ids:
            #record.starter = True
            record.action_check_starter()

    def action_uncheckall_starter(self):
        for record in self.player_ids:
            #record.starter = False
            record.action_uncheck_starter()
