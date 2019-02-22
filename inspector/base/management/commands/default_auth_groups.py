import logging

from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel('INFO')

DEFAULTS = {
    'Checks - view':
        {'datacheck': ['view'],
         'checkrun': ['view'],
         'checkgroup': ['view']
         },
    'Checks - run': {
        'checkrun': ['add']
    }
}


class Command(BaseCommand):
    help = 'Creates default groups and permissions'

    def handle(self, *args, **kwargs):
        for group, models in DEFAULTS.items():
            new_group, created = Group.objects.get_or_create(name=group)
            for model, permissions in models.items():
                for permission in permissions:
                    codename = '{}_{}'.format(permission, model)

                    try:
                        model_add_perm = Permission.objects.get(codename=codename)
                    except Permission.DoesNotExist:
                        self.stderr.write("Permission not found: {}'.".format(codename))
                        continue

                    self.stdout.write("Adding permission '{}' to group '{}'".format(codename, group))
                    new_group.permissions.add(model_add_perm)

        self.stdout.write("Created default groups and permissions.")
