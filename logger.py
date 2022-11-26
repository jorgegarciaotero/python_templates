import os 
import sys 
from datetime import datetime
from datetime import timedelta
import numpy as np
import sys
import math
import sqlalchemy
import pandas as pd

import logging
from importlib import reload
sys.path.insert(1, '/app/tools/route/bin') #example of sys.path

def initLog(logpath,logname):
    logging.shutdown()
    reload(logging)
    logname=logpath+'/'+logname
    logfile =datetime.now().strftime(logname)
    logger = logging.getLogger("LogVision")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def routineExample(logger):
    try:
        print("Something")
        logger.info("printed")
    except Exception as err:
        logger.warning("Warning, some issue")
        logger.error(err)
        sys.exit(0)
 
def main(argv):
    logpath = os.path.dirname('/home/jorgegarciaotero/python_templates/logs')
    logname = 'myLogName.log'
    logger=initLog(logpath,logname)
    logger.info("Starting Process")




    
if __name__ == "__main__":
    main(sys.argv[1:])





