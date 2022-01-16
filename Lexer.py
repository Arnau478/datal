from Token import *
from TokenType import *
from LexicError import *
from LexerResult import *

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#TODO: Implement lower-case ALPHA
ALPHA = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

class Lexer:
    def __init__(self, source):
        self.source = source
        self.current_char = None
        self.next_char = None
        self.idx = -1
        self.line = 1
        self.advance()

    def tokenize(self):
        tokens = []

        while(self.current_char):
            if(self.current_char in [" ", "\n", "\r", "\t"]): # Irrelevant character, ignore it
                self.advance()
            elif(self.current_char == "+"):
                tokens.append(Token(TokenType.PLUS, self.line))
                self.advance()
            elif(self.current_char == "-"):
                tokens.append(Token(TokenType.MINUS, self.line))
                self.advance()
            elif(self.current_char == "*"):
                tokens.append(Token(TokenType.MUL, self.line))
                self.advance()
            elif(self.current_char == "/"):
                tokens.append(Token(TokenType.DIV, self.line))
                self.advance()
            elif(self.current_char == ">"):
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TokenType.GREATER_EQ, self.line))
                    self.advance()
                else:
                    tokens.append(Token(TokenType.GREATER, self.line))
            elif(self.current_char == "<"):
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TokenType.LESS_EQ, self.line))
                    self.advance()
                else:
                    tokens.append(Token(TokenType.LESS, self.line))
            elif(self.current_char == "="):
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TokenType.EQ_EQ, self.line))
                    self.advance()
                else:
                    tokens.append(Token(TokenType.EQ, self.line))
            elif(self.current_char == "!"):
                self.advance()
                if(self.current_char == "="):
                    tokens.append(Token(TokenType.NOT_EQ, self.line))
                    self.advance()
                else:
                    tokens.append(Token(TokenType.NOT, self.line))
            elif(self.current_char == "\""):
                self.advance()

                s = ""

                while(self.current_char != "\"" and self.current_char):
                    s += self.current_char
                    self.advance()
                
                if(self.current_char == None):
                    return LexerResult(LexicError("Unterminated string", self.line))

                self.advance()

                tokens.append(Token(TokenType.STRING, self.line, value=s))
            elif(self.current_char in DIGITS):
                number_s = ""

                while(self.current_char in DIGITS):
                    number_s += self.current_char
                    self.advance()
                
                if(self.current_char == "." and self.next_char in DIGITS):
                    number_s += self.current_char
                    self.advance()
                    while(self.current_char in DIGITS):
                        number_s += self.current_char
                        self.advance()

                tokens.append(Token(TokenType.NUMBER, self.line, value=number_s))
            elif(self.current_char in ALPHA):
                pass
            else:
                return LexerResult(error=LexicError(f"Unexpected character {self.current_char}", self.line))

        tokens.append(Token(TokenType.EOF, self.line))

        return LexerResult(result=tokens)

    def advance(self):
        if(self.idx < len(self.source)-1):
            self.idx += 1
            self.current_char = self.source[self.idx]
            if(self.idx < len(self.source)-1):
                self.next_char = self.source[self.idx + 1]
            if(self.current_char == '\n'): self.line += 1
        else:
            self.current_char = None
            self.next_char = None
        