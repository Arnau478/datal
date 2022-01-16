import os

class Assembler:
    def __init__(self, asm_code, output=None):
        self.asm_code = asm_code
        self.output = output
    
    def assemble(self):
        if(os.system("nasm -f elf64 temp.asm -o temp.o") != 0): return
        if(os.system(f"gcc -no-pie -m64 -o {self.output} temp.o") != 0): return