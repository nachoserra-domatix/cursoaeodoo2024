from odoo import models, fields, api, Command

class SportTeam(models.Model):

    _name = 'sport.team'
    _description = 'Sport team'

    name = fields.Char(string="Name")
    logo = fields.Image('Logo')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')
    color = fields.Integer('Color')

    members = fields.Integer('Members', compute='_compute_members')

    def mark_all_as_titular(self):
        self.player_ids.write({
            "titular": True
        })

    def unmark_all_as_titular(self):
        self.player_ids.write({
            "titular": False
        })

    def get_all_unasigned(self):
        for rec in self:
            unasigned_players = self.env['sport.player'].search([('team_id', '=', False),('age','<',30)])
            for player in unasigned_players:
                player.team_id = rec
                

    @api.depends('player_ids')
    def _compute_members(self):
        self.members = len(self.player_ids)
