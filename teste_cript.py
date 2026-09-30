from gerRSA_v3 import gerRsa


def strToAscii(text):
    return [ord(c) for c in text]

if __name__ == "__main__":
    text    = input("Diga algo: ")
    ascii   = strToAscii(text)
    text2 = ""

    rsa = gerRsa()
    chaves = rsa.getRsa()

    cifrado    = [pow(c, chaves["Public"][1], chaves["Public"][0]) for c in ascii]
    decifrado  = [pow(d, chaves["Private"][1], chaves["Private"][0]) for d in cifrado] 

    for d in decifrado:
        text2 += chr(d)

    print("Texto: ", text)
    print("Ascii: ", ascii)
    print("Cifrado: ", cifrado)
    print("Decifrado: ", decifrado)
    print(text == text2)
    #print(decifrado == ascii)

