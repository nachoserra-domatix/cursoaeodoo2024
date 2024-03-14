from odoo import fields, api, models
from datetime import datetime

class SportCreateMatch(models.TransientModel):
    _name = 'sport.create.match'
    _description = "Create Match"

    match_date = fields.Datetime('Match Date', default=lambda x: datetime.now())
    leage_id = fields.Many2one('sport.leage', string='Leage', default=lambda self:self.get_default_leage())
    sport_id = fields.Many2one('sport.sport', string='Sport', related="leage_id.sport_id")
    team_ids = fields.Many2many('sport.team', string='Teams')

    def get_default_leage(self):
        active_id = self.env.context.get('active_id')
        leage_id = self.env['sport.leage'].browse(active_id)
        return leage_id.id

    def create_match(self):
        self.ensure_one()
        match = self.env['sport.match'].create({
            'match_date':self.match_date,
            'sport_id': self.sport_id.id,
            'leage_id': self.leage_id.id,
            'match_line_ids': [(0,0,{'team_id':team.id}) for team in self.team_ids]
            })
        return {
            'name':'Match',
            'view_mode': 'form',
            'res_model':'sport.match',
            'res_id':match.id,
            'type':'ir.actions.act_window',
            'target':'current',
        }