import logging

logger = logging.getLogger(__name__) #This will create
#a logger with the name of the module
"""
    loggers logging propagates to the root logger
becasue when we create new loggers it creates 
a heirarchy of 
and uses it's configurations. But if we want t stop that we 
can use logger.propagate = False
"""

logger.propagate = False
logger.critical("hello from helper")

