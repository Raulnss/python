def decrypt_caesar_cipher(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_unicode = ord(char) - shift
            if char.islower():
                if shifted_unicode < ord('a'):
                    shifted_unicode += 26
            elif char.isupper():
                if shifted_unicode < ord('A'):
                    shifted_unicode += 26
            plaintext += chr(shifted_unicode)
        else:
            plaintext += char
    return plaintext

def main():
    ciphertext = input("Digite o texto cifrado: ")
    attempts = 0
    for i in range(26):
        decrypted_text = decrypt_caesar_cipher(ciphertext, i)
        print(f"Tentativa {i + 1}: {decrypted_text}")
        attempts += 1
    print(f"Total de tentativas: {attempts}")

if __name__ == "__main__":
    main()