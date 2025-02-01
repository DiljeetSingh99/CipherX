import base64

def encode_text(plaintext):
    encoded_bytes = base64.b64encode(plaintext.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def decode_text(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

def main():
    print("Base64 Encoder/Decoder Program")
    
    while True:
        choice = input("Choose operation - Encode (E) / Decode (D) / Exit (X): ").strip().upper()
        
        if choice == 'X':
            print("Exiting the program.")
            break
        elif choice not in ['E', 'D']:
            print("Invalid option! Please choose 'E' for encoding, 'D' for decoding, or 'X' to exit.")
            continue

        text = input("Enter the text: ").strip()
        
        if choice == 'E':
            result = encode_text(text)
            print(f"Encoded Text: {result}")
        else:
            result = decode_text(text)
            print(f"Decoded Text: {result}")

if __name__ == "__main__":
    main()
