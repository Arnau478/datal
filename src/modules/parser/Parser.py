from modules.struct.TokenType import *
from modules.err.ParseError import *
from modules.parser.ParseResult import *
from modules.struct.SyntaxNodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_tok = None
        self.next_tok = None
        self.idx = -1
        self.line = 0
        self.advance()

    def advance(self):
        if(self.idx < len(self.tokens)):
            self.idx += 1
            self.current_tok = self.tokens[self.idx]
            if(self.idx < len(self.tokens)-1):
                self.next_tok = self.tokens[self.idx+1]
            else:
                self.next_tok = None
            self.line = self.current_tok.line
        else:
            self.current_tok = None
            self.next_tok = None
        
    def advance_n(self, num):
        for i in range(num):
            self.advance()
    
    def match(self, type, value=None):
        return self.current_tok.type == type and (self.current_tok.value == value or value == None)

    def parse(self):
        while(self.current_tok.type != TokenType.EOF and self.current_tok != None):
            if(self.current_tok.type == None):
                return ParseResult(error=ParseError("Unexpected error ocurred", self.line))
            fun = self.par_function()
            return fun
    
    def par_type(self):
        if(self.next_tok.type == TokenType.LESS): # Parametrized
            args = []
            id = self.current_tok

            self.advance_n(2) # Advance id and '<'

            while(self.current_tok.type != TokenType.GREATER):
                if(self.current_tok.type == TokenType.EOF):
                    return ParseResult(error=ParseError("Expected '>'", self.line))
                if(self.current_tok.type == TokenType.COMMA):
                    self.advance() # Advance ','
                
                type = self.par_type()
                if(type.error): return type
                args.append(type.result)
                
            node = Node.Type.Parameterized(id, args)
            self.advance() # Advance '>'
            return ParseResult(node)
        node = Node.Type.Simple(self.current_tok)
        self.advance()
        return ParseResult(node)
    
    def par_function(self):
        if(not self.match(TokenType.KEYWORD, "fun")):
            return ParseResult(error=ParseError("Expected function declaration", self.line))
        self.advance()

        if(not self.match(TokenType.IDENTIFIER)):
            return ParseResult(error=ParseError("Expected identifier", self.line))
        fun_name = self.current_tok
        self.advance()

        if(not self.match(TokenType.COLON)):
            return ParseResult(error=ParseError("Expected ':'", self.line))
        self.advance()


        fun_type = self.par_type()
        if(fun_type.error): return fun_type
        fun_type = fun_type.result

        if(not self.match(TokenType.LPAREN)):
            return ParseResult(error=ParseError("Expected '('", self.line))
        self.advance()

        argdefs = []

        while(not (self.match(TokenType.RPAREN) or (self.current_tok == None))):
            if(not self.match(TokenType.IDENTIFIER)):
                return ParseResult(error=ParseError("Expected identifier", self.line))
            name = self.current_tok
            self.advance()

            if(not self.match(TokenType.COLON)):
                return ParseResult(error=ParseError("Expected ':'", self.line))
            self.advance()

            type = self.par_type()
            if(type.error): return type
            type = type.result

            if(not self.match(TokenType.RPAREN)):
                if(not self.match(TokenType.COMMA)):
                    print(self.current_tok)
                    return ParseResult(error=ParseError("Expected ','", self.line))
                self.advance()

            argdefs.append(Node.Stmt.Definition(name, type))

        return ParseResult(Node.Stmt.Function(fun_name, argdefs, fun_type, None))
