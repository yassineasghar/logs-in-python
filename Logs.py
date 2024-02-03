__author__ = 'Yassine Asghar'
__version__ = '1.0.0'
__date__ = '3.02.2024'

import logging
from logging.handlers import RotatingFileHandler


class Logs:
    """A class for logging messages to a file and stream

    This class provides functionality for logging messages to a specified log file and stream. It uses the logging module from the Python standard library to handle logging operations.

    Attributes:
        log (Logger): The logger object for logging messages.

    Methods:
        __init__(self, name="default", log_file=None, max_size=10**6, backup=5): Initializes the Logs class. Sets the logger name, log file, max size, and backup count.
        _setup_file_handler(self, log_file, max_size, backup): Sets up the file handler for the logger.
        _setup_stream_handler(self): Sets up the stream handler for the logger.
        add(self, level, msg, exc_info=False): Adds a log message with the specified log level and message.
        catch(self, msg): Adds an error log message with exception information.

    """
    def __init__(self, name="default", log_file=None, max_size=10**6, backup=5):
        self.log = logging.getLogger(name)
        self.log.setLevel(logging.DEBUG)
        if not self.log.handlers:
            self._setup_file_handler(log_file, max_size, backup)
            self._setup_stream_handler()

    def _setup_file_handler(self, log_file, max_size, backup):
        f_handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup)
        f_format = '%(asctime)s - %(levelname)s - %(message)s'
        f_handler.setFormatter(logging.Formatter(f_format))
        self.log.addHandler(f_handler)

    def _setup_stream_handler(self):
        s_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        s_handler = logging.StreamHandler()
        s_handler.setFormatter(logging.Formatter(s_format))
        self.log.addHandler(s_handler)

    def add(self, level, msg, exc_info=False):
        try:
            log_func = getattr(self.log, level.lower())
        except AttributeError:
            raise ValueError(f'Invalid logging level: {level}')
        else:
            log_func(msg, exc_info=exc_info)

    def catch(self, msg):
        self.add('ERROR', msg, exc_info=True)
