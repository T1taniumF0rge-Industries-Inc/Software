def icmd():
    try:
        iprompt = 'iCMD>'
        ver = 'iCMD Full 1.05A - Okmeque1 Corporation - (c) Okmeque1 Corporation 2023-2025 All Rights Reserved.'
        print(ver)
        try:
            import os
            while True:
                prompt = input(iprompt)
                if 'prompt:' in prompt:
                    iprompt = prompt[7:] + ">"
                prompt = prompt.lower()
                if prompt == 'exit' or prompt == 'return':
                    return False
                elif prompt == 'ver':
                    print(ver)
                elif 'cd' in prompt[0:3]:
                    os.chdir(prompt[3:])
                elif prompt == 'dsc':
                    print("iCMD - CMD for computers with restricted/no access to CMD.EXE or Linux/Mac Terminal")
                    print("Use at your own risk - Okmeque1 Corporation is not responsible for any damages done to any computers or people using this program.")
                    print("If iCMD gets blocked download the Lite version.")
                    print("Commands depend on your system.The prompt can be changed by doing PROMPT:[STRING]")
                    print("Commands may not work depending on your system.")
                    print("Current system : " + os.name)
                elif 'prompt' in prompt and 'prompt:' not in prompt:
                    print("Usage : PROMPT:[STRING]")
                else:
                    os.system(prompt)
        except OSError:
            print("STOP : 0271\nThe Operating System has forcibly closed the running process due to a fatal system error.")
            input("Press ENTER to exit...")
            return None
        except ImportError:
            print("STOP : 0253\nModule specified does not exist.Module missing : RANDOM.")
            input("Press ENTER to exit...")
            return None
        except SystemError or RuntimeError:
            print("STOP : 760F/755F\nBad Python interpreter.")
            input("Press ENTER to exit...")
            return None
        except MemoryError:
            print("STOP : 765E\nNo more memory for program.")
            input("Press ENTER to exit...")
            return None
        except TimeoutError:
            print("STOP : 780F\nOperation took too long")
            input("Press ENTER to exit...")
            return None
        except NameError:
            print("STOP : 0273\nCode is either invalid or bad reference set was specified.")
            input("Press ENTER to exit...")
            return None
        except ValueError:
            print("STOP : 0211\nThe value for a variable is either invalid or an access violation has occured.")
            input("Press ENTER to exit...")
            return None
        except TypeError:
            print("STOP : 0251\nCode is either invalid or has been tampered with.Please contact support.")
            input("Press ENTER to exit...")
            return None
        except PermissionError:
            print("STOP : 0210\nAccess Violation has occured in your file.The Operating system will now forcibly close due to this error")
            input("Press ENTER to exit...")
            return None
        except FileNotFoundError:
            print("STOP : 6510B\nThe requested file you specified does not exist.The Operating system will forcibly close the program due to reading in an invalid space.")
            input("Press ENTER to exit...")
            return None
        except FileExistsError:
            print("STOP : 6510A\nThe requested file you specified exists.The operating system will forcibly close the program due to writing a created file with no access.")
            input("Press ENTER to exit...")
            return None
        except EOFError:
            print("STOP : 0250\nThe requested operation read beyond the end of the specified file.The Operating system will now forcibly close the program.")
            input("Press ENTER to exit...")
            return None
        except KeyboardInterrupt:
            print("STOP : 0270\nThe user has chosen to exit.Exiting...")
            return None
        except IOError:
            print("STOP : 6510C\nI/O error has occured.This means a device on your system has either malfunctioned or has been unplugged.The Operating system will now forcibly close the program.")
            input("Press ENTER to exit.")
            return None
        except SyntaxError:
            print("STOP : 0280\nCode is either invalid or has been tampered with.Please contact support.")
            input("Press ENTER to exit.")
            return None
        except:
            print("STOP : 0281\nThe program has forcibly exited with code 1")
            input("Press ENTER to exit...")
            return None
    except:
        print("STOP : 0F0A EXCEPTION_IN_EXCEPTION : The program has attempted to recover from an exception causing another exception which caused it to forcibly close.")
        return None
icmd()
