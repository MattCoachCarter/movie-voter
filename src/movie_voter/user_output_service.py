from movie_voter.user_output_backends.stdout_user_output_backend import \
StdoutUserOutputBackend
from .utils import get_logger

class UserOutputService(object):
    def __init__(self, config):
        self.logger = get_logger('UserOutputService')
        self.logger.debug('Constructing')
        self.config = config
        self.setup_backend(self.config['user_output']['backend'])
        self.started = False

    def send_output(self, user_id, output_to_send):
        """Send the output to a given user via the backend.
        :param user_id: A string denoting a user to send the output to. Could
                        vary based on backend
        :param output_to_send: A string of output to send to the user denoted
                               by the user previously mentioned
        """
        if self.started:
            self.backend.send_output(user_id, output_to_send)
        else:
            raise RuntimeError('send_output called before the service was started')

    def setup_backend(self, backend_type):
        """Set up the backend for the user output service
        :param backend_type: A string denoting the backend to be used (should
        come from the config)
        """
        self.backend = None

        if backend_type == "stdout":
            self.backend = StdoutUserOutputBackend(self.config)
        elif backend_type == "twilio":
            pass # TODO
        else:
            raise RuntimeError('Unrecognized backend type: {}, currently '
                'stdout and twilio are the only supported backends'.format(
                    backend_type))

    def start_backend(self):
        self.backend.start()

    def run(self):
        """Run the thread, to invoke run start()
        """
        self.start_backend()
        self.started = True
