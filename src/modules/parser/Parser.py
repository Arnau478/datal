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

    def parse(self):
        while(self.current_tok.type != TokenType.EOF and self.current_tok != None):
            if(self.current_tok.type == TokenType.IDENTIFIER and self.next_tok.type == TokenType.EQ):
                definition = self.par_definition()
                if(definition.error): return definition
                return ParseResult(definition.result)
            else:
                return ParseResult(error=ParseError("Expected definition", self.line))

    def par_expression(self):
        lam = self.par_lambda()
        if(lam.error): return lam
        return ParseResult(lam.result)
    
    def par_lambda(self):
        args = []

        if(self.current_tok.type != TokenType.LPAREN):
            return ParseResult(error=ParseError("Expected '('", self.line))
        
        self.advance() # Advance '('

        while(self.current_tok.type != TokenType.RPAREN and self.current_tok.type != TokenType.EOF):
            if(self.current_tok.type == TokenType.EOF): # Unclosed parenthesis
                return ParseResult(error=ParseError("Expected ')'", self.line))
            
            if(self.current_tok.type == TokenType.COMMA):
                self.advance()

            # TODO: Test if this works with no arguments
            if(self.current_tok.type != TokenType.IDENTIFIER): # If not an identifier
                return ParseResult(error=ParseError("Expected identifier", self.line))
            
            argname = self.current_tok # Save argument name token
            self.advance() # Consume identifier

            if(self.current_tok.type != TokenType.COLON): # Unclosed parenthesis
                return ParseResult(error=ParseError("Expected ':'", self.line))
            self.advance()

            argtype = self.par_type()
            if(argtype.error): return argtype

            node = Node.Stmt.Definition(argname, argtype.result, None)

            args.append(node)
        
        self.advance() # Advance ')'
        if(self.current_tok.type != TokenType.COLON):
            return ParseResult(error=ParseError("Expected ':'", self.line))
        
        self.advance()
        
        ret = self.par_type()

        if(ret.error): return ret

        return ParseResult(Node.Stmt.Function(args, ret.result))
    
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

    def par_definition(self):
        id = self.current_tok
        self.advance()
        if(self.current_tok.type != TokenType.EQ):
            return ParseResult(error=ParseError("Expected '='", self.line))
        self.advance()
        
        expr = self.par_expression()
        if(expr.error): return expr
        return ParseResult(Node.Stmt.Definition(id, None, expr.result)) # TODO: FIX THIS
