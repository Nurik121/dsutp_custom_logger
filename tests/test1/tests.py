import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from custom_logger import Logging

# Without options
log = Logging(log_location='tests/test1/log.log').get_logger()
log.info('Test my logs')
