import argparse

def c_to_js(c_shellcode):
    """Convert C-style shellcode to JavaScript format."""
    c_format_len = len(c_shellcode)
    result = ""
    if c_format_len % 8:
        c_shellcode += "\\x00"
        c_format_len = len(c_shellcode)
    for i in range(2, c_format_len - 6, 8):
        tmp1 = c_shellcode[i:i+2]
        tmp2 = c_shellcode[i+4:i+6]
        result += f"\\u{tmp2}{tmp1}"
    return result

def js_to_c(js_shellcode):
    """Convert JavaScript-style shellcode to C format."""
    js_format_len = len(js_shellcode)
    result = ""
    for i in range(2, js_format_len - 4, 6):
        tmp1 = js_shellcode[i:i+2]
        tmp2 = js_shellcode[i+2:i+4]
        result += f"\\x{tmp2}\\x{tmp1}"
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert shellcode between C and JavaScript formats.")
    parser.add_argument("--input", required=True, help="Input shellcode")
    parser.add_argument("--from", required=True, choices=["c", "js"], help="Input format (c or js)")
    parser.add_argument("--to", required=True, choices=["c", "js"], help="Output format (c or js)")
    args = parser.parse_args()

    if args.from == "c" and args.to == "js":
        output = c_to_js(args.input)
    elif args.from == "js" and args.to == "c":
        output = js_to_c(args.input)
    else:
        print("Invalid conversion direction.")
        exit(1)

    print(output)
