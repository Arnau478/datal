import json

class Node:
    class Stmt:
        class Function:
            def __init__(self, name, argdefs, type, body):
                self.name = name
                self.argdefs = argdefs
                self.type = type
                self.body = body
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "argdefs": self.argdefs,
                    "type": self.type,
                    "body": self.body,
                }.__repr__()
        class Definition:
            def __init__(self, def_name, type):
                self.def_name = def_name
                self.type = type
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "def_name": self.def_name,
                    "type": self.type,
                }.__repr__()
        class Return:
            def __init__(self):
                pass
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                }.__repr__()
        class Block:
            def __init__(self, statements):
                self.statements = statements
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "statements": self.statements,
                }.__repr__()

    class Type:
        class Simple:
            def __init__(self, id):
                self.id = id

            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "id": self.id,
                }.__repr__()

        class Parameterized:
            def __init__(self, id, args):
                self.id = id
                self.args = args

            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "id": self.id,
                    "args": self.args,
                }.__repr__()
