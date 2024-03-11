from odoo import models, fields, api

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'

    name = fields.Char(string='Name', required=True)
    #age = fields.Integer(string='Age')
    position = fields.Char(string='Position')
    team_id = fields.Many2one('sport.team', string='Team')
    starter = fields.Boolean(string='Starter', default=True)

    sport_name = fields.Char('Sport', related='team_id.sport_id.name', store=True)

    birthdate = fields.Date(string='Birthdate')
    age = fields.Integer(string='Age', compute='_compute_age')

    def action_check_starter(self):
        for record in self:
            record.starter = True

    def action_uncheck_starter(self):
        for record in self:
            record.starter = False

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                record.age = ( fields.Date.today() - record.birthdate ).days / 365
            else:
                record.age = 0