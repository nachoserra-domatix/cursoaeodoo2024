from odoo import fields, models

class SportLicense(models.Model):
    _name = 'sport.license'
    _description = 'Sport License'

    name = fields.Char(string='Name', required=True)
    partner_id = fields.Many2one('res.partner')
    reference = fields.Char(string='Reference')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')