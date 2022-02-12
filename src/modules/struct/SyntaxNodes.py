class Expr:
    class Binary:
        def __init__(self, left, op_tok, right):
            self.left = left
            self.op_tok = op_tok
            self.right = right
        
        def __repr__(self):
            return f"({self.left}, {self.op_tok}, {self.right})"

    class Unary:
        def __init__(self, op_tok, right):
            self.op_tok = op_tok
            self.right = right
        
        def __repr__(self):
            return f"({self.op_tok}, {self.right})"

    class Literal:
        def __init__(self, tok):
            self.tok = tok
        
        def __repr__(self):
            return f"{self.tok}"