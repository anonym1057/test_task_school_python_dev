"""
author: Nosova Olga
email: nosova-olenka@mail.ru

Encrypt and decrypt text using a simple algorithm of offsetting 26 letters of English alphabet.
"""
alphabet='abcdefghijklmnopqrstuvwxyz'

def encrypt(string_to_encript:str,offset:int):
    """
    Encrypt text using a simple algorithm of offsetting 26 letters of English alphabet.
    :param string_to_encript: string for encrypt
    :param offset: offset for encrypt
    :return: encrypting string : str
    """
    s=string_to_encript.lower()
    offset_null=ord('a')
    len_alphabet=len(alphabet)

    encrypt_string=""

    for ch in s:
        if ch.isalpha():
            new_index=((ord(ch)-offset_null)+offset)%len_alphabet
            encrypt_string+=alphabet[new_index]
        else:
            encrypt_string+=ch
    return encrypt_string

def decrypt(string_to_encript:str,offset:int):
    """
    Dencrypt text using a simple algorithm of offsetting 26 letters of English alphabet.
    :param string_to_encript: string for decrypt
    :param offset: offset for decrypt
    :return: encrypting string : str
    """
    return encrypt(string_to_encript,offset*-1)


if __name__=="__main__":
    case='1'
    while case!=0:
        if case=='1':
            print("\n1 - print info\n"
                  "2 - encrypt\n"
                  "3 - decrypt\n"
                  "0 - exit\n")
        elif case == '2':
            s=input("String to encrypt: ")
            offset=input("Offset: ")
            try:
                offset=int(offset)
            except Exception:
                print("Invalid format offsets")

            print("Decrypting string: ",encrypt(s,offset))
        elif case== '3':
            s = input("String to dencrypt: ")
            offset = input("Offset: ")
            try:
                offset = int(offset)
            except Exception:
                print("Invalid format offsets")

            print("Ecrypting string: ", decrypt(s, offset))
        elif case == '0':
            break
        else:
            print("Invalid cases value")

        case = input("Choose case: ")


