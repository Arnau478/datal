from modules.struct.Token import *
from modules.struct.TokenType import *
from modules.err.LexicalError import *
from modules.lexer.LexerResult import *

keywords = [
    'fun',
    'return',
    'if',
    'else',
    'for',
    'while',
]

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
            elif(self.current_char == "/" and self.next_char == "/"):
                while(self.current_char != "\n" and self.current_char != None):
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
            elif(self.current_char == "("):
                tokens.append(Token(TokenType.LPAREN, self.line))
                self.advance()
            elif(self.current_char == ")"):
                tokens.append(Token(TokenType.RPAREN, self.line))
                self.advance()
            elif(self.current_char == "{"):
                tokens.append(Token(TokenType.LBRACE, self.line))
                self.advance()
            elif(self.current_char == "}"):
                tokens.append(Token(TokenType.RBRACE, self.line))
                self.advance()
            elif(self.current_char == ":"):
                tokens.append(Token(TokenType.COLON, self.line))
                self.advance()
            elif(self.current_char == ";"):
                tokens.append(Token(TokenType.SEMI, self.line))
                self.advance()
            elif(self.current_char == ","):
                tokens.append(Token(TokenType.COMMA, self.line))
                self.advance()
            elif(self.current_char == "|" and self.next_char == "|"):
                tokens.append(Token(TokenType.OR, self.line))
                self.advance()
                self.advance()
            elif(self.current_char == "&" and self.next_char == "&"):
                tokens.append(Token(TokenType.AND, self.line))
                self.advance()
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
                    if(self.current_char == "\\"):
                        self.advance()
                        if(self.current_char == "\\"):
                            s += "\\"
                        elif(self.current_char == "n"):
                            s += "\n"
                        else:
                            return LexerResult(error=LexicalError(f"Non-existing escape code '\\{self.current_char}'", self.line))
                    else:
                        s += self.current_char
                    self.advance()
                
                if(self.current_char == None):
                    return LexerResult(error=LexicalError("Unterminated string", self.line))

                self.advance()

                tokens.append(Token(TokenType.STRING, self.line, value=s))
            elif(self.current_char.isnumeric()):
                number_s = ""

                while(self.current_char.isnumeric()):
                    number_s += self.current_char
                    self.advance()
                
                if(self.current_char == "." and self.next_char.isnumeric()):
                    number_s += self.current_char
                    self.advance()
                    while(self.current_char.isnumeric()):
                        number_s += self.current_char
                        self.advance()

                tokens.append(Token(TokenType.NUMBER, self.line, value=number_s))
            elif(self.current_char.isalpha()):
                name = self.current_char
                self.advance()
                while (self.current_char.isalpha() or self.current_char == "_"):
                    name += self.current_char
                    self.advance()
                
                if(name in keywords):
                    tokens.append(Token(TokenType.KEYWORD, self.line, value=name))
                else:
                    tokens.append(Token(TokenType.IDENTIFIER, self.line, value=name))
            else:
                return LexerResult(error=LexicalError(f"Unexpected character {self.current_char}", self.line))

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
        