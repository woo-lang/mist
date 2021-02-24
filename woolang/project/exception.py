from clint.textui import colored
import sys as sys

class FileNotFoundException(object):
    def __init__(self, filename, exception_message):
        self.filename = file

        self.exception_message = exception_message

    def evoke_exception_message(self, exit_=True):
        print(colored.red(
            f"FileNotFoundException:{self.exception_message}"
        ))

        
