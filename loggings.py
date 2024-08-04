# Loggings 

import logging

logging.basicConfig(
    filename="output.log",
    level=logging.DEBUG,
    format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
    datefmt='%m/%d/%Y %H:%M:%S'

)

#there are 5 different logging levels 
logging.debug("This is debug message ")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#by default the logger is root. But when you 
#have your own module you need to put your module name
#as the logger. 
#for that switch to file helpers_log.py