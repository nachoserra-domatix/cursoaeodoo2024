from odoo import models, fields

class SportsIssue(models.Model):
    _name = 'sports.license'
    _description = 'Sports License'

    name = fields.Char(string='Name',required=True)
    reference = fields.Char(string='Reference')
    partner_id = fields.Many2one('res.partner')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

          