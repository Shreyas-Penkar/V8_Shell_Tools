import argparse

def c_to_javascript(c_shellcode):
    # Ensure the shellcode length is a multiple of 8
    if len(c_shellcode) % 8 != 0:
        c_shellcode += "\\x00"

    javascript_format = ""
    for i in range(2, len(c_shellcode) - 6, 8):
        tmp1 = c_shellcode[i:i+2]
        tmp2 = c_shellcode[i+4:i+6]
        javascript_format += f"\\u{tmp2}{tmp1}"
    
    return javascript_format

def javascript_to_c(js_shellcode):
    c_format = ""
    for i in range(2, len(js_shellcode) - 4, 6):
        tmp1 = js_shellcode[i:i+2]
        tmp2 = js_shellcode[i+2:i+4]
        c_format += f"\\x{tmp2}\\x{tmp1}"
    
    return c_format

def main():
    parser = argparse.ArgumentParser(description="Convert C shellcode to JavaScript and vice versa.")
    parser.add_argument('-c', '--c_shellcode', type=str, help='C shellcode to convert to JavaScript format')
    parser.add_argument('-j', '--js_shellcode', type=str, help='JavaScript shellcode to convert to C format')

    args = parser.parse_args()

    if args.c_shellcode:
        js_result = c_to_javascript(args.c_shellcode)
        print(f"JavaScript Format: {js_result}")
    
    if args.js_shellcode:
        c_result = javascript_to_c(args.js_shellcode)
        print(f"C Format: {c_result}")

if __name__ == "__main__":
    main()
