import __main__
import os

from modules.compiler.CompileResult import *
from modules.struct.TokenType import *
from modules.struct.SyntaxNodes import *

class Compiler:
    def __init__(self, ast):
        self.ast = ast
    
    def get_stdlib(self):
        datal_path = os.path.realpath(__main__.__file__) # Get datal.py file path
        src_path = os.path.dirname(datal_path) # Get path to src/ directory
        stdlib_path = f"{src_path}/asm/x86/linux/stdlib.asm"
        stdlib = open(stdlib_path).read()
        return stdlib

    def compile(self):
        stdlib = self.get_stdlib()

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
        result += "\n"
        result += "\t\t; exit\n"
        result += "\t\tcall _exit\n"

        return CompileResult(result=result)
    
    def visit(self, node):
        try:
            handler = getattr(self, f"visit_node_{node.__class__.__name__}")
        
            return handler(node)
            
        except AttributeError:
            print("UNEXPECTED ERROR")
            print(f"No visitor handler for type {node.__class__.__name__}")
            exit(1)

    def visit_node_Function(self, node: Node):
        code = ""

        self.visit(node.body)

        self.visit(node)

