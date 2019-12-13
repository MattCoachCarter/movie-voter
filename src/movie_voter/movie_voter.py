import re

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

    def sanitize_value(self, value):
        """Given a value, convert the value to a string and run it through a
        bunch of regex substitutions to sanitize it, and return the sanitized
        version
        """
        # Substitute repeated spaces with single spaces
        value = re.sub(r'\s+', ' ', str(value))
        # Remove spaces at the beginning of the string
        value = re.sub(r'^\s+', '', value)
        # Remove spaces at the end of the string
        value = re.sub(r'\s+$', '', value)
        # Remove special characters:
        value = re.sub(r'[@#\$%\^\&*\)\(+=._-]', '', value)

        return value

    def sanitize_user_input(self, user_input_dict):
        """Given an input user/value manipulate the value so it is easier to
        use and return the user and value as a tuple
        """
        user = user_input_dict.get(['user'], 'UNKNOWN')
        value = user_input_dict.get('value', '')
        return (self.sanitize_value(user).replace(' ', '').upper(),
                self.sanitize_value(value).upper())

    def accept_user_input(self, user_input):
        """Accept user input, and alter our state based on it
        """
        self.logger.info('Got new user input: {}'.format(user_input))
        user, value = sanitize_user_input(user_input)
        
        # Make sure we got a sane user:
        if user == 'UNKNOWN':
            self.logger.error('Got unknown user in user input')
        else:
            if self.state is None or self.state['state'] == 'finished':
                # We haven't even started yet, so we expect this to be a start
                # message with a number of users
                self.handle_input_ready_to_start(value)
            elif self.state['state'] == 'waiting_for_suggestions':
                # We expect this to be a user suggestion
                pass # TODO
            elif self.state['state'] == 'waiting_for_votes':
                # We expect this to be a set of votes
                pass # TODO
            elif self.state['state'] == 'finished':
                # The only thing we should allow the user to do at this point
                # is start over
                pass # TODO
            else:
                raise RuntimeError('MovieVoter in unknown state: {}'.format(
                    self.state['state']))

    def handle_input_ready_to_start(self, value):
        """Given a sanitized user and value handle the input value such that
        we expect to start a new suggestion/voting session
        """
        invalid_value_msg = 'Invalid value received: {}'.format(value)
        if value.startswith('START') and value.count(' ') == 1:
            split = value.split(' ')
            try:
                expected_users = int(split[1])
            except:
                expected_users = 'invalid'

            if split[0] == 'START' and str(expected_users) == split[1]:
                self.logger.info('Starting with {} expected users'.format(
                    expected_users))
                self.state = {}
                state_updates = {
                    'state': 'waiting_for_suggestions',
                    'expected_users': expected_users
                }
                self.update_state(state_updates)
            else:
                self.logger.error(invalid_value_msg)
        else:
            self.logger.error(invalid_value_msg)

    def send_output_to_user(self, user_key, output_data):
        """User the user output service to send output to a user
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
