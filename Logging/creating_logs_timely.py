import logging
from logging.handlers import TimedRotatingFileHandler
import time
logging.basicConfig(
    level=logging.DEBUG,
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
    datefmt='%m/%d/%Y %H:%M:%S'
)
logger = logging.getLogger(__name__)

handler = TimedRotatingFileHandler('Logging/timming_logs/run.log', when='s', interval=2, backupCount=5)

logger.addHandler(handler)

for _ in range(10):
    time.sleep(2)
    logger.debug("Running")