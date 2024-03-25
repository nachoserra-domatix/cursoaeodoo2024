from odoo import models, fields


class SportLicense(models.Model):
    _name = "sport.license"
    _description= "Sport License"

    name = fields.Char(string="Name", required=True)
    partner_id = fields.Many2one("res.partner")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
