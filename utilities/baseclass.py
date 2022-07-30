import inspect
import logging
import pytest

from testdata.constant import Constant

# @author SPEC INDIA
@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        # create logger
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logger.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")

        # Create a filehandler
        fileHandler = logging.FileHandler(Constant.LOG_PATH)
        fileHandler.setFormatter(formatter)

        # Add a filehandler to logger
        logger.addHandler(fileHandler)

        return logger