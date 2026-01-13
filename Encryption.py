def encrypt_text(shift1, shift2):
    with open("raw_text.txt", "r") as infile:
        text = infile.read()

    encrypted = ""

    for ch in text:
        # Lowercase letters
        if ch.islower():
            if 'a' <= ch <= 'm':
                shift = shift1 * shift2
                enc = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
                encrypted += "L1" + enc   # tag: lowercase, first half
            else:  # n-z
                shift = shift1 + shift2
                enc = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
                encrypted += "L2" + enc   # tag: lowercase, second half

        # Uppercase letters
        elif ch.isupper():
            if 'A' <= ch <= 'M':
                shift = shift1
                enc = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
                encrypted += "U1" + enc   # tag: uppercase, first half
            else:  # N-Z
                shift = shift2 ** 2
                enc = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
                encrypted += "U2" + enc   # tag: uppercase, second half

        # Other characters
        else:
            encrypted += "O" + ch        # tag: other

    with open("encrypted_text.txt", "w") as outfile:
        outfile.write(encrypted)
