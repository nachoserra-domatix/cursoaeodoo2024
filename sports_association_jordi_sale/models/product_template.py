from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_sports_ticket = fields.Boolean(string='Is a Sports Ticket')
   