from odoo import models, fields

class SportTag(models.Model):

    _name = 'sport.tag'
    _description = 'Sport Tag'

    name = fields.Char(string="Name")
    issue_ids = fields.Many2many('sport.issue', string='isue')
