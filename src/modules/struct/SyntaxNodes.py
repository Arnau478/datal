class Node:
    class Stmt:
        class Function:
            def __init__(self, fun_name, argdefs, type, body):
                self.fun_name = fun_name
                self.argdefs = argdefs
                self.type = type
                self.body = body
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "fun_name": self.fun_name,
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
        class If:
            def __init__(self, condition, body, body_else):
                self.condition = condition
                self.body = body
                self.body_else = body_else
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "condition": self.condition,
                    "body": self.body,
                    "body_else": self.body_else,
                }.__repr__()

    class Expr:
        class Logical:
            def __init__(self, left, op, right):
                self.left = left
                self.op = op
                self.right = right
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "left": self.left,
                    "op": self.op,
                    "right": self.right,
                }.__repr__()
        class Binary:
            def __init__(self, left, op, right):
                self.left = left
                self.op = op
                self.right = right
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "left": self.left,
                    "op": self.op,
                    "right": self.right,
                }.__repr__()
        class Unary:
            def __init__(self, op, right):
                self.op = op
                self.right = right
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "op": self.op,
                    "right": self.right,
                }.__repr__()
        class Literal:
            def __init__(self, val):
                self.val = val
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "val": self.val,
                }.__repr__()
        class VarAccess:
            def __init__(self, var):
                self.var = var
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "var": self.var,
                }.__repr__()
        class Call:
            def __init__(self, callee, args):
                self.callee = callee
                self.args = args
            
            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "callee": self.callee,
                    "args": self.args,
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
    
    class Program:
            def __init__(self, functions):
                self.functions = functions

            def __repr__(self):
                return {
                    "name": self.__class__.__name__,
                    "functions": self.functions,
                }.__repr__()
