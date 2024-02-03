__author__ = 'Yassine Asghar'
__version__ = '1.0.0'
__date__ = '3.02.2024'

import logging
from logging.handlers import RotatingFileHandler

class Logs:
    """
    The Logs class is used to set up logging handlers and add log messages.

    Attributes:
        log (logging.Logger): Logger object for logging messages.

    Args:
        name (str, optional): Name of the logger. Defaults to "default".
        log_file (str, optional): Path to the log file. Defaults to None.
        max_size (int, optional): Maximum size of log file in bytes. Defaults to 10**6.
        backup (int, optional): Number of backup log files to keep. Defaults to 5.

    Methods:
        _setup_file_handler: Sets up file handler for logging to a file.
        _setup_stream_handler: Sets up stream handler for logging to the console.
        add: Adds a log message with the specified log level.

    """
    def __init__(self, name="default", log_file=None, max_size=10**6, backup=5):
        self.log = logging.getLogger(name)
        self.log.setLevel(logging.DEBUG)
        if not self.log.handlers:
            self._setup_file_handler(log_file, max_size, backup)
            self._setup_stream_handler()

    def _setup_file_handler(self, log_file, max_size, backup):
        f_format = '%(asctime)s - %(levelname)s - %(message)s'
        f_handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup)
        f_handler.setFormatter(logging.Formatter(f_format))
        self.log.addHandler(f_handler)

    def _setup_stream_handler(self):
        s_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        s_handler = logging.StreamHandler()
        s_handler.setFormatter(logging.Formatter(s_format))
        self.log.addHandler(s_handler)

    def add(self, level, msg):
        try:
            log_method = getattr(self.log, level.lower())
        except AttributeError:
            raise ValueError(f'Invalid logging level: {level}')
        else:
            log_method(msg)

    def catch(self, msg):
        """
        Adds an error log message and includes the current exception stack trace.

        Args:
            msg (str): The log message.
        """
        self.log.error(msg, exc_info=True)