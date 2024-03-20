from odoo import models, fields

class SportTag(models.Model):

    _name = 'sport.tag'
    _description = 'Sport Tag'

    name = fields.Char(string="Name")
    issue_ids = fields.Many2many('sport.issue', string='isue')
    color = fields.Integer(string='Color', default=0)

    def unlink_if_not_used(self):
        tag_ids = self.env['sport.tag'].search([])
        for tag in tag_ids:
            issues = self.env['sport.issue'].search([('tag_ids', 'in', tag.id)])
            if not issues:
                tag.unlink()
