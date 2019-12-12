from threading import Thread

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
            pass # TODO
        else:
            raise RuntimeError('Unrecognized backend type: {}, currently '
                'twilio is the only supported backend'.format(backend_type))

    def start_backend(self):
        self.backend.start()

    def start(self):
        """Start the backend, thus starting the service
        """
        self.start_backend()
        self.started = True
