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
        if(self.idx < len(self.tokens)-1):
            self.idx += 1
            self.current_tok = self.tokens[self.idx]
            if(self.idx < len(self.tokens)-2):
                self.next_token = self.tokens[self.idx + 1]
            self.line = self.current_tok.line
        else:
            self.current_tok = None
            self.next_tok = None

    def parse(self):
        return self.expression()

    def expression(self):
        return self.equality()
    
    def equality(self):
        return self.bin_op(self.comparison, [TokenType.EQ_EQ, TokenType.NOT_EQ])
    
    def comparison(self):
        return self.bin_op(self.term, [TokenType.GREATER, TokenType.GREATER_EQ, TokenType.LESS, TokenType.LESS_EQ])
    
    def term(self):
        return self.bin_op(self.factor, [TokenType.PLUS, TokenType.MINUS])
    
    def factor(self):
        return self.bin_op(self.unary, [TokenType.MUL, TokenType.DIV])
    
    def unary(self):
        if(self.current_tok.type in [TokenType.MINUS]):
            op_tok = self.current_tok
            self.advance()
            right = self.unary()
            if(right.error): return right
            right_node = right.result
            return ParseResult(result=Expr.Unary(op_tok, right_node))
        else:
            return self.atom()

    def atom(self):
        if(self.current_tok.type in [TokenType.NUMBER]):
            literal = Expr.Literal(self.current_tok)
            self.advance()
            return ParseResult(result=literal)
        return ParseResult(error=ParseError("Expected number literal", self.line))
    
    def bin_op(self, left, op_toks, right=None):
        if(right == None):
            right = left

        left_node = left();
        if(left_node.error): return left_node
        
        while(self.current_tok.type in op_toks):
            op_tok = self.current_tok
            self.advance()

            right_node = right()
            if(right_node.error): return right_node

            left_node = ParseResult(result=Expr.Binary(left_node.result, op_tok, right_node.result))
        
        return left_node
