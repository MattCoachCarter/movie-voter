import unittest
from unittest.mock import patch

from movie_voter.user_input_service import UserInputService
from movie_voter.movie_voter import MovieVoter
 
class TestBasicFunction(unittest.TestCase):
    @patch.object(MovieVoter, 'accept_user_input')
    @patch.object(UserInputService, 'setup_backend')
    def test_on_user_input(self, setup_backend_patched, accept_user_input_patched):
        user_input = {'a': 'b'}
        mv = MovieVoter({})
        config = {'user_input': {'backend': 'invalid'}}
        uis = UserInputService(config, mv)
        uis.started = True
        uis.on_user_input(user_input)
        accept_user_input_patched.assert_called_once_with(user_input)

    @patch.object(UserInputService, 'setup_backend')
    def test_on_user_input_not_started(self, setup_backend_patched):
        user_input = {'a': 'b'}
        config = {'user_input': {'backend': 'invalid'}}
        uis = UserInputService(config, None)
        with self.assertRaises(RuntimeError):
            uis.on_user_input(user_input)

    def test_setup_backend_invalid(self):
        config = {'user_input': {'backend': 'invalid'}}
        with self.assertRaises(RuntimeError):
            uis = UserInputService(config, None)
 
    @patch.object(UserInputService, 'setup_backend')
    def test_setup_backend(self, setup_backend_patched):
        backend_str = 'backend'
        config = {'user_input': {'backend': backend_str}}
        uis = UserInputService(config, None)
        setup_backend_patched.assert_called_once_with(backend_str)

    
    def test_start_backend(self):
        config = {'user_input': {'backend': 'twilio'}}
        uis = UserInputService(config, None)
        with patch.object(uis.backend, 'start') as backend_start_patched:
            uis.start_backend()
            assert backend_start_patched.called

 
if __name__ == '__main__':
    unittest.main()