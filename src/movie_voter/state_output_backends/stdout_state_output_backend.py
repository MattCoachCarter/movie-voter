from .state_output_backend_base import StateOutputBackendBase

from movie_voter.utils import get_logger

class StdoutStateOutputBackend(StateOutputBackendBase):
    """Class to output state to stdout
    """

    def __init__(self, config):
        super(StdoutStateOutputBackend, self).__init__(config)
        self.logger = get_logger('StdoutStateOutputBackend')
        self.logger.debug('Constructing')

    def format_state(self, state_dict):
        """OVERRIDE of format_state in base class
        """
        self.logger.debug('Formatting state')
        state_str = 'STATE:'
        for k, v in state_dict.items():
            state_str += '\n    {}: {}'.format(k, v)
        return state_str

    def output_state(self, formatted_state):
        """OVERRIDE of output_state in base class
        """
        self.logger.info('Outputting state to stdout')
        print(str(formatted_state))
