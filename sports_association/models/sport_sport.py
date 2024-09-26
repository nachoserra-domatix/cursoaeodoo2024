from odoo import fields, models, _

class SportSport(models.Model):
    _name="sport.sport"
    
    name = fields.Char(string=_('Name'), required=True)
    description = fields.Html(_('Description'), required=True)
    
    
    