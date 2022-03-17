extern printf

section .text
    _f_print:
        pop rax
        pop rdi
        push rax
        push rbp
        xor rsi, rsi
        xor rax, rax
        call printf
        pop rbp
        ret
