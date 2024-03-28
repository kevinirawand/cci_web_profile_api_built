from django.test import TestCase

from users.models_roles import Role
from users.models_divisions import Division
from users.models_users import User


def _create_user(nim, role, division, email, phone):
    User.objects.create(nim=nim, role_id=role, division_id=division, email=email, phone_number=phone)


def _create_role(id, role_name):
    Role.objects.create(id=id, name=role_name)


def _create_division(id, division_name, division_description):
    Division.objects.create(id=id, name=division_name, description=division_description)


class UserTestCase(TestCase):

    def setUp(self):
        _create_role("SPR", 'Superadmin')
        _create_role("PGR", 'Admin')
        _create_role("USR", 'User')

        superuser_role = Role.objects.get(id='SPR')
        admin_role = Role.objects.get(id='PGR')
        user_role = Role.objects.get(id='USR')

        _create_division("WBD", 'Web Developer', 'Web Developer division')
        _create_division('MBL', 'Mobile Developer division', "Mobile")
        _create_division('DSG', 'UI/UX Designer division', "UI")

        web_dev_division = Division.objects.get(id='WBD')
        mobile_dev_division = Division.objects.get(id='MBL')
        ui_ux_division = Division.objects.get(id='DSG')

        _create_user('1234567890', superuser_role, web_dev_division, 'test1@mail.com', "0896")
        _create_user('1234567891', admin_role, mobile_dev_division, 'test2@mail.com', "0893")
        _create_user('1234567892', user_role, ui_ux_division, 'test3@mail.com', "08977")

    def test_user_role(self):
        test_user = User.objects.get(nim='1234567890')
        self.assertEqual(test_user.role_id.name, 'Superadmin')

    def test_user_division(self):
        test_user = User.objects.get(nim='1234567890')
        self.assertEqual(test_user.division_id.id, 'WBD')

    def test_user_superuser(self):
        test_user = User.objects.get(nim='1234567890')
        self.assertEqual(test_user.is_superuser(), True)
