from threading import Thread

from movie_voter.utils import get_logger


class UserOutputBackendBase(Thread):
    """Base class for the user output backend classes
    """

    def __init__(self, config):
        self.config = config
        self.logger = get_logger('UserOutputBackendBase')
        self.logger.debug('Constructing')
        self.running = False
        Thread.__init__(self)

    def send_output(self, user_id, output_to_send):
        """Send the given output to the user denoted by the given user_id. This
        function should be overridden in the child classes of this base class
        """
        self.logger.error('send_output called in the base class')

    def stop(self):
        """Stop running the thread by setting running to False
        """
        self.logger('Stopping')
        self.running = False

    def run(self):
        """Start the thread. This should be overriden in the child classes.
        Implementations of this function should set running to True and stop
        running when run is set to False
        """
        self.logger.error('run invoked in the base class')
