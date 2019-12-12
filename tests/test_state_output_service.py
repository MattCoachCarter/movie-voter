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

    def test_save_state(self):
        config = {'state_output': {'backend': 'stdout'}}
        sos = StateOutputService(config)
        state_data = {'a': 'b'}
        with patch.object(sos.backend, 'start') as backend_start_patched:
            with patch.object(sos.backend, 'save') as backend_save_patched:
                sos.start()
                sos.save_state(state_data)
                assert backend_start_patched.called
                backend_save_patched.assert_called_once_with(state_data)

    def test_save_state_before_start(self):
        config = {'state_output': {'backend': 'stdout'}}
        sos = StateOutputService(config)
        state_data = {'a': 'b'}
        with self.assertRaises(RuntimeError):
            sos.save_state(state_data)

    @patch.object(StateOutputService, 'setup_backend')
    @patch.object(StateOutputService, 'start_backend')
    def test_start(self, setup_backend_patched, start_backend_patched):
        config = {'state_output': {'backend': 'doesntmatter'}}
        sos = StateOutputService(config)
        sos.start()
        assert setup_backend_patched.called
        assert start_backend_patched.called

    
    def test_start_backend(self):
        config = {'state_output': {'backend': 'stdout'}}
        sos = StateOutputService(config)
        with patch.object(sos.backend, 'start') as backend_start_patched:
            sos.start_backend()
            assert backend_start_patched.called

 
if __name__ == '__main__':
    unittest.main()