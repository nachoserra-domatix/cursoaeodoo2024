from odoo.tests import common
from odoo import fields, models
from odoo.exceptions import UserError

class TestSportIssue(common.TransactionCase):

    @classmethod
    def setUpClass(self):
        super(TestSportIssue, self).setUpClass()
        self.user = self.env.ref('base.user_admin')
        self.issue = self.env['sport.issue'].create({
            'name': 'Issue 1',
            'description': 'Description 1',
            'state': 'open',
        })
        self.issue2 = self.env['sport.issue'].create({
            'name': 'Issue 2',
            'description': 'Description 2',
            'state': 'open',
        })        
        self.tag_same_name = self.env['sport.issue.tag'].create({
            'name': 'Issue 1',
        })
        


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
        with self.assertRaises(models.UserError):
            self.issue.action_done()

    def test_action_find_tags(self):
        self.issue.action_find_tags()
        self.assertEqual(self.issue.tags_ids, self.tag_same_name)
        self.issue2.action_find_tags()
        self.assertIn(self.issue2.name, self.issue2.tags_ids.mapped('name'))