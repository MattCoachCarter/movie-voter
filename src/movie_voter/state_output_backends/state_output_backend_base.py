from threading import Thread
from time import sleep

from movie_voter.utils import get_logger

class StateOutputBackendBase(Thread):
    """Base class for the state output backend classes
    """

    def __init__(self, config):
        self.config = config
        self.logger = get_logger('StateOutputBackendBase')
        self.logger.debug('Constructing')
        self.pending_state = None
        self.running = False
        Thread.__init__(self)

    def save(self, state_dict):
        """Save the state. Really, just store the state in an instance
        variable so we can save it later asynchronously
        :param state_dict: A dictionary representing the state to save
        """
        self.logger.debug('Assigning new state to pending_state')
        self.pending_state = state_dict

    def save_pending(self):
        """If the pending state is not None, format it and save it
        """
        if self.pending_state is not None:
            self.output_state(self.format_state(self.pending_state))

    def format_state(self, state_dict):
        """Given a state dictionary, format it to a specific string and return
        said string. This should be overridden in child classes
        :param state_dict: The state dictionary that should be formatted
        :returns: string of formatted state
        """
        self.logger.error('format_state called in base class')
        return str(state_dict)

    def output_state(self, formatted_state):
        """Given a formatted state string, output it to the backend
        This should be overridden in the child classes
        :param formatted_state: A formatted state str
        """
        self.logger.error('output_state called in base class')
        print(str(formatted_state))

    def stop(self):
        """Set the "running" bool instance variable to False to stop the thead
        """
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.save_pending()
            if self.running:
                sleep(float(self.config['state_output']['sleep_interval']))
