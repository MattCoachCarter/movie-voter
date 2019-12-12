from .state_output_service import StateOutputService
from .user_input_service import UserInputService
from .user_output_service import UserOutputService
from .utils import get_logger



class MovieVoter(object):
    def __init__(self, config):
        self.logger = get_logger('MovieVoter')
        self.logger.debug('Constructing')
        

    def accept_user_input(self, user_input):
        """TODO
        """
        pass # TODO

    def send_output_to_user(self, user_key, output_data):
        """TODO
        """
        pass # TODO

    def save_state(self):
        """TODO
        """
        pass

    def setup_user_input_service(self):
        """TODO
        """
        pass

    def setup_user_output_service(self):
        """TODO
        """
        pass

    def setup_state_output_service(self):
        """TODO
        """
        pass
