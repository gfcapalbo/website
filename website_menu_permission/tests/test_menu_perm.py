# Copyright 2017 Simone Orsi.
# Copyright 2019 Therp BV <https://therp.nl>.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
import odoo.tests.common as test_common


class TestMenuPerm(test_common.TransactionCase):

    def setUp(self):
        super(TestMenuPerm, self).setUp()
        self.group_portal = self.env.ref('base.group_portal')
        self.group_user = self.env.ref('base.group_user')
        self.group_public = self.env.ref('base.group_public')
        user_model = self.env['res.users'].with_context(**{
            'no_reset_password': True,
            'mail_create_nosubscribe': True})
        self.employee_user = user_model.create({
            'name': 'Employee user (test ref)',
            'login': 'testref_employee_user',
            'email': 'testref_employee_user@email.com',
            'groups_id': [(6, 0, [self.group_user.id])]})
        self.portal_user = user_model.create({
            'name': 'Portal user',
            'login': 'portaluser',
            'email': 'portaluser@example.com',
            'groups_id': [(6, 0, [self.group_portal.id])]})
        self.public_user = self.env.ref('base.public_user')
        self.menu_model = self.env['website.menu']
        self.menu_item = self.menu_model.create({'name': 'Foo'})

    def test_menu_for_all(self):
        self.menu_item.write({'group_ids': False})
        self.assertTrue(self._can_see(self.employee_user))
        self.assertTrue(self._can_see(self.public_user))
        self.assertTrue(self._can_see(self.portal_user))

    def test_menu_for_employee(self):
        self.menu_item.write({'group_ids': [(6, 0, [self.group_user.id])]})
        self.assertTrue(self._can_see(self.employee_user))
        self.assertFalse(self._can_see(self.public_user))
        self.assertFalse(self._can_see(self.portal_user))

    def test_menu_for_external(self):
        self.menu_item.write({'group_ids': [(6, 0, [self.group_portal.id])]})
        self.assertFalse(self._can_see(self.employee_user))
        self.assertFalse(self._can_see(self.public_user))
        self.assertTrue(self._can_see(self.portal_user))

    def test_menu_for_logged_in_users(self):
        self.menu_item.write(
            {'group_ids': [(6, 0, [
                self.group_portal.id, self.group_user.id])]})
        self.assertTrue(self._can_see(self.employee_user))
        self.assertFalse(self._can_see(self.public_user))
        self.assertTrue(self._can_see(self.portal_user))

    def test_menu_for_not_logged_in_users(self):
        self.menu_item.write({'group_ids': [(6, 0, [self.group_public.id])]})
        self.assertFalse(self._can_see(self.employee_user))
        self.assertTrue(self._can_see(self.public_user))
        self.assertFalse(self._can_see(self.portal_user))

    def test_menu_for_all_explicit(self):
        self.menu_item.write(
            {'group_ids': [(6, 0, [
                self.group_portal.id,
                self.group_user.id,
                self.group_public.id])]})
        self.assertTrue(self._can_see(self.employee_user))
        self.assertTrue(self._can_see(self.public_user))
        self.assertTrue(self._can_see(self.portal_user))

    def _can_see(self, user):
        """Check wether user can see the test menu."""
        menu_model_sudo = self.menu_model.sudo(user.id)
        can_see = self.menu_item in menu_model_sudo.search([])
        return can_see
