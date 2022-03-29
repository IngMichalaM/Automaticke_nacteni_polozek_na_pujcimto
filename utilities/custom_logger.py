import logging
import time


def custom_logger(logging_level=logging.DEBUG):
    time_today = time.strftime("%Y_%m_%d")
    newname = 'pujcimto_logger_' + time_today + '.txt'

    logger = logging.getLogger('pujcimto_log')  # name of the logger , not the file

    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        level=logging_level,
                        filename=newname,
                        datefmt='%d.%m.%Y %H:%M:%S')

    return logger
