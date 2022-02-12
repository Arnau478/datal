class Token:
    def __init__(self, type, line, value=None):
        self.type = type
        self.value = value
        self.line = line
    
    def __repr__(self):
        if(self.value): return f'{self.type}:{self.value}'
        return f'{self.type}'