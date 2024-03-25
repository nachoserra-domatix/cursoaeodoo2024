from odoo import models, fields

class SportsCreateMatch(models.TransientModel):
    _name = 'sports.create.match'
    _description = 'Create Match'

    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    sport_id = fields.Many2one('sports.sport',string='Sport',related='league_id.sport_id')
    league_id = fields.Many2one('sports.league',string='League', default=lambda self: self.env.context.get('active_id'))
    team1_id = fields.Many2one('sports.team', string='Team 1')
    team2_id = fields.Many2one('sports.team', string='Team 2')

    def create_match(self):
        match = self.env['sports.match'].create({
            'date': self.date,
            'sport_id': self.sport_id.id,
            'league_id': self.league_id.id,
            'match_lines': [(0, 0, {'team_id': self.team1_id.id}), (0, 0, {'team_id': self.team2_id.id})],
        })  
        body = 'Match between %s and %s of %s' % (self.team1_id.name, self.team2_id.name,self.league_id.name)
        match.message_post(body=body)
        match.message_post_with_source('mail.message_origin_link', 
                                       render_values={'self': match, 'origin': self.league_id}, 
                                       subtype_xmlid='mail.mt_note')
        return {'name': 'Matches', 'type': 'ir.actions.act_window', 'res_model': 'sports.match', 'view_mode': 'form', 'target': 'current', 'res_id': match.id}
        