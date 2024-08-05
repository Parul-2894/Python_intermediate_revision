"""
 Log handlers, log handlers are required for dispatching different
 messages to output stream, file, http or via email 
"""

# Loggings 

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) #yu would need to set the newly created logger logging level.
#create handler
stream_h = logging.StreamHandler() #to log to a stream
file_h = logging.FileHandler('file.log') #to log to a file

#level and the format:
stream_h.setLevel(logging.INFO)
file_h.setLevel(logging.WARNING)

formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

#add handler to logger
logger.addHandler(stream_h)
logger.addHandler(file_h)



logger.warning("This is a warning")
logger.info("this is a debug message")