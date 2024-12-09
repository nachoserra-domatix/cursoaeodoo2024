# Copyright NuoBiT Solutions - Kilian Niubo <kniubo@nuobit.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)
from odoo import fields, models


class SportIssueTag(models.Model):
    _name = "sport.issue.tag"
    _description = "Sport Issue Tag"

    name = fields.Char(
        required=True,
    )
