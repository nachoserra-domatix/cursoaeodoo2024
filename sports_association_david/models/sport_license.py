from odoo import _, api, fields, models

class SportLicense(models.Model):
    _name = 'sport.license'
    _description = 'Sport License'

    name = fields.Char(string="Name", required=True)
    reference = fields.Text(string="Reference")
    partner_id = fields.Many2one("res.partner", string="Partner")
    start_date = fields.Datetime(string="Start Date")
    end_date = fields.Datetime(string="Start Date")
    