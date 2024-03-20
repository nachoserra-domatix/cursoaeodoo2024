from odoo import models, fields, api

class SportPlayer(models.Model):
    _name = 'sport.player'
    _description = 'Sport Player'
    _inherits = {'res.partner': 'partner_id'}

    #name = fields.Char(string='Name', required=True)
    name = fields.Char(related='partner_id.name', string='Name', inherited=True, readonly=False)

    partner_id = fields.Many2one('res.partner', string='Partner', required=True, ondelete='cascade')

    #age = fields.Integer(string='Age')
    position = fields.Char(string='Position', copy=False)
    team_id = fields.Many2one('sport.team', string='Team')
    starter = fields.Boolean(string='Starter', default=True, copy=False)

    sport_name = fields.Char('Sport', related='team_id.sport_id.name', store=True)

    birthdate = fields.Date(string='Birthdate', copy=False)
    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    # Controla archivado desde acciones
    active = fields.Boolean(string='Active', default=True)

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