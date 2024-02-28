from odoo import fields, models

class SportLicence(models.Model):
    _name = 'sport.license'
    _description = 'Sport License'
    
    name = fields.Char(string='Name', required=True)
    reference = fields.Char(string='reference')
    partner_id = fields.Many2one('res.partner', string='partner')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
