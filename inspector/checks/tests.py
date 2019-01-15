import unittest
from django.urls import reverse
from django.test import Client
from .models import CheckGroup, Datacheck, CheckRun, EnvironmentStatus
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
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
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    return CheckGroup.objects.create(**defaults)


def create_datacheck(**kwargs):
    defaults = {}
    defaults["code"] = "code"
    defaults["description"] = "description"
    defaults["weight"] = "weight"
    defaults["left_type"] = "left_type"
    defaults["left_logic"] = "left_logic"
    defaults["relation"] = "relation"
    defaults["right_logic"] = "right_logic"
    defaults["supports_warning"] = "supports_warning"
    defaults["warning_relation"] = "warning_relation"
    defaults["warning_type"] = "warning_type"
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
    defaults["start_time"] = "start_time"
    defaults["end_time"] = "end_time"
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
        defaults["user"] = create_settings_auth_user_model()
    return CheckRun.objects.create(**defaults)


def create_environmentstatus(**kwargs):
    defaults = {}
    defaults["last_start_time"] = "last_start_time"
    defaults["last_end_time"] = "last_end_time"
    defaults["status"] = "status"
    defaults["result"] = "result"
    defaults.update(**kwargs)
    if "datacheck" not in defaults:
        defaults["datacheck"] = create_datacheck()
    if "environment" not in defaults:
        defaults["environment"] = create_environment()
    if "user" not in defaults:
        defaults["user"] = create_settings_auth_user_model()
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
            "name": "name",
            "description": "description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_checkgroup(self):
        checkgroup = create_checkgroup()
        url = reverse('checks_checkgroup_detail', args=[checkgroup.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_checkgroup(self):
        checkgroup = create_checkgroup()
        data = {
            "name": "name",
            "description": "description",
        }
        url = reverse('checks_checkgroup_update', args=[checkgroup.pk,])
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
            "weight": "weight",
            "left_type": "left_type",
            "left_logic": "left_logic",
            "relation": "relation",
            "right_logic": "right_logic",
            "supports_warning": "supports_warning",
            "warning_relation": "warning_relation",
            "warning_type": "warning_type",
            "warning_logic": "warning_logic",
            "group": create_checkgroup().pk,
            "left_system": create_system().pk,
            "right_system": create_system().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_datacheck(self):
        datacheck = create_datacheck()
        url = reverse('checks_datacheck_detail', args=[datacheck.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_datacheck(self):
        datacheck = create_datacheck()
        data = {
            "code": "code",
            "description": "description",
            "weight": "weight",
            "left_type": "left_type",
            "left_logic": "left_logic",
            "relation": "relation",
            "right_logic": "right_logic",
            "supports_warning": "supports_warning",
            "warning_relation": "warning_relation",
            "warning_type": "warning_type",
            "warning_logic": "warning_logic",
            "group": create_checkgroup().pk,
            "left_system": create_system().pk,
            "right_system": create_system().pk,
        }
        url = reverse('checks_datacheck_update', args=[datacheck.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


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
            "user": create_settings_auth_user_model().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_checkrun(self):
        checkrun = create_checkrun()
        url = reverse('checks_checkrun_detail', args=[checkrun.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_checkrun(self):
        checkrun = create_checkrun()
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
            "user": create_settings_auth_user_model().pk,
        }
        url = reverse('checks_checkrun_update', args=[checkrun.pk,])
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
            "last_start_time": "last_start_time",
            "last_end_time": "last_end_time",
            "status": "status",
            "result": "result",
            "datacheck": create_datacheck().pk,
            "environment": create_environment().pk,
            "user": create_settings_auth_user_model().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_environmentstatus(self):
        environmentstatus = create_environmentstatus()
        url = reverse('checks_environmentstatus_detail', args=[environmentstatus.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_environmentstatus(self):
        environmentstatus = create_environmentstatus()
        data = {
            "last_start_time": "last_start_time",
            "last_end_time": "last_end_time",
            "status": "status",
            "result": "result",
            "datacheck": create_datacheck().pk,
            "environment": create_environment().pk,
            "user": create_settings_auth_user_model().pk,
        }
        url = reverse('checks_environmentstatus_update', args=[environmentstatus.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
