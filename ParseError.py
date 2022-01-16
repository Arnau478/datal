from Error import *

class ParseError(Error):
    def __init__(self, message, line):
        super().__init__(__name__, message, line)

    def __repr__(self): return super().__repr__()