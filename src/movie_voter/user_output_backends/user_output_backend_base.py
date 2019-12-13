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
        self.pending_output = []
        Thread.__init__(self)

    def send_output(self, user_id, output_to_send):
        """Grab output and store it as pending output. Pending output will
        periodically be sent asynchronously
        """
        self.logger.debug('Storing new pending output')
        self.pending_output.append((user_id, output_to_send))

    def send_pending_output(self):
        """Send any pending output we might have. This function should be
        overridden in the child classes of this base class
        """
        self.logger.error('send_output called in the base class')

    def stop(self):
        """Stop running the thread by setting running to False
        """
        self.logger('Stopping')
        self.running = False

    def do_teardown(self):
        """To be overridden in child classes. Tear down any thing necessary
        when the thread it stopped
        Does not need to be overridden if there is nothing to tear down
        """
        pass

    def run(self):
        """Start the thread, and periodically send any pending output we have
        ready to go.
        Stop running when running is set to False
        """
        self.running = True
        while self.running:
            self.send_pending_output()
            time.sleep(self.config['user_output']['sleep_interval'])
        self.do_teardown()
