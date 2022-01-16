extern printf

section .data
    printf_format_int db "%d", 10, 0

section .text
    global _start

    ; Print an integer
    _print_int:
        mov rdi, printf_format_int
        pop r11
        pop rsi
        push r11
        xor rax, rax
        call printf
        ret
    
    ; Exit the program
    _exit:
        mov rax, 60	; exit
        mov rdi, 0
        syscall

    ; Add the two higher values on stack and push the result to stack
    _add:
        pop rcx
        pop rbx
        pop rax
        add rax, rbx
        push rax
        push rcx
        ret

    ; Subtract the two higher values on stack and push the result to stack
    _subtract:
        pop rcx
        pop rbx
        pop rax
        sub rax, rbx
        push rax
        push rcx
        ret

    ; Multiply the two higher values on stack and push the result to stack
    _multiply:
        pop rbx
        pop rax
        pop rcx
        mul rcx
        push rax
        push rbx
        ret

    ; Divide the two higher values on stack and push the result to stack
    _divide:
        pop rbx
        mov rdx, 0
        pop rcx
        pop rax
        div rcx
        push rax
        push rbx
        ret

    ; Negate the number on top of the stack (the same as 0-num)
    _negate_number:
        pop rbx
        pop rax
        neg rax
        push rax
        push rbx
        ret
    
    ; Check if a nuber is greater than another
    _greater:
        pop rdx
        pop rbx
        pop rax
        cmp rax, rbx
        jg .return_true
        jmp .return_false
    .return_true:
        push 1
        jmp .end
    .return_false:
        push 0
        jmp .end
    .end:
        push rdx
        ret
    
    ; Check if a nuber is greater or equal than another
    _greater_eq:
        pop rdx
        pop rbx
        pop rax
        cmp rax, rbx
        jge .return_true
        jmp .return_false
    .return_true:
        push 1
        jmp .end
    .return_false:
        push 0
        jmp .end
    .end:
        push rdx
        ret
    
    ; Check if a nuber is less than another
    _less:
        pop rdx
        pop rbx
        pop rax
        cmp rax, rbx
        jl .return_true
        jmp .return_false
    .return_true:
        push 1
        jmp .end
    .return_false:
        push 0
        jmp .end
    .end:
        push rdx
        ret
    
    ; Check if a nuber is less or equal than another
    _less_eq:
        pop rdx
        pop rbx
        pop rax
        cmp rax, rbx
        jle .return_true
        jmp .return_false
    .return_true:
        push 1
        jmp .end
    .return_false:
        push 0
        jmp .end
    .end:
        push rdx
        ret
    
    ; Check if two numbers are equal
    _equal:
        pop rdx
        pop rbx
        pop rax
        cmp rax, rbx
        je .return_true
        jmp .return_false
    .return_true:
        push 1
        jmp .end
    .return_false:
        push 0
        jmp .end
    .end:
        push rdx
        ret
    
    ; Check if two numbers are not equal
    _not_equal:
        pop rdx
        pop rbx
        pop rax
        cmp rax, rbx
        jne .return_true
        jmp .return_false
    .return_true:
        push 1
        jmp .end
    .return_false:
        push 0
        jmp .end
    .end:
        push rdx
        ret