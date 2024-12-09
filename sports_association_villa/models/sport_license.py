from odoo import fields, models, api
from datetime import timedelta

class SportLicense(models.Model):
    _name = 'sport.license'
    _description = 'Sport License'

    name = fields.Char('Name', required=True)
    partner_id = fields.Many2one('res.partner')
    start_date = fields.Date(string ='Start Date')
    end_date = fields.Date(string='End Date', compute='_compute_end_date')

    @api.depends('start_date')
    def _compute_end_date(self):
        for record in self:
            if record.start_date:
                start_date = fields.Datetime.from_string(record.start_date)
                end_date = start_date + timedelta(days=25)
                record.end_date = fields.Date.to_string(end_date.date())
            else:
                record.end_date = False