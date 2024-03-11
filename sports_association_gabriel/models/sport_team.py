from odoo import models, fields, api
from odoo.exceptions import UserError


class SportTeam(models.Model):
    _name = "sport.team"
    _description = "Sport Team"

    name = fields.Char(string='Name', required=True)
    player_ids = fields.One2many('sport.player', 'team_id', string='Players')
    sport_id = fields.Many2one('sport.sport', string='Sport')
    logo = fields.Binary(string="Logo", attachment=True)
    color = fields.Integer(string='Color', default=0)
    num_players = fields.Integer(string='Number of players', compute='_compute_num_players')

    @api.depends('player_ids')
    def _compute_num_players(self):
        for record in self:
            record.num_players = len(record.player_ids)

    def action_check_players_starter(self):
        for record in self.player_ids:
            record.check_starter()

    def action_uncheck_players_starter(self):
        for record in self.player_ids:
            record.uncheck_starter()

    def action_add_players(self):
        for record in self:
            players_no_team = self.env['sport.player'].search([('team_id', '=', False),('age', '<', 30)])
            if players_no_team:
                # record.write({'player_ids': [(6, 0, players_no_team.ids)]})
                record.player_ids = [(6, 0, players_no_team.ids)]
            else:
                raise UserError("There are no players without an assigned team and under 30 years of age")
            
    def action_view_players(self):
        return {
            'name': 'Players',
            'type': 'ir.actions.act_window',
            'res_model': 'sport.player',
            'view_mode': 'tree,form',
            'domain': [('team_id', '=', self.id)]
        }

