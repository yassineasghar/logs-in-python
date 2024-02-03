__author__ = 'Yassine Asghar'
__version__ = '1.0.0'
__date__ = '3.02.2024'

import logging

LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


class Logs:
    """
    Class Logs
    The Logs class provides a simple interface for logging messages to a file and to the console using the
    standard logging module.
    Methods:
        - __init__(self, logger_name=None, log_file=None): Initializes the Logs object with a logger
        name and log file path.
        - add(self, level, msg): Adds a log message with the specified log level.
    Example usage:
        # Create an instance of the Logs class
        logs = Logs(logger_name='my_logger', log_file='file.log')
        # Add a log message with level DEBUG
        logs.add('DEBUG', 'This is a debug message')
    """
    def __init__(self, logger_name="default_logger", log_file=None):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file)
            file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)
            stream_handler = logging.StreamHandler()
            sformater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            stream_handler.setFormatter(sformater)
            self.logger.addHandler(stream_handler)

    def add(self, level, msg):
        if level.upper() in LEVELS:
            getattr(self.logger, level.lower())(msg)
        else:
            raise ValueError('Invalid logging level: ', level)