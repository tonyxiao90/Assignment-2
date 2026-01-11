
def decrypt_text(shift1, shift2):

    with open ("encrypted_text.txt", "r") as infile:
        text = infile.read()

    decrypt_text = ""

    for char in text: 
        if char.islower():  #Lowercase Letters
            pos = ord(char) - ord('a')
            if pos <= 12: # a-m 
                shift = shift1 * shift2
                new_pos = (pos - shift) % 26
            else:
                shift = shift1 + shift2
                new_pos = (pos + shift) % 26

            decrypt_text += chr(new_pos + ord('a'))

        elif char.isupper():
            pos = ord(char) - ord('A')

            if pos <= 12: 
                shift = shift1
                new_pos = (pos + shift) % 26
            else:
                shift = shift2 ** 2
                new_pos = (pos - shift) % 26

            decrypt_text += chr(new_pos + ord('A'))

        else:
            decrypt_text += char
    
    with open("decrypted_text.txt", "w") as outfile:
        outfile.write(decrypt_text)

