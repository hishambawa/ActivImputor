from zlog import logger, level, ConsoleFormatter

LOG_LEVELS = {
            "debug": level.Level.DEBUG,
            "info": level.Level.INFO,
            "warn": level.Level.WARN,
            "error": level.Level.ERROR,
            "fatal": level.Level.FATAL
        }

class Logger:
    def __init__(self, log_level):
        # set the log level.
        # if the passed level is not found, default value is set to INFO
        logger.base_level = LOG_LEVELS.get(log_level, level.Level.INFO)

    def log_debug(self, message):
        logger.debug().msg(message)

    def log_info(self, message):
        logger.info().msg(message)

    def log_warn(self, message):
        logger.warn().msg(message)

    def log_error(self, message):
        logger.error().msg(message)

    def log_fatal(self, message):
        logger.fatal().msg(message)
        exit(1)