from .user_input_backend_base import UserInputBackendBase
from movie_voter.utils import get_logger

class TwilioUserInputBackend(UserInputBackendBase):
    """Class to handle user input from twilio
    """

    def __init__(self, config, user_input_service):
        super(TwilioUserInputBackend, self).__init__(config, user_input_service)
        self.logger = get_logger('TwilioUserInputBackend')
        self.logger.debug('Constructing')

    def run(self):
        """OVERRIDE of run in base class
        """
        self.logger.info('Running')
        # TODO

