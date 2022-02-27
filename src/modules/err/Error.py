class Error:
    def __init__(self, type, message, line=None):
        self.type = type
        self.message = message
        self.line = line
    
    def __repr__(self):
        error = '\x1b[31m\x1b[1mERROR\x1b[0m '

        if(self.line):
            error += f'\x1b[33m[line {self.line}]\x1b[0m '
        
        error += f'\x1b[1m{self.type}\x1b[0m'

        if(self.message):
            error += f': {self.message}'

        return error
