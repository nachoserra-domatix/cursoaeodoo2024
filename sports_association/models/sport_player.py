from odoo import models, fields


class Sportplayer(models.Model):
    _name = "sport.player"
    _description = "Sport Player"

    name = fields.Char(
        string='Name',
    )
    
    age = fields.Integer(
        string='Age',
    )

    position = fields.Char(
        string='Position',
    )
    
    team_id = fields.Many2one(
        string='Team',
        comodel_name='sport.team',
    )

    starter = fields.Boolean(
        string='Starter',
    )

    def action_check_starter(self):
        for record in self:
            record.starter = True

    def action_uncheck_starter(self):
        for record in self:
            record.starter = False
