
from odoo.tests import common
from odoo import fields, models, Command
from odoo.exceptions import UserError

class TestSportIssue(common.TransactionCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.user = self.env.ref('base.user_admin')
        self.issue = self.env["sport.issue"].create({"name": "Issue 1", "state": "open"})
        self.tag = self.env["sport.issue.tag"].create({"name": "Tag Test"})

    def test_compute_assigned(self):
        self.issue.user_id = False
        self.assertFalse(self.issue.assigned)
        self.issue.user_id = self.user
        self.assertTrue(self.issue.assigned)

    def test_inverse_assigned(self):
        self.issue.assigned = False
        self.assertFalse(self.issue.user_id)
        self.issue.assigned = True
        self.assertEqual(self.issue.user_id, self.env.user)

    def test_action_draft(self):
        self.issue.action_draft()
        self.assertEqual(self.issue.state, "draft")

    def test_action_done(self):
        self.issue.action_done()
        self.assertEqual(self.issue.state, "done")
        self.issue.date = False
        with self.assertRaises(UserError):
            self.issue.action_done()

    def test_action_tags(self):
        self.issue.action_tags()
        self.assertIn(self.env["sport.issue.tag"].search([("name", "=", "Issue 1")]).id, self.issue.tag_ids.ids)
        self.issue.name = "Tag Test"
        self.issue.action_tags()
        self.assertIn(self.tag.id, self.issue.tag_ids.ids)
