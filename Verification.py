def verify_decryption():
    with open("raw_text.txt", "r") as file1:
        original = file1.read()

    with open("decrypted_text.txt", "r") as file2:
        decrypted = file2.read()

    if original == decrypted: 
        print(" Decryption successful")
    else: 
        print("Decryption failed")