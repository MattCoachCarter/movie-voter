from .user_output_backend_base import UserOutputBackendBase
from time import sleep

from movie_voter.utils import get_logger


class StdoutUserOutputBackend(UserOutputBackendBase):
    """Base class for the user output backend classes
    """

    def __init__(self, config):
        super(StdoutUserOutputBackend, self).__init__(config)
        self.logger = get_logger('StdoutUserOutputBackend')
        self.logger.debug('Constructing')

    def send_output(self, user_id, output_to_send):
        """OVERRIDES send_output from the base class
        """
        total_output_str = '@{}: {}'.format(user_id, output_to_send)
        print(total_output_str)

    def run(self):
        """OVERRIDES run from the base class
        """
        self.running = True
        while self.running:
            time.sleep(self.config['user_output']['sleep_interval'])
