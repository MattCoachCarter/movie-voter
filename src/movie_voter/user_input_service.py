from threading import Thread

from movie_voter.user_input_backends.twilio_user_input_backend import \
TwilioUserInputBackend
from .utils import get_logger

class UserInputService(Thread):
    def __init__(self, config, movie_voter):
        Thread.__init__(self)
        self.movie_voter = movie_voter
        self.config = config
        self.logger = get_logger('UserInputService')
        self.logger.debug('Constructing')
        self.setup_backend(self.config['user_input']['backend'])
        self.started = False

    def on_user_input(self, input_data_dict):
        """Take in/process user input
        :param input_data_dict: A dictionary containing the following data:
                                type: a string denoting the type of input
                                user: a string that will uniquely identify a
                                      user
                                value: a string representing the value of the
                                       user input
        """
        self.logger.info('Passing up user input to the movie voter')
        if self.started:
            self.movie_voter.accept_user_input(input_data_dict)
        else:
            raise RuntimeError('on_user_input called before started, is this '
                'even possible?')

    def setup_backend(self, backend_type):
        """Set up the backend user input service
        """
        self.backend = None

        self.logger.info('Setting up backend: {}'.format(backend_type))
        if backend_type == "twilio":
            self.backend = TwilioUserInputBackend(self.config, self)
        else:
            raise RuntimeError('Unrecognized backend type: {}, currently '
                'twilio is the only supported backend'.format(backend_type))

    def start_backend(self):
        """Call start on the backend input handler
        """
        self.logger.info('Starting backend')
        self.backend.start()

    def stop_backend(self):
        self.logger.debug('Stopping backend')
        self.backend.stop()

    def start(self):
        """Start the backend, thus starting the service
        """
        self.start_backend()
        self.started = True

    def stop(self):
        """Stop the service by stopping the backend thread
        """
        self.stop_backend()
        self.started = False
