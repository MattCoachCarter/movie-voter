import unittest
from unittest.mock import patch

from movie_voter.user_input_service import UserInputService
from movie_voter.user_output_service import UserOutputService
from movie_voter.state_output_service import StateOutputService
from movie_voter.movie_voter import MovieVoter
 
class TestMovieVoter(unittest.TestCase):
    @patch.object(MovieVoter, 'setup_user_input_service')
    @patch.object(MovieVoter, 'setup_user_output_service')
    @patch.object(MovieVoter, 'setup_state_output_service')
    def test_setup_services(self,
                            setup_state_output_service_patched,
                            setup_user_output_service_patched,
                            setup_user_input_service_patched):
        mv = MovieVoter({})
        mv.setup_services()
        assert setup_state_output_service_patched.called
        assert setup_user_output_service_patched.called
        assert setup_user_input_service_patched.called

    @patch.object(UserInputService, '__init__', return_value=None)
    @patch.object(UserOutputService, '__init__', return_value=None)
    @patch.object(StateOutputService, '__init__', return_value=None)
    @patch.object(UserInputService, 'start')
    @patch.object(UserOutputService, 'start')
    @patch.object(StateOutputService, 'start')
    def test_start(self,
                   state_output_service_start,
                   user_output_service_start,
                   user_input_service_start,
                   state_output_init_patched,
                   user_output_init_patched,
                   user_input_init_patched):
        mv = MovieVoter({})
        mv.start()
        assert state_output_init_patched.called
        assert user_output_init_patched.called
        assert user_input_init_patched.called
        assert state_output_service_start.called
        assert user_output_service_start.called
        assert user_input_service_start.called

    @patch.object(UserInputService, 'stop')
    @patch.object(UserOutputService, 'stop')
    @patch.object(StateOutputService, 'stop')
    @patch.object(UserInputService, '__init__', return_value=None)
    @patch.object(UserOutputService, '__init__', return_value=None)
    @patch.object(StateOutputService, '__init__', return_value=None)
    def test_stop(self,
                  init_patched_a,
                  init_patched_b,
                  init_patched_c,
                  state_output_service_stop,
                  user_output_service_stop,
                  user_input_service_stop):
        mv = MovieVoter({})
        mv.setup_services()
        mv.stop()
        assert state_output_service_stop.called
        assert user_output_service_stop.called
        assert user_input_service_stop.called

    def test_accept_user_input(self):
        assert False, 'Implement me!'

    def test_sanitize_value(self):
        mv = MovieVoter({})
        assert mv.sanitize_value('  asdf  ') == 'asdf'
        assert mv.sanitize_value('a  s d f') == 'a s d f'
        assert mv.sanitize_value('a.  s.d$f^') == 'a sdf'
        assert mv.sanitize_value('START  44') == 'START 44'

    @patch.object(UserOutputService, 'send_output')
    @patch.object(UserOutputService, '__init__', return_value=None)
    def test_send_output_to_user(self,
                                 init_patched,
                                 user_output_service_send_output):
        user_id = 'user_id'
        output = 'output_to_send'
        mv = MovieVoter({})
        mv.setup_user_output_service()
        mv.send_output_to_user(user_id, output)
        user_output_service_send_output.assert_called_once_with(user_id,
                                                                output)

    @patch.object(StateOutputService, 'save_state')
    @patch.object(StateOutputService, '__init__', return_value=None)
    def test_save_state(self, init_patched, state_output_service_save_state):
        state_dict = {'test': 'test'}
        mv = MovieVoter({})
        mv.state = state_dict
        mv.setup_state_output_service()
        mv.save_state()
        state_output_service_save_state.assert_called_once_with(state_dict)

    @patch.object(MovieVoter, 'save_state')
    def test_update_state(self, movie_voter_save_state):
        starting_state = {'test': 'test'}
        state_updates = {'a': 'b'}
        expected_state = starting_state
        expected_state.update(state_updates)
        mv = MovieVoter({})
        mv.state = starting_state
        mv.update_state(state_updates)
        assert mv.state == expected_state
        assert movie_voter_save_state.called

    @patch.object(UserInputService, '__init__', return_value=None)
    def test_setup_user_input_service(self, service_constructor):
        config = {'a': 'b'}
        mv = MovieVoter(config)
        mv.setup_user_input_service()
        service_constructor.assert_called_once_with(config, mv)

    @patch.object(UserOutputService, '__init__', return_value=None)
    def test_setup_user_output_service(self, service_constructor):
        config = {'a': 'b'}
        mv = MovieVoter(config)
        mv.setup_user_output_service()
        service_constructor.assert_called_once_with(config)

    @patch.object(StateOutputService, '__init__', return_value=None)
    def test_setup_state_output_service(self, service_constructor):
        config = {'a': 'b'}
        mv = MovieVoter(config)
        mv.setup_state_output_service()
        service_constructor.assert_called_once_with(config)


if __name__ == '__main__':
    unittest.main()