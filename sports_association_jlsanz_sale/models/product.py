from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_ticket = fields.Boolean('is_ticket')