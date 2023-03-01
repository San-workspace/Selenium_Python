import inspect
import logging

import pytest


class Baseclass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]  # to get exact testcase name in log
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)  # print the log in all the level
        return logger
