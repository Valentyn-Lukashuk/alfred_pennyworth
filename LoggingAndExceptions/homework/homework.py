import logging.handlers



class Error(Exception):
    pass


class TooManyVisitors(Error):
    pass


class TooFewVisitors(Error):
    pass


class Concert:
    max_visitors = 200
    min_visitors = 10

    # add 2 class attributes - max_visitors (200) and min_visitors (10)

    def __init__(self, visitors_num):
        self.visitors_num = visitors_num
        # """
        # if visitors num is bigger than max_visitors - raise TooManyVisitors error
        # if visitors num is less than min_visitors - raise TooFewVisitors error
        # """
        if visitors_num > Concert.max_visitors:
            raise TooManyVisitors
        elif visitors_num < Concert.min_visitors:
            raise TooFewVisitors


def make_concert(visitors_num):
    # """
    #    create Concert instance - handle TooManyVisitors and TooFewVisitors errors here:
    #    in case if caught - log error to console and return False, in case of successful initialization - return True
    #    """
    try:
        Concert(visitors_num)
    except TooFewVisitors:
        log_message("not enough visitors", 20)
        return False
    except TooManyVisitors:
        log_message("a lot of visitors", 30)
        return False
    else:
        return True


# create Logger object
# set level to debug
# add handler to write logs to file "test.log"
logging.basicConfig(filename='test.log', filemode='a', level=logging.DEBUG)
logger = logging.getLogger("logs")
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(filename="test.log", maxBytes=200, backupCount=1)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)


def log_message(message, level):
    if level == 10:
        return logger.debug(f"{message}")
    elif level == 20:
        return logger.info(f"{message}")
    elif level == 30:
        return logger.warning(f"{message}")
    elif level == 40:
        return logger.error(f"{message}")
    elif level == 50:
        return logger.critical(f"{message}")
    # """
    # this function should use the logger defined above and log messages.
    # level is the numeric representation of log level the message should refer to.
    # :param message:
    # :param level:201
    # """


