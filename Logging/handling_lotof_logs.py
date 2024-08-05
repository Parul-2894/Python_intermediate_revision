"""
    If you have a big application and there are lot
    of log messages, then you can use a rotating file handler.
    it will keep the files small.
"""

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logger.addHandler(RotatingFileHandler('Logging/logs/run.log', maxBytes=2000, backupCount=5))

for _ in range(20000):
    logger.info("Hello  world")



