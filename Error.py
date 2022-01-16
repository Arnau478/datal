class Error:
    def __init__(self, type, message, line=None):
        self.type = type
        self.message = message
        self.line = line
    
    def __repr__(self):
        error = '\x1b[31mERROR\x1b[0m '

        if(self.line):
            error += f'[line {self.line}] '
        
        error += f'{self.type}'

        if(self.message):
            error += f': {self.message}'

        return error