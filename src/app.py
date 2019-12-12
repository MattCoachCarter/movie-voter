import json
import sys

from movie_voter.movie_voter import MovieVoter


def read_config(path_to_config):
    with open(path_to_config, 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    global movie_voter_obj
    movie_voter_obj = MovieVoter(read_config(sys.argv[1])).start()