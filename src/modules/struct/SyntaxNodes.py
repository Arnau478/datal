class Node:
    class Stmt:
        class Definition:
            def __init__(self, target_tok, type, value):
                self.target_tok = target_tok
                self.type = type
                self.value = value
            
            def __repr__(self):
                return f"DEF({self.target_tok}, {self.type}, {self.value})"

        class Function:
            def __init__(self, argdefs, type):
                self.argdefs = argdefs
                self.type = type
            
            def __repr__(self):
                return f"FUN({self.argdefs}, {self.type})"

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
