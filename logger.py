import logging

def get_logger():
    logger = logging.getLogger('myapp')
    hdlr = logging.FileHandler('tree.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
    return logger


