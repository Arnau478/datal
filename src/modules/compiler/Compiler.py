import __main__
import os

from modules.compiler.CompileResult import *
from modules.compiler.Namer import *
from modules.struct.TokenType import *
from modules.struct.SyntaxNodes import *

class Compiler:
    def __init__(self, ast, verbose=False):
        self.ast = ast
        self.verbose = verbose
        self.code = ""
        self.data = ""
    
    def get_stdlib(self):
        src_path = os.path.dirname(os.path.realpath(__main__.__file__)) # Get path to src/ directory
        stdlib_path = f"{src_path}/asm/x86/linux/io.asm"
        stdlib = open(stdlib_path).read()
        return stdlib

    def compile(self):
        self.visit(self.ast)

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
        result += "\t\tcall _f_main\n"
        result += "\t\tmov rax, 0\n"
        result += "\t\tret\n"
        result += self.code
        result += "section .data\n"
        result += self.data

        return CompileResult(result=result)
    
    def visit(self, node):
        handler = getattr(self, f"visit_node_{node.__class__.__name__}", None)
        if(handler == None):
            self.code += "{ CRASHED HERE }\n"
            print("\n[UNEXPECTED ERROR]")
            print(f"\tNo visitor handler for type '{node.__class__.__name__}'")
            print("\tPlease open a issue on https://github.com/Arnau478/datal/issues")
            if(self.verbose):
                print("Generated code:")
                print(self.code)
                print("Generated data:")
                print(self.data)
            exit(1)
        if(self.verbose): print(f"Compiler calling '{handler.__name__}'...")
    
        return handler(node)

    def visit_node_Function(self, node: Node.Stmt.Function):
        end_id = f"_i_end_{gen_id()}"
        
        self.code += f"\t_f_{node.fun_name.value}:\n"
        self.code += f"\t\tpop r15\n"
        self.visit(node.body)

    def visit_node_Block(self, node: Node.Stmt.Block):
        for stmt in node.statements:
            self.visit(stmt)

    def visit_node_If(self, node: Node.Stmt.If):
        then_id = f"_i_then_{gen_id()}"
        else_id = f"_i_else_{gen_id()}"
        end_id = f"_i_end_{gen_id()}"

        self.visit(node.condition)
        self.code += f"\t\tpop rax\n"
        self.code += f"\t\tcmp rax, 0\n"
        self.code += f"\t\tjnz {then_id}\n"
        self.code += f"\t\tjmp {else_id}\n"
        self.code += f"\t{then_id}:\n"
        self.visit(node.body)
        self.code += f"\t\tjmp {end_id}\n"
        self.code += f"\t{else_id}:\n"
        self.visit(node.body_else)
        self.code += f"\t{end_id}:\n"

    def visit_node_Logical(self, node: Node.Expr.Logical):
        self.visit(node.left)
        self.visit(node.right)
        self.code += f"\t\tpop rax\n"
        self.code += f"\t\tpop rbx\n"
        if(node.op.type == TokenType.AND): self.code += f"\t\tand rax, rbx\n"
        else: raise Exception()
        self.code += f"\t\tpush rax\n"

    def visit_node_Binary(self, node: Node.Expr.Binary):
        yes_id = f"_i_yes_{gen_id()}"
        no_id = f"_i_no_{gen_id()}"
        end_id = f"_i_end_{gen_id()}"

        self.visit(node.left)
        self.visit(node.right)
        self.code += f"\t\tpop rax\n"
        self.code += f"\t\tpop rbx\n"
        self.code += f"\t\tcmp rax, rbx\n"
        self.code += f"\t\tje {yes_id}\n"
        self.code += f"\t\tjmp {no_id}\n"
        self.code += f"\t{yes_id}:\n"
        self.code += f"\t\tpush 1\n"
        self.code += f"\t\tjmp {end_id}\n"
        self.code += f"\t{no_id}:\n"
        self.code += f"\t\tpush 0\n"
        self.code += f"\t{end_id}:\n"

        if(node.op.type == TokenType.EQ_EQ): pass
        else: raise Exception()
    
    def visit_node_Literal(self, node: Node.Expr.Literal):
        if(node.val.type == TokenType.STRING):
            id = f"LIT_STR_{gen_id()}"
            self.data += f"{id}: db \"{node.val.value}\", 0\n"
            self.code += f"\t\tpush {id}\n"
        elif(node.val.type == TokenType.NUMBER):
            self.code += f"\t\tpush {node.val.value}\n"
        else:
            raise Exception()
    
    def visit_node_Call(self, node: Node.Expr.Call):
        for arg in node.args:
            self.visit(arg)
        self.code += f"\t\tcall _f_{node.callee.var.value}\n"
    
    def visit_node_Return(self, node: Node.Stmt.Return):
        self.code += f"\t\tret\n"
