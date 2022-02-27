class ParseResult:
    def __init__(self, result=None, error=None):
        self.result = result
        self.error = error
    
    def __repr__(self):
        return f'Result = {self.result}\nError = {self.error}'
