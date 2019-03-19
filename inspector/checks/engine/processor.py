import logging
from datetime import datetime as dt
from importlib import import_module

import pytz

from .exceptions import CheckExecutorException, InstanceNotFound
from .executors import CheckExecutor, CONFIG
from .executors.python_executor import PythonExecutor
from ..constants import STATUSES, RELATIONS, RESULTS
from ..models import CheckRun, Datacheck, EnvironmentStatus
from ...systems.models import Instance, System

logger = logging.getLogger(__name__)


class CheckProcessor:

    def __init__(self, checkrun_id: int):
        self.checkrun: CheckRun = CheckRun.objects.get(id=checkrun_id)
        self.datacheck: Datacheck = self.checkrun.datacheck
        self.left_executor: CheckExecutor = None
        self.right_executor: CheckExecutor = None

    def prepare_check(self) -> bool:

        errors = []

        try:
            self.left_executor = self.get_executor(
                system=self.datacheck.left_system,
                check_type=self.datacheck.left_type
            )
        except CheckExecutorException as exc:
            errors.append(repr(exc))

        try:
            self.right_executor = self.get_executor(
                system=self.datacheck.right_system,
                check_type=self.datacheck.right_type
            )
        except CheckExecutorException as exc:
            errors.append(repr(exc))

        if errors:
            self.checkrun.error_message = '\n'.join(errors)
            self.checkrun.status = STATUSES.ERROR
            status = False
        else:
            logger.info('Starting check -  %s', self.datacheck.code)
            self.checkrun.status = STATUSES.RUNNING
            self.checkrun.start_time = dt.now(pytz.utc)
            status = True

        self.checkrun.save()

        return status

    def get_executor(self,
                     system: System,
                     check_type) -> CheckExecutor:
        if system is None:
            return PythonExecutor(instance=None, check_type=self.datacheck.right_type)

        instance = self.get_instance(system=system)
        executor = self.get_executor_for_instance(instance=instance, check_type=check_type)
        try:
            executor.test_connection()
        except Exception as exc:
            raise CheckExecutorException(exc)

        return executor

    def get_instance(self, system: System) -> Instance:
        try:
            instance = Instance.objects.get(environment=self.checkrun.environment, system=system)
        except Instance.DoesNotExist:
            raise InstanceNotFound(system, self.checkrun.environment)

        return instance

    @staticmethod
    def get_executor_for_instance(instance: Instance, check_type) -> CheckExecutor:

        config = CONFIG[instance.system.application]
        executor_module = import_module(f'inspector.checks.engine.executors.{config["executor.module"]}')
        executor_class = getattr(executor_module, config['executor.class'])
        return executor_class(instance=instance, check_type=check_type, **config['params'])

    def execute_checks(self):

        status = True
        result = None
        errors = list()

        try:
            left_value = self.left_executor.execute(self.datacheck.left_logic)
            self.checkrun.left_value = str(left_value)
        except Exception as exc:
            errors.append(str(exc))
            status = False

        try:
            right_value = self.right_executor.execute(self.datacheck.right_logic)
            self.checkrun.right_value = str(right_value)
        except Exception as exc:
            errors.append(str(exc))
            status = False

        if status:
            comparator = CheckComparator(self.datacheck)
            result = comparator.compare(left_value, right_value)

            if result is None and self.datacheck.supports_warning:
                try:
                    warning_value = self.right_executor.execute(self.datacheck.warning_logic)
                    self.checkrun.warning_value = str(warning_value)
                except Exception as exc:
                    errors.append(str(exc))
                    status = False

        end_time = dt.now(pytz.utc)

        if status:
            self.checkrun.status = STATUSES.FINISHED
            self.checkrun.result = result
            self.checkrun.end_time = end_time
        else:
            self.checkrun.error_message = '\n'.join(errors)
            self.checkrun.status = STATUSES.ERROR

        self.checkrun.save()

        try:
            environment_status: EnvironmentStatus = EnvironmentStatus.objects.get(
                environment=self.checkrun.environment,
                datacheck=self.checkrun.datacheck
            )
            environment_status.user = self.checkrun.user
        except EnvironmentStatus.DoesNotExist:
            environment_status: EnvironmentStatus = EnvironmentStatus(
                environment=self.checkrun.environment,
                datacheck=self.checkrun.datacheck,
                user=self.checkrun.user
            )

        environment_status.result = result
        if status:
            environment_status.last_start_time = self.checkrun.start_time
            environment_status.last_end_time = end_time
            environment_status.status = STATUSES.FINISHED
        else:
            environment_status.last_start_time = None
            environment_status.last_end_time = None
            environment_status.status = STATUSES.ERROR
        environment_status.save()


class CheckComparator:

    def __init__(self, datacheck: Datacheck):
        self.datacheck = datacheck

    def compare(self, left, right, warning_check: bool = False):

        if warning_check:
            relation = self.datacheck.warning_relation
        else:
            relation = self.datacheck.relation

        if relation == RELATIONS.eq:
            res = RESULTS.SUCCESS if left == right else False
        elif relation == RELATIONS.ne:
            res = RESULTS.SUCCESS if left != right else False
        elif relation == RELATIONS.gt:
            res = RESULTS.SUCCESS if left > right else False
        elif relation == RELATIONS.ge:
            res = RESULTS.SUCCESS if left >= right else False
        elif relation == RELATIONS.lt:
            res = RESULTS.SUCCESS if left < right else False
        elif relation == RELATIONS.le:
            res = RESULTS.SUCCESS if left <= right else False
        else:
            res = None

        if res is False and not warning_check:
            res = RESULTS.FAILED

        return res
