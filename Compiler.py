from CompileResult import *
from TokenType import *

class Compiler:
    def __init__(self, ast):
        self.ast = ast

    def compile(self):
        stdlib = open("asm/x86/linux/stdlib.asm", "r").read()

        result = ""

        result += ";\n; STD Lib\n;\n"
        result += stdlib + "\n"
        result += "\n"
        result += ";\n; Program\n;\n"
        result += "\n"
        result += "global main\n"
        result += "\n"
        result += "section .text\n"
        result += "\tmain:\n"
        result += self.visit(self.ast)
        result += "\t\tcall _print_int\n"
        result += "\n"
        result += "\t\t; exit\n"
        result += "\t\tcall _exit\n"

        return CompileResult(result=result)
    
    def visit(self, node):
        return getattr(self, f"visit_node_{node.__class__.__name__}")(node)

    def visit_node_Binary(self, node):
        code = ""

        code += self.visit(node.left)
        code += self.visit(node.right)

        if(node.op_tok.type == TokenType.PLUS):
            code += "\t\tcall _add\n"
        elif(node.op_tok.type == TokenType.MINUS):
            code += "\t\tcall _subtract\n"
        elif(node.op_tok.type == TokenType.MUL):
            code += "\t\tcall _multiply\n"
        elif(node.op_tok.type == TokenType.DIV):
            code += "\t\tcall _divide\n"
        elif(node.op_tok.type == TokenType.GREATER):
            code += "\t\tcall _greater\n"
        elif(node.op_tok.type == TokenType.GREATER_EQ):
            code += "\t\tcall _greater_eq\n"
        elif(node.op_tok.type == TokenType.LESS):
            code += "\t\tcall _less\n"
        elif(node.op_tok.type == TokenType.LESS_EQ):
            code += "\t\tcall _less_eq\n"
        elif(node.op_tok.type == TokenType.EQ_EQ):
            code += "\t\tcall _equal\n"
        elif(node.op_tok.type == TokenType.NOT_EQ):
            code += "\t\tcall _not_equal\n"
        else:
            raise Exception(f"Undefined compiler case for binary operation '{node.op_tok.type}'")

        return code

    def visit_node_Unary(self, node):
        code = ""

        code += self.visit(node.right)

        if(node.op_tok.type == TokenType.MINUS):
            code += "\t\tcall _negate_number\n"
        else:
            raise Exception(f"Undefined compiler case for unary operation '{node.op_tok.type}'")

        return code

    def visit_node_Literal(self, node):
        code = ""

        code += f"\t\tpush {node.tok.value}\n"

        return code