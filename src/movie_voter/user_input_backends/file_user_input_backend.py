import os
from time import sleep

from .user_input_backend_base import UserInputBackendBase
from movie_voter.utils import get_logger

class FileUserInputBackend(UserInputBackendBase):
    """Class to handle user input from a file
    """
    SPLIT_KEY = '::'

    def __init__(self, config, user_input_service):
        super(FileUserInputBackend, self).__init__(config, user_input_service)
        self.logger = get_logger('FileUserInputBackend')
        self.logger.debug('Constructing')
        self.last_input_str_seen = None

    def get_file_contents(self):
        """Get and return the file contents of the configured input file
        """
        contents = None
        file_path = self.config['user_input']['file_path']
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                contents = f.read()
        return contents

    def check_file_contents(self):
        """Get the contents of the configured file and compare it to the last
        input we've seen, if it is new then send the input up the chain
        """
        contents = self.get_file_contents()
        if contents is not None and contents != self.last_input_str_seen:
            self.last_input_str_seen = str(contents)
            self.logger.info('Got new user input file contents: {}'.format(
                self.last_input_str_seen))
            if FileUserInputBackend.SPLIT_KEY in self.last_input_str_seen:
                split = self.last_input_str_seen.split(
                    FileUserInputBackend.SPLIT_KEY)
                self.user_input_service.on_user_input({'user': split[0],
                                                       'value': split[1]})
            else:
                self.logger.error('New input file contents invalid')

    def run(self):
        """OVERRIDE of run in base class
        """
        self.running = True
        self.logger.info('Running')
        while self.running:
            self.check_file_contents()
            sleep(self.config['user_input']['sleep_interval'])

