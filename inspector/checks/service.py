from django.contrib.auth.models import User

from .constants import STATUSES
from .models import Datacheck, Environment, CheckRun


class CheckRunService:

    @staticmethod
    def create_check_run(
        check_code: str,
        environment: str,
        user: User
    ) -> int:
        datacheck = Datacheck.objects.get(code=check_code)
        environment = Environment.objects.get(name=environment)

        check_run = CheckRun(
            datacheck=datacheck,
            environment=environment,
            status=STATUSES.NEW,
            user=user
        )
        check_run.save()

        return check_run.pk
