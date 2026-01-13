def decrypt_text(shift1, shift2):
    with open("encrypted_text.txt", "r") as infile:
        text = infile.read()

    decrypted = ""
    i = 0

    while i < len(text):
        tag = text[i:i+2] if text[i] in "LU" else text[i]
        i += 2 if text[i] in "LU" else 1
        ch = text[i]
        i += 1

        if tag == "L1":
            shift = shift1 * shift2
            decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))

        elif tag == "L2":
            shift = shift1 + shift2
            decrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

        elif tag == "U1":
            shift = shift1
            decrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

        elif tag == "U2":
            shift = shift2 ** 2
            decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))

        else:  # Other characters
            decrypted += ch

    with open("decrypted_text.txt", "w") as outfile:
        outfile.write(decrypted)
