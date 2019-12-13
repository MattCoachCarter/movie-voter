from .user_output_backend_base import UserOutputBackendBase
from time import sleep
from twilio.rest import Client

from movie_voter.utils import get_logger


class TwilioUserOutputBackend(UserOutputBackendBase):
    """Class to send user output to useres over twilio
    """

    def __init__(self, config):
        super(TwilioUserOutputBackend, self).__init__(config)
        self.logger = get_logger('TwilioUserOutputBackend')
        self.logger.debug('Constructing')
        self.setup_twilio_client()

    def send_pending_output(self):
        """OVERRIDES send_pending_output from the base class
        """
        while len(self.pending_output) > 0:
            user_id, output_to_send = self.pending_output.pop(0)
            self.logger.info('Sending output to {}'.format(user_id))
            self.twilio_client.messages.create(
                body=str(output_to_send),
                from_=str(self.config['user_output']['twilio']['number']),
                to=str(user_id)
            )

    def setup_twilio_client(self):
        """Set up the twilio client to use to send user output
        """
        self.logger.info('Setting up Twilio client')
        account_sid = self.config['user_output']['twilio']['account_sid']
        auth_token = self.config['user_output']['twilio']['auth_token']
        self.twilio_client = Client(account_sid, auth_token)
        self.logger.debug('Twilio client set up')
