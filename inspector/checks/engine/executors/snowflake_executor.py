from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
from json import loads
from .sql_executor import SQLExecutor, CheckExecutor


class SnowflakeExecutor(SQLExecutor):
    def __init__(self, *args, **kwargs):
        CheckExecutor.__init__(self, *args, **kwargs)
        json_data = loads(self.instance.extra_json)
        self.engine = create_engine(
            URL(
                user=self.instance.login,
                password=self.instance.password,
                account=json_data["account"],
                region=json_data["region"],
                database=self.instance.db,
                warehouse=json_data["warehouse"],
                role=json_data["role"],
            )
        )
