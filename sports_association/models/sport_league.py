from odoo import models, fields

class SportLeague(models.Model):
    _name = "sport.league"
    _description = "Sport League"

    
    name = fields.Char(
        string='Name',
    )
    
    sport_id = fields.Many2one(
        string='Sport',
        comodel_name='sport.sport',
    )
    
    description = fields.Text(
        string='Description',
    )
    
    image = fields.Binary(
        string='Image',
    )
    
    date_start = fields.Date(
        string='Start Date',
        default=fields.Date.context_today,
    )
    date_end = fields.Date(
        string='End Date',
        default=fields.Date.context_today,
    )

    league_line_ids = fields.One2many('sport.league.line', 'league_id', string='League Classifications')

    def action_compute_classification(self):
        for record in self:
            for line in record.league_line_ids:
                games_won = self.env["sport.game"].search([("team_winner_id", "=", line.team_id.id),('league_id','=',self.id)])
                line.points = sum(game["points"] for game in games_won)



