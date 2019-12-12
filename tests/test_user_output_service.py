import unittest
from unittest.mock import patch

from movie_voter.user_output_service import UserOutputService
 
class TestUserOutputService(unittest.TestCase):
    def test_send_output(self):
        config = {'user_output': {'backend': 'stdout'}}
        uos = UserOutputService(config)
        uos.started = True
        with patch.object(uos.backend, 'send_output') as backend_send_patched:
            uos.send_output('user_id', 'output')
            assert backend_send_patched.called
 
    @patch.object(UserOutputService, 'setup_backend')   
    def test_send_output_not_started(self, setup_backend_patched):
        config = {'user_output': {'backend': 'stdout'}}
        uos = UserOutputService(config)
        with self.assertRaises(RuntimeError):
            uos.send_output('user_id', 'output')

    def test_setup_backend_invalid(self):
        config = {'user_output': {'backend': 'invalid'}}
        with self.assertRaises(RuntimeError):
            uos = UserOutputService(config)
 
    @patch.object(UserOutputService, 'setup_backend')
    def test_setup_backend(self, setup_backend_patched):
        backend_str = 'backend'
        config = {'user_output': {'backend': backend_str}}
        uos = UserOutputService(config)
        setup_backend_patched.assert_called_once_with(backend_str)

    def test_start_backend(self):
        config = {'user_output': {'backend': 'stdout'}}
        uos = UserOutputService(config)
        with patch.object(uos.backend, 'start') as backend_start_patched:
            uos.start_backend()
            assert backend_start_patched.called

 
if __name__ == '__main__':
    unittest.main()