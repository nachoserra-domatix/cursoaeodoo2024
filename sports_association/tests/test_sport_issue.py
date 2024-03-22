from odoo import _, api, fields, models
from odoo.tests.common import  TransactionCase
from odoo.exceptions import ValidationError, UserError

class TestSportIssue(TransactionCase):
    
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.user = self.env.ref('base.user_admin')
        self.issue = self.env['sport.issue'].create({'name': 'Issue 1', 'state': 'open'})
        self.issue2 = self.env['sport.issue'].create({'name': 'Issue 2', 'state': 'open'})
        self.tag = self.env['sport.issue.tag'].create({'name': 'Issue 1'})

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
        self.assertEqual(self.issue.state, 'draft')

    def test_action_done(self):
        self.issue.action_done()
        self.assertEqual(self.issue.state, 'done')
        self.issue.date = False
        with self.assertRaise(UserError):
            self.issue.action_done()

    def test_action_add_tags(self):
        self.issue.action_add_tag()
        self.assertEqual(self.issue.tag_ids, self.tag)
        self.issue2.action_add_tag()
        self.assertIn(self.issue2.name, self.issue2.tag_ids.mapped('name'))