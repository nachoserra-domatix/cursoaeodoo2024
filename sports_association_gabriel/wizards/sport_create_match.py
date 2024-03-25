from odoo import fields, models, api

class SportCreateMatch(models.TransientModel):
    _name = 'sport.create.match'
    _description = 'Create Match'

    league_id = fields.Many2one('sport.league', string='League')
    sport_id = fields.Many2one('sport.sport', string='Sport', related='league_id.sport_id')
    team_ids = fields.Many2many('sport.team', string='Teams')
    date = fields.Datetime('Date')

    def create_match(self):
        vals = {
            'league_id': self.league_id.id,
            'sport_id': self.sport_id.id,
            'match_date': self.date,
            'match_line_ids': [(0, 0, {'team_id': team.id}) for team in self.team_ids]
        }
        match = self.env['sport.match'].create(vals)

        # msg_body = f'El partido pertenece a la liga {match.league_id.name}'
        # match.message_post(body= msg_body)
        match.message_post_with_source('mail.message_origin_link', 
                                       render_values={'self': match, 'origin': self.league_id}, 
                                       subtype_xmlid='mail.mt_note')

        return {
            'name': 'Match',
            'view_mode': 'form',
            'res_model': 'sport.match',
            'res_id': match.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

