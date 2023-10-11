import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from dsutp_custom_logger import Logging

# Without options
log = Logging(log_location='tests/test4/log.log', log_buffer_size_file=10, backupCount=3).get_logger()

for i in range(10):
    log.info(f'Test my logs {i}')
