import logging
import logging.config
from os import path

logging_path= path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(logging_path)

logger = logging.getLogger('simpleExample')

logger.debug("Ths is a debug message")