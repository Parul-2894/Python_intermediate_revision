import logging
import traceback

logging.basicConfig(
    filename="output.log",
    level=logging.DEBUG,
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
    datefmt='%m/%d/%Y %H:%M:%S'

)
logger = logging.getLogger(__name__)

a=[1,2,3]
try: 
    b = a[4] #index out of range
except Exception as e:
    logger.error(e, exc_info=True)

# If you want to add some string
try: 
    b = a[4] #index out of range
except Exception as e:
    logger.error("This is the error %s", traceback.format_exc())