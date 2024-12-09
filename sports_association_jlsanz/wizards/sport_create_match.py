from odoo import fields, api, models

class SportCreateMatch(models.TransientModel):
    _name = 'sport.create.match'
    _description = 'Generate new match'

    sport_id = fields.Many2one('sport.sport', string='Sport', related='league_id.sport_id' )
    date_time = fields.Datetime(string='Date', default=fields.Date().today())
    matchpoints = fields.Integer(string='Points', default='3')
    league_id = fields.Many2one('sport.league', string='League', default=lambda self: self.env.context.get('active_id'))
    team_ids = fields.Many2many('sport.team')

    def create_match(self):
        vals = {
            'sport_id': self.sport_id.id,
            'date_time': self.date_time,
            'matchpoints': self.matchpoints,
            'league_id': self.league_id.id,
            'match_result_ids': [(0, 0, {'team_id': team.id}) for team in self.team_ids]
            }
        match = self.env['sport.match'].create(vals)
        # Para el chatter
        match.message_post_with_source('mail.message_origin_link',
                                        render_values={'self': match, 'origin': self.league_id},
                                        subtype_xmlid='mail.mt_note')
        # Devolver el formulario del registro creado
        return {
            'name': 'Match',
            'view_mode': 'form',
            'res_model': 'sport.match',
            'res_id': match.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

