from odoo import models, fields, api


class SportTicket(models.Model):
    _name = "sport.ticket"
    _description = "Sport Ticket"

    name = fields.Char(string='Name')
    partner_id = fields.Many2one('res.partner', string='Partner')
    match_id = fields.Many2one('sport.match', string='Match')

    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('sport.ticket')
        res = super().create(vals)        
        return res

    