import os
def icmd():
        try:
                print("iCMD-Lite - iCMD with limited features : core functionality.\nCopyright (c) Okmeque1 Corporation 2023-2025")
                while True:
                        prompt = input("iCMD-Lite>")
                        if prompt == 'exit' or prompt == 'return':
                                return False
                        elif 'cd' in prompt[0:3]:
                                os.chdir(prompt[3:])
                        elif 'prompt' in prompt:
                                print("PROMPT disabled in iCMD-Lite")
                        os.system(prompt)
        except BaseException:
                print("STOP : 770A\n General Exception.Retry the operation")
                input("Press ENTER to exit...")
                return None
icmd()
