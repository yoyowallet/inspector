from model_utils import Choices

APPLICATIONS = Choices(
    (0, 'POSTGRES', 'Postgresql'),
    (1, 'REDSHIFT', 'Redshift'),
    (2, 'MYSQL', 'MySQL')
)
