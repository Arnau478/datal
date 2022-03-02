class Node:
    class Stmt:
        class Function:
            def __init__(self, name, argdefs, type, body):
                self.name = name
                self.argdefs = argdefs
                self.type = type
                self.body = body
            
            def __repr__(self):
                return f"FUN({self.name}, {self.type}, {self.argdefs}, {self.body})"
        class Definition:
            def __init__(self, name, type):
                self.name = name
                self.type = type
            
            def __repr__(self):
                return f"DEF({self.name}, {self.type})"

    class Type:
        class Simple:
            def __init__(self, id):
                self.id = id

            def __repr__(self):
                return f"S_TYPE({self.id})"

        class Parameterized:
            def __init__(self, id, args):
                self.id = id
                self.args = args

            def __repr__(self):
                return f"P_TYPE({self.id}, {self.args})"
