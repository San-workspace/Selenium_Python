import logging

def test_logging():
    logger=logging.getLogger(__name__)

    filehandler=logging.FileHandler("logfile.log")
    formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)


    logger.setLevel(logging.DEBUG) # print the log in all the level
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("wanrning alert")
    logger.error("erro message")
    logger.critical("critical message")