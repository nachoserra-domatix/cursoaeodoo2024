from odoo import models, fields



class SportSport(models.Model):
    _name = 'sport.sport'
    _description = 'Sport'

    name = fields.Char(string='Name', required=True, translate=True)
    description = fields.Text(string='Description', translate=True)
    image = fields.Image(string='image')
    team_ids = fields.One2many(comodel_name='sport.team', inverse_name='sport_id', string='Teams')
    
    
    
    
