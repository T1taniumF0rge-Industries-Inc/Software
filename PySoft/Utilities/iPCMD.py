def ipcmd():
    try:
        import os
        iprompt = 'iPCMD>'
        ver = 'GamerSoftware Corporation™ [Version iPCMD Python Full 6.278E]'
        ver1 = '(c) GamerSoftware Corporation™'
        print(ver)
        print(ver1)
        print('')
        try:
            while True:
                prompt = input(iprompt)
                prompt = prompt.lower()
                if prompt == 'exit' or prompt == 'return':
                    return False
                elif prompt == 'ver':
                    print(ver)
                    print(ver1)
                    print('')
                elif 'cd' in prompt[0:3]:
                    os.chdir(prompt[3:])
                    print('')
                elif prompt == 'dsc':
                    print("iPCMD - CMD in Python for bypassing computers with restricted/no access to Windows Command Prompt (cmd.exe) or Linux/Mac Terminal")
                    print("Use at your own risk - GamerSoftware & Okmeque1 Corporation is not responsible for any damages done to any computers or people using this program.")
                    print("If iPCMD gets blocked or fails to bypass then your computer is not bypassable.")
                    print("Commands depend on your system. The prompt can be changed from the iprompt value in the code")
                    print("Commands may not work depending on your system.")
                    print("Current system : " + os.name)
                    print('') 
                elif 'prompt' in prompt and 'prompt:' not in prompt and 'prompt reset' not in prompt:
                    print("Usage for prompt setting: prompt:[string]")
                    print("To reset prompt type: 'prompt reset'")
                    print('')
                elif 'prompt:' in prompt:
                    iprompt = prompt[7:]+'>'
                    print('Prompt setting complete!')
                    print("To reset prompt type: 'prompt reset'")
                    print('')
                elif prompt == 'prompt reset':
                    print('Prompt resetting complete!')
                    print('')
                    iprompt = 'iPCMD>'
                else:
                    os.system(prompt)
                    print('')
        except OSError:
            print("Error: The operating system has forcibly closed the running process due to a fatal system error.")
            print('')
            input("Press enter to continue...")
            return None
        except ValueError:
            print("Error: The value for a variable is either invalid or an access violation has occured.")
            print('')
            input("Press enter to continue...")
            return None
        except PermissionError:
            print("Error: Access violation and permission error and security bypass fail has occured in your file. The operating system will now forcibly close due to this error.")
            print('')
            input("Press enter to continue...")
            return None
        except FileNotFoundError:
            print("Error: The requested file you specified does not exist. The operating system will forcibly close the program due to reading in an invalid space.")
            print('')
            input("Press enter to continue...")
            return None
        except EOFError:
            print("Error: The requested operation read beyond the end of the specified file. The operating system will now forcibly close the program.")
            print('')
            input("Press enter to continue...")
            return None
        except KeyboardInterrupt:
            print("Error: The user has chosen to exit. Exiting...")
            return None
        except IOError:
            print("Error: I/O ports error. A device on your system has either malfunctioned or has been unplugged. The operating system will now forcibly close the program.")
            print('')
            input("Press enter to continue...")
            return None
        except:
            print("Error: The program has forcibly exited with code 1.")
            print('')
            input("Press enter to continue...")
            return None
    except:
        print("Error: EXCEPTION_IN_EXCEPTION: The program has attempted to recover from an exception causing another exception which caused it to forcibly close.")
        return None
ipcmd()
