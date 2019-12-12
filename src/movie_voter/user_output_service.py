from threading import Thread

class UserOutputService(Thread):
    def __init__(self, backend_type, movie_voter):
        Thread.__init__(self)
        self.setup_backend(backend_type)

    def on_user_input(self, input_data_dict):
        """Take in/process user input
        :param input_data_dict: A dictionary containing the following data:
                                type: a string denoting the type of input
                                user: a string that will uniquely identify a
                                      user
                                value: a string representing the value of the
                                       user input
        """
        pass  # TODO


    def setup_backend(self, backend_type):
        """Set up the backend user input service
        """
        self.backend = None

        if backend_type == "twilio":
            pass # TODO
        else:
            raise RuntimeError('Unrecognized backend type: {}, currently '
                'twilio is the only supported backend'.format(backend_type))

    def start_backend(self):
        pass # TODO

    def run(self):
        """Run the thread, to invoke run start()
        """
        self.start_backend()
