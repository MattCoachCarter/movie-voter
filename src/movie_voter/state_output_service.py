from movie_voter.state_output_backends.json_file_state_output_backend \
    import JSONFileStateOutputBackend
from movie_voter.state_output_backends.stdout_state_output_backend \
    import StdoutStateOutputBackend

from .utils import get_logger


class StateOutputService(object):
    def __init__(self, config):
        self.config = config
        self.logger = get_logger('StateOutputService')
        self.logger.debug('Constructing')
        self.setup_backend(self.config['state_output']['backend'])
        self.started = False

    def save_state(self, state_dict):
        """Take in a state dictionary and save it using our configured backend
        :param state_dict: A dictionary representing state to save 
        """
        if self.started:
            self.backend.save(sate_dict)
        else:
            raise RuntimeError('save_state called before starting service')

    def setup_backend(self, backend_type):
        """Set up the backend user input service
        """
        self.backend = None

        self.logger.info('Setting up backend: {}'.format(backend_type))
        if backend_type == "json_file":
            self.backend = JSONFileStateOutputBackend(self.config)
        elif backend_type == "stdout":
            self.backend = StdoutStateOutputBackend(self.config)
        else:
            raise RuntimeError('Unrecognized backend type: {}, currently '
                'json_file and stdout are the only supported backends'.format(
                    backend_type))

    def start_backend(self):
        self.logger.info('Starting backend')
        self.backend.start()

    def start(self):
        """Start the backend and thus the service
        """
        self.start_backend()
        self.started = True
