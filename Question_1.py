from Encryption import *
from Decryption import *
from Verification import *

def main():
    shift1 = int(input("Enter Shift1: "))
    shift2 = int(input("Enter Shift2: "))

    encrypt_text (shift1, shift2)
    decrypt_text (shift1, shift2)
    verify_decryption()

if __name__ == "__main__":
    main()




#     from Encryption import *

# from Decryption import * #all 

# def main():

#     message = "hello world tony"

#     shift = 5

#     encrypted = encrypt(message, shift)

#     print(encrypted)

#     decrypted = decrypt(encrypted, shift)

#     print(decrypted)

# if __name__ == "__main__":
#     main()


# #commits 
# #pull request 
# #push request