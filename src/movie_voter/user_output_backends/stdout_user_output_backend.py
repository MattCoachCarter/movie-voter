from .user_output_backend_base import UserOutputBackendBase
from time import sleep

from movie_voter.utils import get_logger


class StdoutUserOutputBackend(UserOutputBackendBase):
    """Class to send user output to stdout
    """

    def __init__(self, config):
        super(StdoutUserOutputBackend, self).__init__(config)
        self.logger = get_logger('StdoutUserOutputBackend')
        self.logger.debug('Constructing')

    def send_pending_output(self):
        """OVERRIDES send_pending_output from the base class
        """
        while len(self.pending_output) > 0:
            user_id, output_to_send = self.pending_output.pop(0)
            total_output_str = '@{}: {}'.format(user_id, output_to_send)
            print(total_output_str)
