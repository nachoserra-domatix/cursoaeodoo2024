from odoo import models, fields, api

class SportPlayerPosition(models.Model):
    _name = 'sport.player.position'
    
    name = fields.Char(string='Name', required=True)
    description = fields.Html(string='Description', required=True)
    sport_id = fields.Many2one(comodel_name='sport.sport', string='Sport', required=True)