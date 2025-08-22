from cryptography.fernet import Fernet
def keygen(keygen1):
    try:
        key = Fernet.generate_key()
        with open(keygen1,"wb") as openfl:
            openfl.write(key)
        print(f"Key file saved to {keygen1}.")
        return 
    except FileExistsError as e:
        print(f"STOP : 6510A\nThe file name that you specified is conflicting with another file. Delete or rename the conflicting file, or choose a different name for your file.\nDetails: {e}")
        input("Press ENTER to return to main menu...")
        return
    except Exception as e:
        input(f"STOP : {e}\nReview the error chart and Python manual for more info.\nPress ENTER to return to main menu...")
        return            
def enc(keychose,file_enc):
    try:
        with open(keychose,"rb") as load:
            key = load.read()
        with open(file_enc,"rb") as lwe:
            towr = lwe.read()
        key1 = Fernet(key)
        encrypted = key1.encrypt(towr)
        with open(file_enc,"wb") as twrite:
            twrite.write(encrypted)
        print("Encrypted with no errors")
        return
    except FileNotFoundError:
        print("STOP : 6510B\nFile specified does not exist.Make sure the file exists and try again.")
        input("Press ENTER to return to main menu...")
        return
    except Exception as e:
        input(f"STOP : {e}\nReview the error chart and Python manual for more info.\nPress ENTER to return to main menu...")
        return
def dec(keychose,file_dec):
    try:
        with open(keychose,"rb") as load:
            key = load.read()
        with open(file_dec,"rb") as lwd:
            tore = lwd.read()
        key2 = Fernet(key)
        decrypted = key2.decrypt(tore)
        with open(file_dec,"wb") as td:
            td.write(decrypted)
        print("Decrypted with no errors.")
    except FileNotFoundError:
        print("STOP : 6510B\nFile specified does not exist.Make sure the file exists and try again.")
        input("Press ENTER to return to main menu...")
        return
    except Exception as e:
        input(f"STOP : {e}\nReview the error chart and Python manual for more info.\nPress ENTER to return to main menu...")
        return