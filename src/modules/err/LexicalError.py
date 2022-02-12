from modules.err.Error import *

class LexicalError(Error):
    def __init__(self, message, line):
        super().__init__(__name__, message, line)

    def __repr__(self): return super().__repr__()
