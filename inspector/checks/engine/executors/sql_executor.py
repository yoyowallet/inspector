from sqlalchemy import create_engine

from . import CheckExecutor
from ...constants import CHECK_TYPES


class SQLExecutor(CheckExecutor):
    supported_check_types = (CHECK_TYPES.SQL_QUERY, CHECK_TYPES.SQL_EXPRESSION)

    def __init__(self, *args, **kwargs):
        self.connection_string = kwargs.pop("connection_string")
        super().__init__(*args, **kwargs)
        self.engine = create_engine(
            self.connection_string.format(
                login=self.instance.login,
                password=self.instance.password,
                host=self.instance.host,
                port=self.instance.port,
                db=self.instance.db,
            )
        )

    def test_connection(self):
        connection = self.engine.connect()
        connection.close()

    def execute(self, check_logic):
        connection = self.engine.connect()
        res = connection.execute(check_logic)
        row = res.fetchone()
        connection.close()
        return row[0]
