from abc import ABCMeta
from typing import Tuple, Union

from ..exceptions import CheckTypeNotSupported
from ....systems.constants import APPLICATIONS
from ....systems.models import Instance

CONFIG = {
    APPLICATIONS.POSTGRES: {
        'executor.module': 'sql_executor',
        'executor.class': 'SQLExecutor',
        'params': {
            'connection_string': 'postgres+psycopg2://{0}:{1}@{2}:{3}/{4}'
        }
    },
    APPLICATIONS.REDSHIFT: {
        'executor.module': 'sql_executor',
        'executor.class': 'SQLExecutor',
        'params': {
            'connection_string': 'redshift+psycopg2://{0}:{1}@{2}:{3}/{4}'
        }
    },
    APPLICATIONS.MYSQL: {
        'executor.module': 'sql_executor',
        'executor.class': 'SQLExecutor',
        'params': {
            'connection_string': 'mysql://{0}:{1}@{2}:{3}/{4}'
        }
    }
}


class CheckExecutor(metaclass=ABCMeta):
    supported_check_types: Tuple = tuple()

    def __init__(self, instance: Union[Instance, None], check_type):
        self.instance = instance
        self.check_type = check_type
        if check_type not in self.supported_check_types:
            raise CheckTypeNotSupported

    def test_connection(self):
        pass

    def execute(self, check_logic):
        pass
