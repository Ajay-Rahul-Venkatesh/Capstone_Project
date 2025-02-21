import pytest
import logging

@pytest.mark.usefixtures('browser_setup')
class Baseclass:

    def get_logger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(filename)s :%(funcname)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        return logger
