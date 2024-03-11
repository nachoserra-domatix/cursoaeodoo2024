from odoo import models, fields

class SportTeam(models.Model):
    _name = 'sport.team'
    _description = 'Sport Team'
    _order = "sport_id, name"

    name = fields.Char(string='Nombre', required=True)
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    coach_id = fields.Many2one('sport.player', string='Coach')
    displayed_image_id = fields.Image(string='Displayed Image')
    color = fields.Integer(string='Color Index', default=0)
    player_count = fields.Integer(compute='_compute_player_count')

    def _compute_player_count(self):
        for rec in self:
            rec.player_count = len(rec.player_ids)

    def action_add_players(self):
        for rec in self:
            players = self.env['sport.player'].search([('team_id', '=', False), ('age', '<', 30)])
            rec.player_ids |= players

    def action_view_players(self):
        self.ensure_one()
        return {
            'name': 'Players',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.player',
            'view_mode': 'tree,form',
            'domain': [('team_id', '=', self.id)],
        }
