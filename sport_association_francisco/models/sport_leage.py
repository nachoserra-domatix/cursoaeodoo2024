from odoo import models, fields, api, Command

class SportLeage(models.Model):

    _name = 'sport.leage'
    _description = 'Sport Leage'

    name = fields.Char(string="Name")
    sport_id = fields.Many2one('sport.sport', string='Sport')
    leage_line_ids = fields.One2many('sport.leage.line', 'leage_id', string='Leage Line')
    date_start = fields.Date('date_start')
    date_end = fields.Date('date_end')

    def update_leage_points(self):
        for rec in self:
            rec.leage_line_ids.unlink()
            useful_matches = self.env['sport.match'].search([('match_date', '>=', rec.date_start), ('match_date', '<=',rec.date_end)])
            teams = useful_matches.match_line_ids.mapped('team_id')
            for team in teams:
                total_points = sum(useful_matches.search([('winner_team_id','=',team.id),('match_date', '>=', rec.date_start), ('match_date', '<=',rec.date_end)]).mapped('up_score'))
                rec.write({
                    'leage_line_ids': [Command.create({'team_id': team.id, 'score':total_points})]
                })
                
