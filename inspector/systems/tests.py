import unittest
from django.urls import reverse
from django.test import Client
from .models import System, Environment, Instance
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


def create_system(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["application"] = "application"
    defaults.update(**kwargs)
    return System.objects.create(**defaults)


def create_environment(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return Environment.objects.create(**defaults)


def create_instance(**kwargs):
    defaults = {}
    defaults["host"] = "host"
    defaults["port"] = "port"
    defaults["database_or_schema"] = "database_or_schema"
    defaults["login"] = "login"
    defaults["password"] = "password"
    defaults.update(**kwargs)
    if "system" not in defaults:
        defaults["system"] = create_system()
    if "environment" not in defaults:
        defaults["environment"] = create_environment()
    return Instance.objects.create(**defaults)


class SystemViewTest(unittest.TestCase):
    '''
    Tests for System
    '''
    def setUp(self):
        self.client = Client()

    def test_list_system(self):
        url = reverse('systems_system_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_system(self):
        url = reverse('systems_system_create')
        data = {
            "name": "name",
            "application": "application",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_system(self):
        system = create_system()
        url = reverse('systems_system_detail', args=[system.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_system(self):
        system = create_system()
        data = {
            "name": "name",
            "application": "application",
        }
        url = reverse('systems_system_update', args=[system.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class EnvironmentViewTest(unittest.TestCase):
    '''
    Tests for Environment
    '''
    def setUp(self):
        self.client = Client()

    def test_list_environment(self):
        url = reverse('systems_environment_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_environment(self):
        url = reverse('systems_environment_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_environment(self):
        environment = create_environment()
        url = reverse('systems_environment_detail', args=[environment.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_environment(self):
        environment = create_environment()
        data = {
            "name": "name",
        }
        url = reverse('systems_environment_update', args=[environment.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InstanceViewTest(unittest.TestCase):
    '''
    Tests for Instance
    '''
    def setUp(self):
        self.client = Client()

    def test_list_instance(self):
        url = reverse('systems_instance_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_instance(self):
        url = reverse('systems_instance_create')
        data = {
            "host": "host",
            "port": "port",
            "database_or_schema": "database_or_schema",
            "login": "login",
            "password": "password",
            "system": create_system().pk,
            "environment": create_environment().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_instance(self):
        instance = create_instance()
        url = reverse('systems_instance_detail', args=[instance.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_instance(self):
        instance = create_instance()
        data = {
            "host": "host",
            "port": "port",
            "database_or_schema": "database_or_schema",
            "login": "login",
            "password": "password",
            "system": create_system().pk,
            "environment": create_environment().pk,
        }
        url = reverse('systems_instance_update', args=[instance.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
