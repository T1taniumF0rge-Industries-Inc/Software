from cryptography.fernet import Fernet
def enc(key):
    file_enc = input("Please enter a valid file name to encrypt → ")
    with open(file_enc,"rb") as lwe:
        towr = lwe.read()
    key1 = Fernet(key)
    encrypted = key1.encrypt(towr)
    with open(file_enc,"wb") as twrite:
        twrite.write(encrypted)
    print("Encrypted with no errors")
    mainmenu()
def dec(key):
    file_dec = input("Please enter a valid file name to decrypt → ")
    with open(file_dec,"rb") as lwd:
        tore = lwd.read()
    key2 = Fernet(key)
    decrypted = key2.decrypt(tore)
    with open(file_dec,"wb") as td:
        td.write(decrypted)
    print("Decrypted with no errors.")
    mainmenu()
def start():
        key = input("Please enter a valid file name with a valid key. : ")
        with open(key,"rb") as encdeckey:
            key1 = encdeckey.read()
        mainmenu(key1)
def mainmenu(key):
    try:
        print("Encrypter-Decrypter system by Okmeque1")
        print("1 → Encrypt file.")
        print("2 → Decrypt file.")
        a = input("Please choose : ")
        if a == "1":
            enc(key)
        elif a == "2":
            dec(key)
        else:
            return
    except FileNotFoundError:
        print("STOP : 6510B\nFile specified does not exist.Make sure the file exists and try again.")
        input("Press ENTER to exit.")
        return None
    except KeyboardInterrupt or EOFError:
        print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
        return None
start()
