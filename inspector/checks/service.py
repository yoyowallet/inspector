from django.contrib.auth.models import User

from inspector.taskapp.tasks import execute_check
from .constants import STATUSES
from .models import Datacheck, Environment, CheckRun, CheckGroup


class CheckRunService:

    @staticmethod
    def create_check_run_api(
        check_code: str,
        environment: str,
        user: User
    ) -> int:
        datacheck = Datacheck.objects.get(code=check_code)
        environment = Environment.objects.get(name=environment)

        return CheckRunService._create_and_execute_checkrun(
            datacheck,
            environment,
            user)

    @staticmethod
    def run_check_group(
        checkgroup_id: int,
        environment: Environment,
        user: User,
    ):
        checkgroup = CheckGroup.objects.get(id=checkgroup_id)

        for chk in Datacheck.objects.filter(group=checkgroup):
            CheckRunService._create_and_execute_checkrun(
                chk,
                environment,
                user)

    @staticmethod
    def run_check_group_api(
        checkgroup_name: str,
        environment: str,
        user: User,
    ):
        checkgroup = CheckGroup.objects.get(name=checkgroup_name)
        environment = Environment.objects.get(name=environment)

        for chk in Datacheck.objects.filter(group=checkgroup):
            CheckRunService._create_and_execute_checkrun(
                chk,
                environment,
                user)

    @staticmethod
    def _create_and_execute_checkrun(check: Datacheck, environment: Environment, user: User) -> int:
        check_run = CheckRun(
            datacheck=check,
            environment=environment,
            status=STATUSES.NEW,
            user=user
        )
        check_run.save()
        execute_check(check_run.id)

        return check_run.id
