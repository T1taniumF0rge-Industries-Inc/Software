from cryptography.fernet import Fernet
def keygen():
    print("© Okmeque1 Software")
    keygen1 = input("Please enter a valid file name to generate the key(Please make sure that the file is empty before use.) → ")
    key = Fernet.generate_key()
    with open(keygen1,"wb") as openfl:
        openfl.write(key)
    cont = input("Generate other key?[Y,any invalid option to abort]")
    if cont == "Y":
        keygen()
    else:
        return
keygen()
