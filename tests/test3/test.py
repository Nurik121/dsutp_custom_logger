import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from dsutp_custom_logger import Logging

# Without options
log = Logging(
    log_location='tests/test3/log.log',
    base_json_fields={
        'level': 'levelname',
        'message': 'message',
        'loggerName': 'name',
        'processName': 'processName',
        'processID': 'process',
        'threadName': 'threadName',
        'threadID': 'thread',
        'timestamp': 'asctime',
        'filename': 'filename',
        'module': 'module',
        'pathname': 'pathname',
    },
    custon_json_fields={'test': 'my test field'},
).get_logger()
log.info('Test my logs')
