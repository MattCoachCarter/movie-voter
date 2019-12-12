import logging


def get_logger(logger_name):
    """Convenience function for objects to create an get a handle to a logger
    :param logger_name: A string with the name that the logger should have
    :returns: A configured logger object with the given name
    """
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=log_format) # This only does something the
                                           # first time it is called, since
                                           # force is not set to True
    return logging.getLogger(logger_name)
