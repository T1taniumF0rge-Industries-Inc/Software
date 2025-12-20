import os, socket
def ipcmd():
    while True:
            iprompt = 'iPCMD>'
            ver = 'GamerSoftware Corporation™ [Version iPCMD Extended Python Full 7.00M]'
            ver1 = '(c) GamerSoftware Corporation™, (c) Okmeque1 Software'
            print(ver)
            print(ver1)
            print("Type 'dsc' for a description of this program.")
            print("Type 'prompt' for prompt setting changes")
            print("Type 'help' to get a list of commands for your system")
            print("Type 'intro' to see this introduction screen.")
            print("NOTE: when using the 'cd' command, use the following format: 'cd directory' (with a space between the commands)")
            print('')
            directory_prompt = False
            try:
                while True:
                    if directory_prompt is True:
                        prompt = input(os.getcwd() + ">")
                    else:
                        print(f"{os.getlogin()}@{socket.gethostname()} {os.getcwd()} - iPCMD")
                        prompt = input(iprompt)
                    prompt1 = prompt.lower() # This way system commands still have the raw input
                    if prompt1 == 'exit' or prompt1 == 'return':
                        return False
                    elif prompt1 == 'ver':
                        print(ver)
                        print(ver1)
                        print('')
                    elif prompt1 in ('cd', 'cd /?', 'cd/?', 'cd -help', 'cd --help'):
                        print("Use the 'cd' command to change directories. Example: 'cd C:\\WINDOWS\\SYSTEM32' will change the directory to C:\\WINDOWS\\SYSTEM32")
                        print('')
                    elif os.name == 'nt' and len(prompt1.strip()) == 2 and prompt1.strip()[1] == ':' and prompt1.strip()[0].isalpha() == True:
                        os.chdir(prompt1.strip())
                        print()
                    elif 'cd' in prompt1[0:2]:
                        command_chaining = prompt.split("&")
                        os.chdir(command_chaining[0][2:].strip())
                        for x in range(1, len(command_chaining)):
                            os.system(command_chaining[x])
                        print('')
                    elif prompt1 == 'dsc':
                        print("*** iPCMD - Intelligent Python CMD ***")
                        print("iPCMD - CMD in Python for bypassing computers with restricted/no access to Windows Command Prompt (cmd.exe) or Linux/Mac Terminal")
                        print("Use at your own risk - GamerSoftware & Okmeque1 Corporation is not responsible for any damages done to any computers or people using this program.")
                        print("If iPCMD gets blocked or fails to bypass then your computer is not bypassable (could be for the block of os module or deleting CMD.exe, etc).")
                        print("Commands depend on your system. Custom commands specific to this program can be seen using the 'intro' command")
                        print("Commands may not work depending on your system or if the os module has been blocked.")
                        print("NOTE: when using the 'cd' command, use the following format: 'cd directory' (with a space between the commands)")
                        print("Current system : " + os.name)
                        print('') 
                    elif prompt1.startswith("prompt") and not prompt1.startswith("prompt:") and prompt1 != 'prompt reset' and prompt1 != 'prompt directory':
                        print("Usage for prompt setting: prompt:[whatever text you want to be the prompt]")
                        print("To set the prompt to the current directory, type 'prompt directory'")
                        print("To reset prompt type: 'prompt reset'")
                        print('')
                    elif prompt1.startswith("prompt:"):
                        iprompt = prompt[7:]+'>'
                        print('Prompt setting complete!')
                        print("To reset prompt type: 'prompt reset'")
                        print('')
                    elif prompt1 == 'prompt reset':
                        directory_prompt = False
                        print('Prompt resetting complete!')
                        print('')
                        iprompt = 'iPCMD>'
                    elif prompt1 == 'prompt directory':
                        directory_prompt = True
                        print('Prompt successfully set to show current directory!')
                        print(''))
                    elif prompt1 == 'intro' or prompt1 == 'ver':
                        print(ver)
                        print(ver1)
                        print("Type 'dsc' for a description of this program.")
                        print("Type 'prompt' for prompt setting changes")
                        print("Type 'help' to get a list of commands for your system")
                        print("Type 'intro' to see this introduction screen.")
                        print("NOTE: when using the 'cd' command, use the following format: 'cd directory' (with a space between the commands)")
                        print('')
                    else:
                        os.system(prompt)
                        print('')
            except IOError as e:
                print(f"Error: I/O error. A device on your system has either malfunctioned or has been unplugged or a file operation has failed. Make sure that any hardware connected to the computer is functioning and is correctly attached to the computer (like a USB drive plugged in all the way) and that you use Safe Eject when removing devices from the computer.")
                print(f"Details: {e}, error code 0272")
                print('')
                input("Press enter to continue...")
                continue
            except OSError as e:
                print(f"Error: Operating system or program error. Check your drives and program, as well as any files and programs that were run, and try again. ")
                print(f"Details: {e}, error code 0271")
                print('')
                input("Press enter to continue...")
                continue
            except PermissionError as e:
                print(f"Error: Access violation and permission error and security bypass fail has occured in your resource. Make sure that you have the appropriate permissions to use your resource.")
                print(f"Details: {e}, error code 6510C")
                print('')
                input("Press enter to continue...")
                continue
            except FileNotFoundError as e:
                print(f"Error: The requested file you specified does not exist. Make sure that the file name is valid and that the file exists and is usable")
                print(f"Details: {e}, error code 6510B")
                print('')
                input("Press enter to continue...")
                continue
            except (KeyboardInterrupt, EOFError, SystemExit):
                print("User has chosen to exit. Exiting...")
                exit()
            except Exception as e:
                print(f"Error: An error has occured in this program. Consult the GamerSoft24/Software PySoft error chart and the Python manual for more information, using the details as guidance for the error.")
                print(f"Details: {e}, error code 0281 (check error chart using details information for a possible solution to this problem)")
                print('')
                input("Press enter to continue...")
                continue
ipcmd()
