import json
import signal
import sys

from movie_voter.movie_voter import MovieVoter


def read_config(path_to_config):
    with open(path_to_config, 'r') as f:
        return json.load(f)


def signal_handler(signal_received, frame):
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    global movie_voter_obj
    movie_voter_obj.stop()

if __name__ == '__main__':
    global movie_voter_obj
    if len(sys.argv) != 2:
        print('Usage: {} <path_to_config.json>'.format(sys.argv[0]))
        sys.exit(1)

    signal.signal(signal.SIGINT, signal_handler)

    movie_voter_obj = MovieVoter(read_config(sys.argv[1]))
    movie_voter_obj.start()
