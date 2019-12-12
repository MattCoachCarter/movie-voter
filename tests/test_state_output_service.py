import unittest
from unittest.mock import patch

from movie_voter.state_output_service import StateOutputService
from movie_voter.movie_voter import MovieVoter
 
class TestStateOutputService(unittest.TestCase):
    def test_setup_backend_invalid(self):
        config = {'state_output': {'backend': 'invalid'}}
        with self.assertRaises(RuntimeError):
            sos = StateOutputService(config)

    @patch.object(StateOutputService, 'setup_backend')
    def test_setup_backend(self, setup_backend_patched):
        backend_str = 'backend'
        config = {'state_output': {'backend': backend_str}}
        sos = StateOutputService(config)
        setup_backend_patched.assert_called_once_with(backend_str)

 
if __name__ == '__main__':
    unittest.main()