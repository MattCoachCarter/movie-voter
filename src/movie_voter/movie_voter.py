from .state_output_service import StateOutputService
from .user_input_service import UserInputService
from .user_output_service import UserOutputService
from .utils import get_logger



class MovieVoter(object):
    def __init__(self, config):
        self.config = config
        self.logger = get_logger('MovieVoter')
        self.logger.debug('Constructing')
        self.state = None
        self.user_input_service = None
        self.user_output_service = None
        self.state_output_service = None

    def accept_user_input(self, user_input):
        """TODO
        """
        pass # TODO

    def send_output_to_user(self, user_key, output_data):
        """TODO
        """
        self.user_output_service.send_output(user_key, output_data)

    def save_state(self):
        """Use the state output service to save the state
        """
        self.state_output_service.save_state(self.state)

    def update_state(self, updates):
        """Update the stored state with the given state updates
        """
        self.state.update(updates)
        self.save_state()

    def setup_services(self):
        """Set up all the input/output services
        """
        self.logger.info('Setting up all services')
        self.setup_user_input_service()
        self.setup_user_output_service()
        self.setup_state_output_service()

    def setup_user_input_service(self):
        """Set up the user input service instance variable
        """
        self.logger.debug('Setting user input service')
        self.user_input_service = UserInputService(self.config, self)

    def setup_user_output_service(self):
        """Set up the user output service instance variable
        """
        self.logger.debug('Setting user output service')
        self.user_output_service = UserOutputService(self.config)

    def setup_state_output_service(self):
        """Set up the state output service instance variable
        """
        self.logger.debug('Setting state output service')
        self.state_output_service = StateOutputService(self.config)

    def start(self):
        """Set up and start all the services
        """
        self.logger.info('Starting')
        self.setup_services()
        self.user_input_service.start()
        self.user_output_service.start()
        self.state_output_service.start()

    def stop(self):
        """Stop all the services
        """
        self.logger.info('Stopping')
        self.user_input_service.stop()
        self.user_output_service.stop()
        self.state_output_service.stop()
