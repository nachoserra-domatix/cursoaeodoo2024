from odoo.tests import common
from odoo.exceptions import UserError

class TestSportIssue(common.TransactionCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.user = self.env.ref('base.user_admin')
        self.issue_1 = self.env['sport.issue'].create({'name': 'Issue 1 - Hombro', 'state': 'open'})
        self.issue_2 = self.env['sport.issue'].create({'name': 'Issue 2 - Pie', 'state': 'open'})
        self.issue_tag = self.env['sport.issue.tag'].create({'name': 'Issue 1 - Hombro'})

    def test_compute_assigned(self):
        self.issue_1.user_id = False
        self.assertFalse(self.issue_1.assigned)
        self.issue_1.user_id = self.user
        self.assertTrue(self.issue_1.assigned)

    def test_inverse_assigned(self):
        self.issue_1.assigned = False
        self.assertFalse(self.issue_1.user_id)
        self.issue_1.assigned = True
        self.assertEqual(self.issue_1.user_id, self.env.user)

    def test_action_draft(self):
        self.issue_1.action_draft()
        self.assertEqual(self.issue_1.state, 'draft')

    def test_action_done(self):
        self.issue_1.action_done()
        self.assertEqual(self.issue_1.state, 'done')
        self.issue_1.date = False
        with self.assertRaises(UserError):
            self.issue_1.action_done()

    def test_action_add_tags(self):
        self.issue_1.action_add_tags()
        self.assertEqual(self.issue_1.tag_ids, self.issue_tag)
        self.issue_2.action_add_tags()
        self.assertIn(self.issue_2.name, self.issue_2.tag_ids.mapped('name'))

    