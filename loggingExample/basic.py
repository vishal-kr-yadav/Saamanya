#!/usr/bin/python3
#importing module
import logging

#Create and configure logger
logging.basicConfig(filename="newfile.log",
					format='%(asctime)s %(message)s',
					filemode='w')

#Creating an object
logger=logging.getLogger()

#Setting the threshold of logger to DEBUG
logger.setLevel(logging.ERROR)

#Test messages
logger.debug("DEBUG")
logger.info("INFO")
logger.warning("WARNING")
logger.error("ERROR")
logger.critical("CRITICAL")
