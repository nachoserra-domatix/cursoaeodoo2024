from odoo import fields, models


class SportIssueTag(models.Model):
    _name = "sport.issue.tag"
    _description = "Sport Issue Tag"

    name = fields.Char(string="name", translate=True)
    color = fields.Integer(string="Color", default=0)
    issue_ids = fields.Many2many(
        string="Issues",
        comodel_name="sport.issue",
        relation="sport_issue_tag_rel",
        column1="tag_ids",
        column2="issue_ids",
    )

    def _cron_remove_unused_tags(self):
        unused_tags = self.search([("issue_ids", "=", False)])
        unused_tags.unlink()
