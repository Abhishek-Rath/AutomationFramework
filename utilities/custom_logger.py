import inspect
import logging

def custom_logger(logLevel = logging.DEBUG):
    # get the name of the class/method from where this is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default log all the messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode = 'a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler((fileHandler))

    return logger