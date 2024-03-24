from odoo import fields,api,models

class SportCreateMatch(models.TransientModel):
    _name = 'sport.create.match'
    _description = 'Create match'

    league_id = fields.Many2one('sport.league', string='League')
    sport_id = fields.Many2one('sport.sport', string='Sport', related='league_id.sport_id')
    team_ids = fields.Many2many('sport.team', string='Teams')
    date = fields.Datetime('Date')
    allowed_team_ids = fields.Many2many('sport.team', relation='sport_match_team_rel', string='Allowed Teams', compute='_compute_allowed_team_ids', store=True)

    @api.depends('league_id')
    def _compute_allowed_team_ids(self):
        for record in self:
            record.allowed_team_ids = self.league_id.sport_league_ids.team_id.ids
    
    def create_match(self):
        vals = {
            'league_id': self.league_id.id,
            'sport_id': self.sport_id.id,
            'date': self.date,
            'match_line_ids': [(0, 0, {'team_id': team.id}) for team in self.team_ids]
            }
        match = self.env['sport.match'].create(vals)
        return {
            'name': 'Match',
            'view_mode': 'form',
            'res_model': 'sport.match',
            'res_id': match.id,
            'type': 'ir.actions.act_window',
            'target': 'current',}
            