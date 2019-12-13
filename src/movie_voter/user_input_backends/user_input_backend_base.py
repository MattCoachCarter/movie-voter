from threading import Thread
from time import sleep

from movie_voter.utils import get_logger

class UserInputBackendBase(Thread):
    """Base class for the state output backend classes
    """

    def __init__(self, config, user_input_service):
        self.config = config
        self.logger = get_logger('UserInputBackendBase')
        self.logger.debug('Constructing')
        self.running = False
        self.user_input_service = user_input_service
        Thread.__init__(self)

    def on_user_input(self, input_data):
        """To be called in child classes when input is ready to be passed up
        :param input_data: The formatted input data dictionary
        """
        self.logger.info('Passing user input up to user input service')
        self.user_input_service.on_user_input(input_data)

    def stop(self):
        """Set the "running" bool instance variable to False to stop the thead
        """
        self.running = False

    def run(self):
        """To be implemented in the child classes, run the thread and start
        accepting user input.
        Implementations of this should be able to stop running when
        self.running becomes False
        """
        self.logger.error('run called in base class')
