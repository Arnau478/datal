import os

class Assembler:
    def __init__(self, asm_code, output=None):
        self.asm_code = asm_code
        self.output = output
    
    def assemble(self):
        if(not os.path.exists("/tmp/datal/")): os.mkdir("/tmp/datal/")
        open("/tmp/datal/temp.asm", "w").write(self.asm_code)
        if(os.system("nasm -f elf64 /tmp/datal/temp.asm -o /tmp/datal/temp.o") != 0): return
        if(os.system(f"gcc -no-pie -m64 -o {self.output} /tmp/datal/temp.o") != 0): return
