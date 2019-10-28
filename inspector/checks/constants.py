from model_utils import Choices

RELATIONS = Choices(
    (0, "eq", "="),
    (1, "ne", "!="),
    (2, "gt", ">"),
    (3, "lt", "<"),
    (4, "ge", ">="),
    (5, "le", "<="),
)

STATUSES = Choices(
    ("NEW", "New"), ("RUNNING", "Running"), ("FINISHED", "Finished"), ("ERROR", "Error")
)

RESULTS = Choices(("SUCCESS", "Success"), ("WARNING", "Warning"), ("FAILED", "Failed"))

CHECK_TYPES = Choices(
    (0, "SQL_QUERY", "SQL query"),
    (1, "SQL_EXPRESSION", "SQL expression"),
    (2, "NUMBER", "Number"),
    (3, "STRING", "String"),
    (4, "DATE", "Date"),
    (5, "PYTHON_EXPRESSION", "Python expression"),
)
