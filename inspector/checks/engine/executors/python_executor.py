from . import CheckExecutor
from ...constants import CHECK_TYPES


class PythonExecutor(CheckExecutor):
    supported_check_types = (CHECK_TYPES.NUMBER, CHECK_TYPES.STRING, CHECK_TYPES.DATE)

    def execute(self, check_logic):
        if self.check_type == CHECK_TYPES.STRING:
            return str(check_logic)
        if self.check_type == CHECK_TYPES.NUMBER:
            return float(check_logic)
