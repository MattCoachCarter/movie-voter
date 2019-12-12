from .state_output_backend_base import StateOutputBackendBase

from movie_voter.utils import get_logger

class JSONFileStateOutputBackend(StateOutputBackendBase):
    """Class to output state to as JSON to a file
    """

    def __init__(self, config):
        super(JSONFileStateOutputBackend, self).__init__(config)
        self.logger = get_logger('JSONFileStateOutputBackend')
        self.logger.debug('Constructing')
        self.file_path = self.config['state_output']['json_file']

    def format_state(self, state_dict):
        """OVERRIDE of format_state in base class
        """
        self.logger.debug('Formatting state')
        state_str = 'STATE:'
        for k, v in state_dict.items():
            state_str += '\n    {}: {}'.format(k, v)
        return json.dumps(state_dict, indent=4, sort_keys=True)

    def output_state(self, formatted_state):
        """OVERRIDE of output_state in base class
        """
        self.logger.info('Outputting state to file: {}'.format(
            self.file_path))
        with open(self.file_path, 'w') as f:
            f.write(str(formatted_state))
