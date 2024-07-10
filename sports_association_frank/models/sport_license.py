from odoo import models, fields

class SportLicense(models.Model):
    _name = "sport.license"
    _description = "Sport License"

    name = fields.Char(string="Title", required=True)
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
    )
    sequence = fields.Char(string="Sequence 1")
    sequence_id = fields.Many2one(
        comodel_name="ir.sequence",
        string="Sequence",
    )
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")


