class CheckExecutorException(Exception):
    pass


class InstanceNotFound(CheckExecutorException):
    def __init__(self, system, environment):
        super().__init__(
            f"No instance for system [{system.name}] in environment [{environment.name}]"
        )


class CheckTypeNotSupported(CheckExecutorException):
    pass
