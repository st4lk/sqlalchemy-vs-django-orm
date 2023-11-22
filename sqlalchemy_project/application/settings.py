import logging
import logging.config
import os

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
SERVICE_NAME = 'my-service'

DB_USER = 'appuser'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_NAME = 'sqlal_project'
DB_PORT = '55440'

# https://docs.sqlalchemy.org/en/20/core/engines.html#sqlalchemy.create_engine.params.connect_args
DB_POOL_SIZE = 2  # default is 5
DB_MAX_OVERFLOW = 1  # default is 10
DB_POOL_RECYCLE = 3600  # default is -1, no recycle. In seconds.
DB_POOL_TIMEOUT = 30  # default is 30. In seconds.
DB_LOG = os.getenv('DB_LOG') in [1, '1', 'True', 'true']


class FilterSQLAlchemyLogs(logging.Filter):
    def filter(self, record):
        if record.name.startswith('sqlalchemy') and not DB_LOG:
            return False
        if len(record.args) == 2 and record.args[0] == 'raw sql' and str(record.args[1]) == '()':
            return False
        return True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'filter_sqlalchemy': {
            '()': FilterSQLAlchemyLogs
        }
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)s:%(name)s: %(message)s (%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'sqlalchemy': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
            'filters': ['filter_sqlalchemy'],
        },
        'sqlalchemy.engine.Engine': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
            'filters': ['filter_sqlalchemy'],
        },
        'sqlalchemy.orm': {
            'filters': ['filter_sqlalchemy'],
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'sqlalchemy.pool.impl.AsyncAdaptedQueuePool': {
            'filters': ['filter_sqlalchemy'],
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'filters': ['filter_sqlalchemy'],
        },
    }
}
logging.config.dictConfig(LOGGING)
