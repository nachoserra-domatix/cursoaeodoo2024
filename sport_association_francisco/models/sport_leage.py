from odoo import models, fields, api, Command, _
from odoo.exceptions import ValidationError

class SportLeage(models.Model):

    _name = 'sport.leage'
    _description = 'Sport Leage'

    name = fields.Char(string="Name")
    sport_id = fields.Many2one('sport.sport', string='Sport')
    leage_line_ids = fields.One2many('sport.leage.line', 'leage_id', string='Leage Line')
    match_ids = fields.One2many('sport.match', 'leage_id', string='Matches')
    date_start = fields.Date('date_start')
    date_end = fields.Date('date_end')
    match_count = fields.Integer('Match count', compute="compute_match_count")

    def compute_match_count(self):
        for rec in self:
            rec.match_count = len(rec.match_ids)


    @api.constrains('date_start', 'date_end')
    def verify_cost(self):
        for rec in self:
            if rec.date_start > rec.date_end:
                raise ValidationError(_("The start date must be before end date."))

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

    def update_all_leage_points(self):
        leages = self.env['sport.leage'].search([])
        leages.update_leage_points()

    def action_view_matches(self):
        return{
            "name": "Matches",
            "type": 'ir.actions.act_window',
            "view_mode": 'tree,form',
            "res_model": "sport.match",
            "domain": [('leage_id', '=', self.id)],
        }
                