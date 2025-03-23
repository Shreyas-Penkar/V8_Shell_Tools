import struct

def hex_to_double(hex_pointer):
    # Remove the '0x' prefix and pad the hex value to 16 characters (64 bits)
    hex_value = hex_pointer[2:].zfill(16)
    
    # Convert the hex string to bytes
    byte_value = bytes.fromhex(hex_value)
    
    # Unpack the bytes to a double (64-bit floating point)
    double_value = struct.unpack('!d', byte_value)[0]
    
    return double_value

def double_to_hex(double_value):
    # Pack the double into bytes
    byte_value = struct.pack('!d', double_value)
    
    # Convert the bytes to a hex string
    hex_value = byte_value.hex()
    
    # Add the '0x' prefix
    return f"0x{hex_value}"

def main():
    while True:
        print("\nOptions:")
        print("1. Hex to Double")
        print("2. Double to Hex")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ").strip()
        
        if choice == "1":
            # Hex to Double
            hex_input = input("Enter a hex value with '0x' prefix: ").strip()
            if not hex_input.startswith("0x"):
                print("Error: Hex value must start with '0x'.")
                continue
            try:
                double_value = hex_to_double(hex_input)
                print(f"Double value: {double_value:.20e}")
            except ValueError:
                print("Error: Invalid hex value.")
        
        elif choice == "2":
            # Double to Hex
            double_input = input("Enter a double value in scientific notation: ").strip()
            try:
                double_value = float(double_input)
                hex_output = double_to_hex(double_value)
                print(f"Hex value: {hex_output}")
            except ValueError:
                print("Error: Invalid double value.")
        
        elif choice == "3":
            # Exit
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
