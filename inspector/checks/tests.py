import unittest
from random import shuffle

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.test import Client
from django.urls import reverse

from .constants import CHECK_TYPES, RELATIONS
from .models import CheckGroup, Datacheck, CheckRun, EnvironmentStatus
from ..systems.tests import create_system, create_environment

RANDOMS = list(range(10000))
shuffle(RANDOMS)


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    user_no = RANDOMS.pop()
    defaults["username"] = "user-{}".format(user_no)
    defaults["email"] = "user-{}@tempurl.com".format(user_no)
    defaults.update(**kwargs)
    User = get_user_model()
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_checkgroup(**kwargs):
    defaults = {}
    defaults["name"] = "checkgroup-{}".format(RANDOMS.pop())
    defaults["description"] = "description"
    defaults.update(**kwargs)
    return CheckGroup.objects.create(**defaults)


def create_datacheck(**kwargs):
    defaults = {}
    defaults["code"] = "datacheck-{}".format(RANDOMS.pop())
    defaults["description"] = "description"
    defaults["weight"] = 1
    defaults["left_type"] = CHECK_TYPES.SQL_QUERY
    defaults["left_logic"] = "left_logic"
    defaults["relation"] = RELATIONS.eq
    defaults["right_type"] = CHECK_TYPES.SQL_QUERY
    defaults["right_logic"] = "right_logic"
    defaults["supports_warning"] = False
    defaults["warning_relation"] = None
    defaults["warning_type"] = None
    defaults["warning_logic"] = "warning_logic"
    defaults.update(**kwargs)
    if "group" not in defaults:
        defaults["group"] = create_checkgroup()
    if "left_system" not in defaults:
        defaults["left_system"] = create_system()
    if "right_system" not in defaults:
        defaults["right_system"] = create_system()
    return Datacheck.objects.create(**defaults)


def create_checkrun(**kwargs):
    defaults = {}
    defaults["status"] = "status"
    defaults["result"] = "result"
    defaults["left_value"] = "left_value"
    defaults["right_value"] = "right_value"
    defaults["warning_value"] = "warning_value"
    defaults["error_message"] = "error_message"
    defaults.update(**kwargs)
    if "datacheck" not in defaults:
        defaults["datacheck"] = create_datacheck()
    if "environment" not in defaults:
        defaults["environment"] = create_environment()
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return CheckRun.objects.create(**defaults)


def create_environmentstatus(**kwargs):
    defaults = {}
    defaults["status"] = "status"
    defaults["result"] = "result"
    defaults.update(**kwargs)
    if "datacheck" not in defaults:
        defaults["datacheck"] = create_datacheck()
    if "environment" not in defaults:
        defaults["environment"] = create_environment()
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return EnvironmentStatus.objects.create(**defaults)


class CheckGroupViewTest(unittest.TestCase):
    '''
    Tests for CheckGroup
    '''

    def setUp(self):
        self.client = Client()

    def test_list_checkgroup(self):
        url = reverse('checks_checkgroup_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_checkgroup(self):
        url = reverse('checks_checkgroup_create')
        data = {
            "name": "checkgroup-{}".format(RANDOMS.pop()),
            "description": "description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_update_checkgroup(self):
        checkgroup = create_checkgroup()
        data = {
            "name": "checkgroup-{}".format(RANDOMS.pop()),
            "description": "description",
        }
        url = reverse('checks_checkgroup_update', args=[checkgroup.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DatacheckViewTest(unittest.TestCase):
    '''
    Tests for Datacheck
    '''

    def setUp(self):
        self.client = Client()

    def test_list_datacheck(self):
        url = reverse('checks_datacheck_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_datacheck(self):
        url = reverse('checks_datacheck_create')
        data = {
            "code": "code",
            "description": "description",
            "weight": 1,
            "left_type": CHECK_TYPES.SQL_QUERY,
            "left_logic": "left_logic",
            "relation": RELATIONS.eq,
            "right_logic": "right_logic",
            "supports_warning": False,
            "warning_relation": None,
            "warning_type": None,
            "warning_logic": None,
            "group": create_checkgroup().pk,
            "left_system": create_system().pk,
            "right_system": create_system().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_detail_datacheck(self):
        datacheck = create_datacheck()
        url = reverse('checks_datacheck_detail', args=[datacheck.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_datacheck(self):
        datacheck = create_datacheck()
        data = {
            "code": "code",
            "description": "description",
            "weight": 1,
            "left_type": "left_type",
            "left_logic": "left_logic",
            "relation": RELATIONS.eq,
            "right_logic": "right_logic",
            "supports_warning": False,
            "warning_relation": None,
            "warning_type": None,
            "warning_logic": None,
            "group": create_checkgroup().pk,
            "left_system": create_system().pk,
            "right_system": create_system().pk,
        }
        url = reverse('checks_datacheck_update', args=[datacheck.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)


class CheckRunViewTest(unittest.TestCase):
    '''
    Tests for CheckRun
    '''

    def setUp(self):
        self.client = Client()

    def test_list_checkrun(self):
        url = reverse('checks_checkrun_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_checkrun(self):
        url = reverse('checks_checkrun_create')
        data = {
            "start_time": "start_time",
            "end_time": "end_time",
            "status": "status",
            "result": "result",
            "left_value": "left_value",
            "right_value": "right_value",
            "warning_value": "warning_value",
            "error_message": "error_message",
            "datacheck": create_datacheck().pk,
            "environment": create_environment().pk,
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_checkrun(self):
        checkrun = create_checkrun()
        url = reverse('checks_checkrun_detail', args=[checkrun.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_checkrun(self):
        checkrun = create_checkrun()
        data = {
            "status": "status",
            "result": "result",
            "left_value": "left_value",
            "right_value": "right_value",
            "warning_value": "warning_value",
            "error_message": "error_message",
            "datacheck": create_datacheck().pk,
            "environment": create_environment().pk,
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('checks_checkrun_update', args=[checkrun.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class EnvironmentStatusViewTest(unittest.TestCase):
    '''
    Tests for EnvironmentStatus
    '''

    def setUp(self):
        self.client = Client()

    def test_list_environmentstatus(self):
        url = reverse('checks_environmentstatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_environmentstatus(self):
        url = reverse('checks_environmentstatus_create')
        data = {
            "status": "status",
            "result": "result",
            "datacheck": create_datacheck().pk,
            "environment": create_environment().pk,
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_environmentstatus(self):
        environmentstatus = create_environmentstatus()
        url = reverse('checks_environmentstatus_detail', args=[environmentstatus.pk, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_environmentstatus(self):
        environmentstatus = create_environmentstatus()
        data = {
            "status": "status",
            "result": "result",
            "datacheck": create_datacheck().pk,
            "environment": create_environment().pk,
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('checks_environmentstatus_update', args=[environmentstatus.pk, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
