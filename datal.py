#!/usr/bin/env python3

import time
import argparse

from Lexer import *
from Parser import *
from Compiler import *
from Assembler import *

def compile(source, output=None, verbose=False):
    print("Tokenizing... ", end="", flush=True)
    lexer = Lexer(source)
    lexer_result = lexer.tokenize()
    if(lexer_result.error):
        print(lexer_result.error)
        exit(1)
    tokens = lexer_result.result
    print("Done")

    if(verbose): print(f"Tokens: {tokens}")

    print("Parsing... ", end="", flush=True)
    parser = Parser(tokens)
    parse_result = parser.parse()
    if(parse_result.error):
        print(parse_result.error)
        exit(1)
    ast = parse_result.result
    print("Done")

    if(verbose): print(f"AST: {ast}")

    print("Compiling... ", end="", flush=True)
    compiler = Compiler(ast)
    compile_result = compiler.compile()
    if(parse_result.error):
        print(compile_result.error)
        exit(1)
    asm_code = compile_result.result
    open("temp.asm", "w").write(asm_code)
    print("Done")

    print("Assembling... ", end="", flush=True)
    assembler = Assembler(asm_code, output=output)
    assembler.assemble()
    print("Done")

    print()
    print("Compiled successfully")


if(__name__ == "__main__"):
    argument_parser = argparse.ArgumentParser(description="Datal programming language compiler")
    argument_parser.add_argument("input", help="Path to the source file to compile")
    argument_parser.add_argument("-o", help="Compiled output path", metavar="FILE", dest='output')
    argument_parser.add_argument("-v", "--verbose", help="Turn on verbose/debug mode for compiler", action="store_true")
    args = argument_parser.parse_args()

    source = open(args.input, "r").read()

    compile(source, output=args.output, verbose=args.verbose)