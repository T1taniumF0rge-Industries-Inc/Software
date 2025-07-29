import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from tkinter import *
import datetime     
import requests
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
import random
import os
import json
import html
import sys
import psutil
from cryptography.fernet import Fernet
import math
class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033{4m'
    END = '\033[0m'

class AssistantApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("G-AIO")
        self.configure(bg="black")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, OpenWebPage, SendEmail, RandomJoke, SystemCommand, GamesMenu, TicTacToe, TextEditor, ToolsMenu, PassManager, OpenTDB, not1,ErrorGen,RPS,Calculator,HangMan,GuessNumber,WinAIO,Diskpart):
            # print(F)
            # print(type(F)) 
            frame = F(container, self) #put a stupid virgule on there, caused the entire program to stop working
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        copyrights = Label(self,text="© Okmeque1 Software & Midnight_G0ldX Corporation")
        label = tk.Label(self, text="Main Menu.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        options = [
            ("Open a Web Page.", lambda: controller.show_frame(OpenWebPage)),
            ("Send an Email.", lambda: controller.show_frame(SendEmail)),
            ("Fetch a Random Joke.", lambda: controller.show_frame(RandomJoke)),
            ("Execute a System Command.", lambda: controller.show_frame(SystemCommand)),
            ("Games Menu.", lambda: controller.show_frame(GamesMenu)),
            ("Text Editor", lambda: controller.show_frame(TextEditor)),
            ("Tools Menu", lambda: controller.show_frame(ToolsMenu)),
            ("WinAIO", lambda: controller.show_frame(WinAIO)), #DO NOT FORGET TO ADD A COMMA AFTER THE END, BECAUSE OTHERWISE IT CAUSES THE ENTIRE PROGRAM TO CRASH!!!
            ("Exit.", self.quit)
        ]

        for text, command in options:
            button = tk.Button(self, text=text, width=40, height=2, command=command)
            button.pack(pady=5)
    def gettime(self):
        return datetime.datetime.now()
class WinAIO(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="WinAIO (G-AIO for Windows)", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)
        b1 = Button(self,text="Install WinAIO ", width=40,command=lambda: self.setup(0))
        b4 = Button(self,text="Uninstall WinAIO ", width=40,command=lambda: self.setup(1))
        b2 = Button(self,text="More informations (highly recommended)",width=40,command=lambda: self.setup(2))
        b7 = Button(self,text="Open file manager",width=40,command=lambda: os.system("C:\windows\explorer.exe"))
        b5 = Button(self,text="Restart Computer",width=40,command=lambda: os.system("shutdown /r /t 0"))
        b6 = Button(self,text="Remove WinAIO Directory and files",width=40,command=lambda: self.rmv())
        b3 = Button(self,text="Return to main menu",width=40,command=lambda: controller.show_frame(MainMenu))
        b1.pack(pady=5)
        b4.pack(pady=5)
        b2.pack(pady=5)
        b7.pack(pady=5)
        b5.pack(pady=5)
        b6.pack(pady=5)
        b3.pack(pady=5)
    def rmv(self):
        if "C:\\WinAIO" in os.path.abspath(__file__):
            x = messagebox.askyesno("WinAIO Removal","Removal tool can't remove C:\\WinAIO folder because you are currently running G-AIO in that folder. The program must be copied to another location before the removal process can start.\n\nDo you want to copy?",icon=messagebox.WARNING)
            if x:
                directory = filedialog.askdirectory()
                a = os.system(f'copy /Y "{os.path.abspath(__file__)}" "{directory}"')
                if a == 0:
                    os.chdir(directory)
                    os.system(f'start "" {os.path.basename(__file__)} --rd')
                    exit()
                else:
                    x = messagebox.showerror("WinAIO Removal","Error while removing C:\\WinAIO. Please see the logs for more info (usually the command line or the Python interpeter, usually seen with a snake icon)")  
                    return            
            else:
                x = messagebox.showerror("WinAIO Removal","Failed to remove WinAIO directory: The folder is in use by another process.")
                return
        else:
            a = os.system("rd /q /s C:\\WinAIO")
            if a == 0:
                x = messagebox.showinfo("WinAIO Removal","Removal of C:\\WinAIO successful.")
                return
            else:
                x = messagebox.showerror("WinAIO Removal","Error while removing C:\\WinAIO. Please see the logs for more info (usually the command line or the Python interpeter, usually seen with a snake icon)")
                return
    def setup(self,parameter):
        if parameter == 0:
            wordchoice = "install G-AIO onto your computer. It will be installed in the C:\WinAIO folder (the install location can not be changed due to compatibility reasons. You can add it in the code if you want)"
        if parameter == 1:
            wordchoice = "uninstall G-AIO from your computer."
        if parameter == 2:
            a = messagebox.showinfo("WinAIO Setup Information","WinAIO is a plug-in for Windows that replaces the standard shell with this program. It changes the Shell registry key and install itself in C:\\WinAIO folder. This install directory cannot be changed.\n\nNOTE: To use this function of this program, you must agree to the license and its terms of conditions as said in the GitHub GamerSoft24/Software repository, as well as any and all disclaimers and warranty information (if applicable). We will not be liable for any damages caused by any file, software package, individual program or other material from this repository in your possession (this includes, but is not limited to, modification, execution or download of the files)! This includes, but is not limited to, unintentional bugs, user error caused by an unclear prompt, clearly marked dangerous programs that may crash your computer or user negligence (didn't read the warnings) and more.")
            return
        if os.name != 'nt':
            a = messagebox.showerror("The OS that you are using is not compatible with WinAIO Software. ")
        a = messagebox.showinfo("WinAIO Setup",f"Setup will now {wordchoice}")
        if parameter == 0:
            a = messagebox.askyesno("WinAIO Setup","Setup will override the default Windows menu that you may be used to and replace it with this program. The developers of this program are in no way, shape or form liable for any data loss that occurs, to the extent of the LICENSE and warranty agreements in the GitHub GamerSoft24/Software repository.\nDo you with to continue?",icon=messagebox.WARNING)
            if a:
                os.system("md C:\\WinAIO")
                try:
                    with open("C:\\Windows\\py.exe","r") as detect:
                        
                        with open("C:\\WinAIO\\START.BAT","w") as launcher:
                            launcher.write("@echo off")
                            launcher.write('start "" C:\\WinAIO\\G-AIO.PY')
                            launcher.write("exit /b")
                        with open("C:\\WinAIO\\RUN.BAT","w") as temp:
                            temp.write(f"{os.path.abspath(__file__)} --setup\n")
                            temp.write("exit /b\n")
                        with open("C:\\WinAIO\\SETUP.BAT", "w") as authadmin:
                            authadmin.write("@echo off\n")
                            authadmin.write("net session >nul 2>&1\n")
                            authadmin.write("if %errorLevel% neq 0 (\n")
                            authadmin.write("    echo Please wait for admin privileges to be authorized\n")
                            authadmin.write(f"""   powershell -Command "Start-Process cmd -ArgumentList '/c C:\\WinAIO\\RUN.BAT' -Verb RunAs"\n""")
                            authadmin.write("    exit /b\n")
                            authadmin.write(")\n")  
                        os.system("C:\\WinAIO\\SETUP.BAT")
                        return
                except FileNotFoundError:
                    askcontinue = messagebox.askyesno("WinAIO Setup","Python was not detected at the standard location of C:\Windows\py.exe\nDo you wish to specify the location of the python interpreter?",icon=messagebox.WARNING)
                    if askcontinue:
                        python = filedialog.askopenfilename()
                        with open("C:\\WinAIO\\START.BAT","w") as launcher:
                            launcher.write("@echo off")
                            launcher.write('start "" C:\\WinAIO\\G-AIO.PY')
                            launcher.write("exit /b")
                        with open("C:\\WinAIO\\RUN.BAT","w") as temp:
                            temp.write(f"{os.path.abspath(__file__)} --setup --python-interpreter={python}\n")
                            temp.write("exit /b\n")
                        with open("C:\\WinAIO\\SETUP.BAT", "w") as authadmin:
                            authadmin.write("@echo off\n")
                            authadmin.write("net session >nul 2>&1\n")
                            authadmin.write("if %errorLevel% neq 0 (\n")
                            authadmin.write("    echo Please wait for admin privileges to be authorized\n")
                            authadmin.write(f"""   powershell -Command "Start-Process cmd -ArgumentList '/c C:\\WinAIO\\RUN.BAT' -Verb RunAs"\n""")
                            authadmin.write("    exit /b\n")
                            authadmin.write(")\n")  
                        os.system("C:\\WinAIO\\SETUP.BAT")    
                        return       
                    else:
                        a = messagebox.showerror("WinAIO Setup","The operation was cancelled because no Python interpreter could be found.")  
                        return
                except Exception as e:
                    a = messagebox.showerror("WinAIO Setup",f"An error has occured while creating and configuring the configuration scripts \nError details: {e}")
                    return
            else:
                a = messagebox.showerror("WinAIO Setup","The operation was cancelled.")
                return
        if parameter == 1:       
                os.system("md C:\\WinAIO")
                os.system("del /f C:\\WinAIO\\START.BAT")
                with open("C:\\WinAIO\\RUN.BAT","w") as temp:
                    temp.write(f"{os.path.abspath(__file__)} --unsetup\n")
                    temp.write("exit /b\n")
                with open("C:\\WinAIO\\UNSETUP.BAT", "w") as authadmin:
                    authadmin.write("@echo off\n")
                    authadmin.write("net session >nul 2>&1\n")
                    authadmin.write("if %errorLevel% neq 0 (\n")
                    authadmin.write("    echo Please wait for admin privileges to be authorized\n")
                    authadmin.write(f"""   powershell -Command "Start-Process cmd -ArgumentList '/c C:\\WinAIO\\RUN.BAT' -Verb RunAs"\n""")
                    authadmin.write("    exit /b\n")
                    authadmin.write(")\n")           
                os.system("C:\\WinAIO\\UNSETUP.BAT")
                return
class Diskpart(Frame): #G-AIO to SATA, lose all your DATA
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Hard Disk Utilities", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)
        l1 = Label(self,text="Welcome to the Hard Disk utilities.\nBeware that this program has limited compatability on other operating systems, Windows is best\nAdmin power is required for all functions of this utility.")
        l1.pack(pady=5)
        b1 = Button(self,text="Format Computer Hard Disk (Windows Only)",width=40,command=self.format1)
        b1.pack(pady=5)
        b2 = Button(self,text="Refresh Hard Disk information",width=40, command=self.refresh)
        b2.pack(pady=5)
        b3 = Button(self,text="Return to main menu",width=40,command=lambda: controller.show_frame(MainMenu))
        b3.pack(pady=5)
        self.diskinfo = Text(self,width=50,height=10)
        self.diskinfo.pack()
    def format1(self): #because the format() function already exists??
        formatstr = "format "
        filesystem = simpledialog.askstring("File System Type","Please enter the type of file system.\nFor Windows, use 'NTFS', but for USB drives and other devices, use 'FAT32'.\nPress CANCEL for default")
        label = simpledialog.askstring("Volume Label","Please enter the volume label.\nPress CANCEL for a blank label")
        quick = messagebox.askyesno("Format Speed","Perform a quick format?",icon=messagebox.QUESTION)
        drive = simpledialog.askstring("Drive Selection","Enter the drive to format")
        confirm = messagebox.askyesno("Data Warning",f"All data on drive {drive} will be ERASED!\nDo you wish to proceed?",icon=messagebox.WARNING)
        if confirm:
            if not drive:
                x = messagebox.showerror("Format Error","Disk not selected.")
                return
            formatstr += f"{drive} "
            if filesystem:
                formatstr += f"/FS:{filesystem} "
            if label:
                formatstr += f"/V:{label} "
            if quick:
                formatstr += "/Q "
            if not quick:
                safe = messagebox.askyesno("Format drive safely","Do you want to fill every sector with 0?\nNote that this may take several hours to complete, but will make it so that no recovery programs may recover the drive")
                if safe:
                    formatstr += "/P:0"
            try:
                x = messagebox.showinfo("G-AIO","If the process ever appears to freeze, make sure to check the Python interpreter (usually a black window with text) if there are any prompts or error messages.")
                result = os.system(formatstr)
                if result == 0:
                    x = messagebox.showinfo("G-AIO","Disk formatted successfully")
                else:
                    x = messagebox.showerror("G-AIO","Error while formatting disk, please see the logs for more info (usually the command line or the Python interpeter, usually seen with a snake icon)")
            except Exception as e:
                x = messagebox.showerror("G-AIO",f"Error while formatting disk.\nError : {e}")



    def refresh(self):
            self.diskinfo.delete("1.0",END)
            self.diskinfo.insert(END,"Hard Disk Info\nDRIVE | FILE SYSTEM | SIZE | USED | FREE\n")
            for x in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(x.mountpoint)
                    self.diskinfo.insert(END,f"{x.mountpoint}     {x.fstype}          {usage.total/(1024**3):.2f} {usage.used/(1024**3):.2f} {usage.free/(1024**3):.2f}\n")
                except PermissionError as e:
                    if 'not ready' in str(e):
                        self.diskinfo.insert(END,f"{x.mountpoint}      Disk not ready for reading\n")
                        continue
                    x = messagebox.showerror("G-AIO",f"A disk read error has occured while fetching disk information.\nError: {e}")
                    continue
                except Exception as e:
                    x = messagebox.showerror("G-AIO",f"Error while refreshing hard disk informations.\nError: {e}")
class OpenWebPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        l1 = Label(self,text="Browser Location (leave blank for default browser)",width=40) #because not everyone wants to use IE7
        l1.pack(pady=5)
        self.other_BR = Entry(self,width=100)
        self.other_BR.pack(pady=5)
        l2 = Label(self,text="URL")
        l2.pack(pady=5)
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=10, padx=10)

        open_button = tk.Button(self, text="Open.", command=self.open_webpage)
        open_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def open_webpage(self):
        
        if self.other_BR.get() == "":
            url = self.url_entry.get()
            webbrowser.open(url)
        else:
            try:
                result = subprocess.run(f'start "" {self.other_BR.get()} {self.url_entry.get()}', shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    pass
                else:
                    messagebox.showerror("G-AIO",f"Failed to start browser. Error: {result.stderr}")
            except Exception as e:
                messagebox.showerror("G-AIO", f"Failed to start browser. Error: {str(e)}.")            

class SendEmail(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Send an Email.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        self.to_label = tk.Label(self, text="To:.")
        self.to_label.pack()

        self.to_entry = tk.Entry(self, width=50)
        self.to_entry.pack(pady=5)

        self.subject_label = tk.Label(self, text="Subject:.")
        self.subject_label.pack()

        self.subject_entry = tk.Entry(self, width=50)
        self.subject_entry.pack(pady=5)

        self.message_label = tk.Label(self, text="Message:.")
        self.message_label.pack()

        self.message_text = tk.Text(self, width=50, height=10)
        self.message_text.pack(pady=5)

        send_button = tk.Button(self, text="Send.", command=self.send_email,width=40)
        send_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu),width=40)
        back_button.pack(pady=10)

    def send_email(self):
        smpt = simpledialog.askstring("SMTP Server","Enter an SMTP server for your mail provider. Default is 'smtp.gmail.com'\nIf you do not spell it correctly, you will get an error!")
        port = simpledialog.askinteger("SMTP Server Port","Enter a port for your SMTP server. Default for GMail is 587")
        mail = simpledialog.askstring("Email address","Enter an email address that corresponds to your provider. This will affect how the password works.")
        pwd = simpledialog.askstring("Password","Enter an app or regular passwords. GMail requires app passwords due to security restrictions, which can be found at https://myaccount.google.com/apppasswords.\nIf with another email provider, check for more info.")
        to_email = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        from_email = mail # Replace with your email address (Gmail only. You can change the SMTP server and port below for other mail providers.)
        app_pwd_or_std_pwd = pwd # Replace with you Gmail App Password. Regular password will not work due to Gmail Security Restrictions. If you want to use an other mail provider, check their security restrictions to see if you need an App Password like Gmail or not.

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP(smpt, port) # You can change the SMTP server and port here if you want a different mail provider like Outlook or Yahoo. Search online for more information.
            server.starttls()
            server.login(from_email, app_pwd_or_std_pwd)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            messagebox.showinfo("Email.", "Email sent successfully.")
        except Exception as e:
            messagebox.showerror("Email.", f"Failed to send email. Error: {str(e)}.")

        self.to_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)

class RandomJoke(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Random Joke.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        self.joke_label = tk.Label(self, text="", font=('Arial', 14))
        self.joke_label.pack(pady=10)

        fetch_button = tk.Button(self, text="Fetch Joke.", command=self.fetch_joke)
        fetch_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def fetch_joke(self):
        try:
            response = requests.get('https://official-joke-api.appspot.com/random_joke')
            if response.status_code == 200:
                joke = response.json()
                self.joke_label.config(text=f"{joke['setup']}\n{joke['punchline']}.")
            else:
                messagebox.showerror("Joke.", "Failed to fetch joke from API, check firewall and internet restrictions.")
        except Exception as e:
            messagebox.showerror("Joke.", f"Failed to fetch joke. Error: {str(e)}.")

class SystemCommand(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="System Command.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        self.command_entry = tk.Entry(self, width=50)
        self.command_entry.pack(pady=10)

        execute_button = tk.Button(self, text="Execute.", command=self.execute_command)
        execute_button.pack(pady=5)

        self.output_text = tk.Text(self, width=80, height=18)
        self.output_text.pack(pady=10)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu),width=40)
        back_button.pack(pady=10)

    def execute_command(self):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, f"Please wait for the Command Execution Service...\nCommands will time out after 5 seconds of being executed.")
        command = self.command_entry.get()
        try:
            result = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True, shell=True)
            stdout, stderr = result.communicate(timeout=5)
            if result.returncode == 0:
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, f"Command executed successfully.\nOutput:\n{stdout}.")
            else:
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, f"Command failed with error:\n{stderr}.")
        except subprocess.TimeoutExpired as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f'Command timed out. \nError: {str(e)}.\n\nTip: if you want to start an application, if you are on Windows, try typing:\nstart "" (your program name here)')            
        except Exception as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Failed to execute command. \nError: {str(e)}.")
class TextEditor(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        l1 = Label(self,text="Text Editor",font=('Arial',18,'bold'))
        l1.pack(pady=10,padx=10)
        self.text = Text(self,width=80,height=20)
        self.text.pack(pady=10)
        l2 = Label(self,text="File Name")
        l2.pack(pady=5)
        self.filename = Entry(self,width=40)
        self.filename.pack(pady=10)
        load = Button(self,text="Load",command=lambda: self.load(),width=40)
        load.pack(pady=5)
        save = Button(self,text="Save",command=lambda: self.save(),width=40)
        save.pack(pady=5)
        frp = Button(self,text="Find/Replace",command=lambda: self.findreplace(),width=40)
        frp.pack(pady=5)
        menu = Button(self,text="Return to Main Menu",command=lambda: controller.show_frame(MainMenu),width=40)
        menu.pack()
    def load(self):
        try:
            with open(self.filename.get(),"r") as reading:
                self.text.delete("1.0",END)
                self.text.insert(END,reading.read())
        except Exception as e:
            x = messagebox.showerror("G-AIO - Load failed",f"Load failed. Error : {str(e)}")
    def save(self):
        try:
            with open(self.filename.get(), "w") as writing:
                writing.write(self.text.get("1.0",END))
                x = messagebox.showinfo("G-AIO","Save complete.")
        except Exception as e:
            x = messagebox.showerror("G-AIO - Save failed",f"Save failed. Error : {str(e)}")
    def findreplace(self):
        try:
            counter = 0
            counter1 = 0
            match = False
            passon = {}
            tofind = simpledialog.askstring("G-AIO","Please enter the value to find.")
            toreplace = simpledialog.askstring("G-AIO","Please enter the value to replace the previous value.\nIf you do not want to replace, press CANCEL")
            with open(self.filename.get(),"r") as read1:
                dalines = read1.readlines()
                for x in range(len(dalines)):
                    while counter < len(dalines[x]):
                        counter1 = 0
                        while counter1 <= len(tofind)-1 and dalines[x][counter] == tofind[counter1]:
                            counter += 1
                            counter1 += 1
                        if counter1 == len(tofind):
                            match == True
                            a = counter - len(tofind)
                            b = x
                            adsf = messagebox.showinfo("G-Editor","Line where found : " + str(b+1) + "\nPosition in line : " + str(a+1))
                            if b not in passon:
                                passon[b] = [a]
                            else:
                                passon[b].append(a)
                        if counter1 == 0:
                            counter += 1
                    counter = 0
                if toreplace == None:
                    return
                with open(self.filename.get(),"r") as replaceit:
                    lines = replaceit.readlines()
                    for x in passon:
                        for y in passon[x]:
                            lines[x] = lines[x][:y] + toreplace + lines[x][y + len(tofind):]
                with open(self.filename.get(),"w") as actuallyreplace:
                    for x in range(len(lines)):
                        actuallyreplace.writelines(lines[x])
                self.load()
        except Exception as e:
            x = messagebox.showerror("G-AIO",f"Failed to find or replace. Error : {e}")
class ErrorGen(Frame):
    def __init__(self,parent,controller):
        self.buttonsoricons = ["showerror","showwarning","showinfo","askokcancel","askquestion","askretrycancel","askyesno","askyesnocancel"]#possible buttons/icons, pretty obvious
        self.icons = ["messagebox.ERROR","messagebox.INFO","messagebox.WARNING","messagebox.QUESTION"]
        self.choices = ["messagebox.","","(","",",",""]
        super().__init__(parent)
        self.controller = controller
        l1 = Label(self,text="Title string : ")
        TString = Entry(self,width=40)
        l2 = Label(self,text="Error message string : ")
        MSGString = Entry(self,width=40)
        ErrorOk = Button(self,text="MSGBOX Show Error",command=lambda: self.u1(),width=40)
        WarningOk = Button(self,text="MSGBOX Show Warning",command=lambda: self.u2(),width=40)
        InfoOk = Button(self,text="MSGBOX Show Info",command=lambda: self.u3(),width=40)
        okcan = Button(self,text="MSGBOX Buttons OK and CANCEL",command=lambda: self.u4(),width=40)
        ques = Button(self,text="MSGBOX QUESTION",command=lambda: self.u5,width=40)
        racecar = Button(self,text="MSGBOX Buttons RETRY and CANCEL",command=lambda: self.u6(),width=40)#some of these names you have to understand by reading the string
        yesrefuse = Button(self,text="MSGBOX Buttons YES and NO",command=lambda: self.u7(),width=40)
        yescancelno = Button(self,text="MSGBOX Buttons YES, NO and CANCEL",command=lambda: self.u8(),width=40)
        useerroricon = Button(self,text="Use ERROR icon",command=lambda: self.i3(),width=40)
        useinfoicon = Button(self,text="Use INFO icon",command=lambda: self.i5(),width=40)
        usewarningicon = Button(self,text="Use WARNING icon",command=lambda: self.i7(),width=40)
        usequestionicon = Button(self,text="Use QUESTION icon",command=lambda: self.i9(),width=40)
        generate = Button(self,text="Generate!",command=lambda: self.gen(TString.get(),MSGString.get()),width=40)
        log = Button(self,text="How to use/About",command=lambda: self.about_htu(),width=40)
        stopbutton = Button(self,text="RESET",command=lambda: self.stop(),width=40)#STOP button is the same one used in this video https://www.youtube.com/watch?v=1Fnso7KcgAw&t=75s
        what = Button(self,text="??",command=lambda: self.w(),width=40)
        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu),width=40)    
        l1.pack()#packing up...
        TString.pack()
        l2.pack()
        MSGString.pack()
        ErrorOk.pack()
        WarningOk.pack()
        InfoOk.pack()
        okcan.pack()
        ques.pack()
        racecar.pack()
        yesrefuse.pack()
        yescancelno.pack()
        useerroricon.pack()
        useinfoicon.pack()
        usewarningicon.pack()
        usequestionicon.pack()
        generate.pack()
        log.pack()
        stopbutton.pack()
        what.pack()
        back_button.pack(pady=10)    
    def w(self):
        app.withdraw()
        x = messagebox.showerror("?","???")
        app.deiconify()
    def stop(self):
            self.buttonsoricons = ["showerror","showwarning","showinfo","askokcancel","askquestion","askretrycancel","askyesno","askyesnocancel"]#possible buttons/icons, pretty obvious
            self.icons = ["messagebox.ERROR","messagebox.INFO","messagebox.WARNING","messagebox.QUESTION"]#possible icons, pretty obvious
            # 1st part of choices = base, 2nd part is the buttonsoricons list that needs to be, 3rd is the parenthesis to start, 4th is msgbox title, 5th is comma, 6th is message string and the (non-existent) 7th part is for the icon 
            self.choices = ["messagebox.","","(","",",",""]#this was part of trying to eval() the thing but got way to complicated and I gave up...
            return
    def u1(self):#U functions. They change the buttons and/or icon. From options 3-7 you need to choose an icon
        self.choices[1] = self.buttonsoricons[0]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u2(self):
        self.choices[1] = self.buttonsoricons[1]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u3(self):
        self.choices[1] = self.buttonsoricons[2]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u4(self):
        self.choices[1] = self.buttonsoricons[3]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u5(self):
        self.choices[1] = self.buttonsoricons[4]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u6(self):
        self.choices[1] = self.buttonsoricons[5]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u7(self):
        self.choices[1] = self.buttonsoricons[6]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u8(self):
        self.choices[1] = self.buttonsoricons[7]
        x = messagebox.showinfo("Info","Complete.")
        return
    def i3(self):# I functions, not because it i9 won't run on an i3, but it changes the icons needed for buttonsoricons 3-7. Note the try/except to do this,which you shouldn't
        try:
            self.choices[6] = self.icons[0]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            self.choices.append(self.icons[0])
            x = messagebox.showinfo("Info","Complete.")
            return
    def i5(self):
        try:
            self.choices[6] = self.icons[1]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            self.choices.append(self.icons[1])
            x = messagebox.showinfo("Info","Complete.")
            return
    def i7(self):
        try:
            self.choices[6] = self.icons[2]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            self.choices.append(self.icons[2])
            x = messagebox.showinfo("Info","Complete.")
            return
    def i9(self):
        try:
            self.choices[6] = self.icons[3]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            self.choices.append(self.icons[3])
            x = messagebox.showinfo("Info","Complete.")
            return
    def gen(self,titl,mst) -> None:#The REAL stuff, this is where generation happens and it's clunky due to the way I made it just work by jamming code...
            app.withdraw()#remove da window
            if self.buttonsoricons[0] == self.choices[1]:
                z = messagebox.showerror(titl,mst)
                app.deiconify()#deiconify() puts back the window after putting the button
                return
            elif self.buttonsoricons[1] == self.choices[1]:
                z = messagebox.showwarning(titl,mst)
                app.deiconify()
                return
            elif self.buttonsoricons[2] == self.choices[1]:
                z = messagebox.showinfo(titl,mst)
                app.deiconify()
                return
            elif self.buttonsoricons[3] == self.choices[1]:
                if self.icons[0] in self.choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.ERROR)
                    app.deiconify()
                    return
                elif self.icons[1] in self.choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.INFO)
                    app.deiconify()
                    return
                elif self.icons[2] in self.choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.WARNING)
                    app.deiconify()
                    return
                elif self.icons[3] in self.choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.QUESTION)
                    app.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                    app.deiconify()
                    return  
            elif self.buttonsoricons[4] == self.choices[1]:
                if self.icons[0] in self.choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.ERROR)
                    app.deiconify()
                    return
                elif self.icons[1] in self.choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.INFO)
                    app.deiconify()
                    return
                elif self.icons[2] in self.choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.WARNING)
                    app.deiconify()
                    return
                elif self.icons[3] in self.choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.QUESTION)
                    app.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                    app.deiconify()
                    return  
            elif self.buttonsoricons[5] == self.choices[1]:
                if self.icons[0] in self.choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.ERROR)
                    app.deiconify()
                    return
                elif self.icons[1] in self.choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.INFO)
                    app.deiconify()
                    return
                elif self.icons[2] in self.choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.WARNING)
                    app.deiconify()
                    return
                elif self.icons[3] in self.choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.QUESTION)
                    app.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                    app.deiconify()
                    return  
            elif self.buttonsoricons[6] == self.choices[1]:
                if self.icons[0] in self.choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.ERROR)
                    app.deiconify()
                    return
                elif self.icons[1] in self.choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.INFO)
                    app.deiconify()
                    return
                elif self.icons[2] in self.choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.WARNING)
                    app.deiconify()
                    return
                elif self.icons[3] in self.choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.QUESTION)
                    app.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                    app.deiconify()
                    return  
            elif self.buttonsoricons[7] == self.choices[1]:
                if self.icons[0] in self.choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.ERROR)
                    app.deiconify()
                    return
                elif self.icons[1] in self.choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.INFO)
                    app.deiconify()
                    return
                elif self.icons[2] in self.choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.WARNING)
                    app.deiconify()
                    return
                elif self.icons[3] in self.choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.QUESTION)
                    app.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                    app.deiconify()
                    return  
            else:
                z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                app.deiconify()
                return
    def about_htu(self):
        x = messagebox.showinfo("Info/HTU","This is the Okmeque1 Error message creator and can generate as many errors as tkinter wants.\n\nTo use this program, you can choose from the 1st 8 buttons BUT from buttons 4-8 you NEED to select an icon. Otherwise generation might fail aswell as your whole computer.")
        return
class not1(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        self.l1 = Label(self,text="Not 1 Game\nScore : 0",font=('Arial',14))
        self.l1.pack(pady=5)
        self.l2 = Label(self,text="Press the desired mode button to start.\nThe computer will randomly generate a number between 1 and 6, and the number chosen will be added to your score. \nIf the number chosen is one, you lose the game\nOn easy mode, your score will not reset to zero when one is chosen\nOn hard mode, your score is set to 0 once you lose.")
        self.l2.pack(pady=5)
        easy = Button(self,text="Not 1 Game - Easy Mode",command=lambda: self.game(False),width=40)
        easy.pack(pady=5)
        hard = Button(self,text="Not 1 Game - Hard Mode",command=lambda: self.game(True),width=40)
        hard.pack(pady=5)
        menu = Button(self,text="Return to Main Menu",command=lambda: controller.show_frame(MainMenu),width=40)
        menu.pack()        
    def game(self,mode):
        pts = 0
        while True:
            number = random.randint(1,6)
            if number == 1:
                if mode == False:
                    self.l1.config(text=f"Not 1 Game - Game Lost\nFinal Score : {pts}")
                    x = messagebox.showerror("G-AIO - Game lost",f"The computer chose 1.\nThe final score is {pts}")
                    return
                else:
                    pts = 0
                    self.l1.config(text=f"Not 1 Game - Game Lost\nFinal Score : {pts}")
                    x = messagebox.showerror("G-AIO - Game lost",f"The computer chose 1.\nThe final score is {pts}")
                    return                    
            else:
                pts += number
                self.l1.config(text=f"Not 1 Game\nScore : {pts}")
                x = messagebox.askyesno("G-AIO",f"The number chosen is {number}. Would you like to continue playing or end the game now?(The next number could be 1)")
                if not x:
                    x = messagebox.showinfo("G-AIO - Game Finished",f"The final score is {pts}")
                    self.l1.config(text=f"Not 1 Game\nFinal Score : {pts}")
                    return
                self.l1.config(text=f"Not 1 Game\nScore : {pts}")
class RPS(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        l1 = tk.Label(self, text="Rock Paper Scissors", font=('Arial', 18, 'bold'))
        l1.pack(pady=10, padx=10)        
        self.p1score = Label(self,text="P1 Score : 0")
        self.p2score = Label(self,text="P2 Score : 0")
        self.p1score.pack(pady=5)
        self.p2score.pack(pady=5)
        b1 = Button(self,text="Play regular version",command=lambda: self.play(0),width=40)#try the new version, the old one is boring why you play it?
        b2 = Button(self,text="Play Okmeque1 Edition",command=lambda:self.play(1),width=40)
        back = Button(self,text="Back to Main Menu",command=lambda: controller.show_frame(MainMenu),width=40)
        b1.pack(pady=5)
        b2.pack(pady=5)
        back.pack() #wait another backpack?
    def play(self,gamemode):
        pts = 0
        pts1 = 0
        mode = simpledialog.askinteger("G-AIO - Setup Players","Please select the number of players.\n[1] for 1 player (vs computer)\n[2] for 2 players.")
        x = messagebox.showinfo("G-AIO","This is the regular rock paper scissor that everybody knows how to play.\nYou will be asked to enter a number for your item. Here's what is means.\n[1] is Rock, which breaks scissors\n[2] is Paper, which breaks rocks\n[3] is Scissors, which breaks Paper.\nIf playing Okmeque1 Edition, then : \n[1] is ROCK, which breaks SCISSORS or BOX KNIFE.\n[2] is PAPER, which breaks ROCK MINER only.\n[3] is SCISSORS, which breaks PAPER only.\n[4] is ROCK MINER, which breaks ROCK only.\n[5] is CARDBOARD, which breaks ROCK and SCISSORS.\n[6] is BOX KNIFE, which breaks PAPER and CARDBOARD.")
        winmap = {1:[3],2:[1],3:[2]} if gamemode == 0 else {1:[3,6], 2:[4], 3:[2], 4:[1], 5:[1,3], 6:[2,5]}#map that determines P1 and P2 score
        gamemap = {0:"Regular",1:"Okmeque1 Edition"}
        gamestr = gamemap[gamemode]
        while True:
            if pts == 10:
                x = messagebox.showinfo("G-AIO","P1 has won the game.")
                self.p1score.config(text=f"P1 is victorious.\nP1 Score : {pts}")
                return
            if pts1 == 10:
                x = messagebox.showinfo("G-AIO","P2 has won the game.")
                self.p2score.config(text=f"P2 is victorious.\nP1 Score : {pts}")
                return
            m1 = simpledialog.askinteger(f"G-AIO RPS - {gamestr} Mode","Enter the item to use. (P1) (Make sure to hide the screen if in 2 player mode.)")
            if mode == 2:
                m2 = simpledialog.askinteger(f"G-AIO RPS - {gamestr} Mode","Enter the item to use (P2) (Did you look at P1's move?)")
            else:
                m2 = random.randint(1,3) if gamemode == 0 else random.randint(1,6)
            if m1 == None or m2 == None:
                return
            if m2 in winmap[m1]:
                pts += 1
                self.p1score.config(text=f"P1 Score : {pts}")
                x = messagebox.showinfo(f"G-AIO RPS - {gamestr} Mode",f"P1 has gained a point.\nCurrent Scores : \nP1 : {pts}\nP2 : {pts1}\nP1 Move : {m1}\nP2 Move : {m2}")
            elif m1 in winmap[m2]:#pretty easy to understand, checks if an item is in the dict key.
                pts1 += 1
                self.p2score.config(text=f"P2 Score : {pts}")
                x = messagebox.showinfo(f"G-AIO RPS - {gamestr} Mode",f"P2 has gained a point.\nCurrent Scores : \nP1 : {pts}\nP2 : {pts1}\nP1 Move : {m1}\nP2 Move : {m2}")
            else:
                x = messagebox.showinfo(f"G-AIO RPS - {gamestr} Mode",f"Nothing happened.\nCurrent Scores : \nP1 : {pts}\nP2 : {pts1}\nP1 Move : {m1}\nP2 Move : {m2}")
class Calculator(Frame):#please kill me, this took far faaaaaaaarrrrrr tooo long.
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        self.calculation = ""       
        self.clearall = 1
        l0 = tk.Label(self, text="Calculator", font=('Arial', 18, 'bold'))
        l0.pack(pady=10, padx=10) 
        b1 = Button(self,text="1",width=13,height=3,command=lambda: self.addchar("1"))
        b2 = Button(self,text="2",width=13,height=3,command=lambda: self.addchar("2"))
        b3 = Button(self,text="3",width=13,height=3,command=lambda: self.addchar("3"))
        b4 = Button(self,text="4",width=13,height=3,command=lambda: self.addchar("4"))
        b5 = Button(self,text="5",width=13,height=3,command=lambda: self.addchar("5"))
        b6 = Button(self,text="6",width=13,height=3,command=lambda: self.addchar("6"))
        b7 = Button(self,text="7",width=13,height=3,command=lambda: self.addchar("7"))
        b8 = Button(self,text="8",width=13,height=3,command=lambda: self.addchar("8"))
        b9 = Button(self,text="9",width=13,height=3,command=lambda: self.addchar("9"))
        b0 = Button(self,text="0",width=40,command=lambda: self.addchar("0"))
        self.num1 = ""
        self.displaycurrentnum = Label(self,text="")
        self.calcstr = Label(self,text="Final Calculation : ")
        add = Button(self,text="+",width=40,command=lambda: self.addchar("+"))
        sub = Button(self,text="-",width=40,command=lambda: self.addchar("-"))
        mul = Button(self,text="*",width=40,command=lambda: self.addchar("*"))
        div = Button(self,text="/",width=40,command=lambda: self.addchar("/"))
        sqr = Button(self,text="SQRT",width=40,command=lambda: self.squareroot())
        pwr = Button(self,text="EXPONENT",width=40,command=lambda: self.exponent())
        pie = Button(self,text="PI (3.1415926535)",width=40,command=self.pi)
        bksp = Button(self,text="BACKSPACE (PRESS 3 TIMES TO CLEAR)",width=40,command=lambda:self.clear(True))
        cls = Button(self,text="DECIMAL POINT",width=40,command=lambda: self.addchar("."))
        calc = Button(self,text="Calculate",width=40,command=self.calculate)
        about = Button(self,text="Back to Main Menu",width=40,command=lambda: controller.show_frame(MainMenu))
        self.calcstr.pack()
        self.displaycurrentnum.pack()
        b1.place(x=268,y=108)
        b2.place(x=357,y=108)
        b3.place(x=446,y=108)
        b4.place(x=268,y=171)
        b5.place(x=357,y=171)
        b6.place(x=446,y=171)
        b7.place(x=268,y=234)
        b8.place(x=357,y=234)
        b9.place(x=446,y=234)
        b0.place(x=268,y=297)
        add.place(x=268,y=322)
        sub.place(x=268,y=347)
        mul.place(x=268,y=372)
        div.place(x=268,y=397)
        sqr.place(x=268,y=422)
        pwr.place(x=268,y=447)
        pie.place(x=268,y=472)
        bksp.place(x=268,y=497)
        cls.place(x=268,y=522)
        calc.place(x=268,y=547)
        about.place(x=268,y=572)
    def clear(self,parameter):
        if parameter:
            if self.clearall == 3:
                self.clearall = 0
                self.clear(False)
            self.calculation = self.calculation[:-1]
            self.num1 = self.num1[:-1]
            self.calcstr.config(text=f"Final Calculation : {self.calculation}")
            self.displaycurrentnum.config(text=f"{self.num1}")
            self.clearall += 1
        else:
            self.calculation = ""
            self.num1 = ""
            self.displaycurrentnum.config(text="")
            self.calcstr.config(text=f"Final Calculation : ")
    def about(self):
        x = messagebox.showinfo("G-AIO - Calculator Function","The NUM1 Parameter is required to be filled with something at all times.\n\nThe buttons will clear the input field to let you enter something else. Between every number, you need to press a button to indicate your calculation.\n\nThe SQRT and EXPONENT work by taking in the number underneath the final calculation label, but the exponent will ask to expand to your desired number.\n\nThe PI button will give a rough approximation of 3.1415926535 and add it to your calculation.\n\n")
    def addchar(self,char):
        self.clearall = 0
        digits = "1234567890."
        if char not in digits:
            self.num1 = ""
            self.displaycurrentnum.config(text="")
        else:
            self.num1 = str(self.num1)
            self.num1 += char
            self.displaycurrentnum.config(text=f"{self.num1}")
        self.calculation += char
        self.calcstr.config(text=f"Final Calculation : {self.calculation}")
        return
    def squareroot(self):
        try:
            print(self.num1)
            num = float(self.num1)
            sqrted = math.sqrt(num)
            x = messagebox.askyesno("G-AIO",f"The square root of {num} is {sqrted}. Would you like to add that to your calculation?")
            if x:
                try:
                    self.calculation = int(self.calculation)
                except:
                    pass
                self.clear(True)
                self.calculation = str(sqrted)
                self.num1 = sqrted
                self.displaycurrentnum.config(text=f'{self.num1}')
                self.calcstr.config(text=f"Final Calculation : {self.calculation}")
        except Exception as e:
            x = messagebox.showerror("G-AIO",f"Failed to SQRT {self.num1}. Reason : {e}")
    def exponent(self):
        self.clearall = 0
        expand = simpledialog.askinteger("G-AIO",f"{self.num1} shall be to the power of... ")
        toreturn = float(self.num1)
        toreturn = int(self.num1) ** expand
        x = messagebox.askyesno("G-AIO",f"The expanded form of {self.num1} to the power of {expand} is {toreturn}. Would you like to add that to your calculation?")
        if x:
                temp = float(self.num1)
                temp += toreturn
                temp -= float(self.num1)
                self.clear(True)
                self.calculation += str(temp)
                self.calcstr.config(text=f"Final Calculation : {self.calculation}")
    def pi(self):
        self.clearall = 0
        self.calculation += "3.1415926535"
        self.num1 += "3.1415926535"
        self.displaycurrentnum.config(text=f'{self.num1}')
        self.calcstr.config(text=f"Final Calculation : {self.calculation}")      
    def calculate(self):
        self.clearall = 0
        try:
            result = eval(f"{self.calculation}")
            x = messagebox.showinfo("G-AIO",f"The result is {result}")
            self.calcstr.config(text=f"Final Calculation : {self.calculation}\nResult : {result}")
        except Exception as e:
            x = messagebox.showerror("G-AIO - Calculation Failed",f"The calculation has failed. Please check the format and the characters used.\nError : {e}\nOriginal Calculation : {self.calculation}")
class OpenTDB(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        self.l1 = Label(self,text="Points : 0",font=('Arial',14))
        self.l1.pack(pady=5)
        self.l2 = Label(self,text="When using setup, the setup prompts may be behind the app window.")
        self.l2.pack(pady=5)
        play = Button(self,text="Play!",command = lambda: self.setup(),width=40)
        play.pack(pady=5)
        back = Button(self,text="Back to main menu", command=lambda: controller.show_frame(MainMenu),width=40)
        back.pack(pady=5)
    def setup(self):
        try:
            x = messagebox.showinfo("G-AIO - Credits","OpenTDB API - By OpenTDB Corp - Licensed under CC BY-SA 4.0. All copies of this program shall mention OpenTDB Corp.")
            numquestion = simpledialog.askinteger("Setup - Question number","Enter number of questions")
            difselect = simpledialog.askstring("Setup - Difficulty Selection","Please select the difficulty by typing the letters in brackets\n[A]ny\n[E]asy\n[M]edium\n[H]ard")
            difmap = {"A":"Any","E":"easy","M":"medium","H":"hard"}
            difselect = difmap[difselect.upper()]
            catselect = simpledialog.askinteger("Setup - Category Selection","""
    0 : Random
    1 : General knowledge
    2 : Books
    3 : Films
    4 : Music
    5 : Music/Teathrals
    6 : Television  
    7 : Video games
    8 : Board games
    9 : Science and nature
    10 : Computer science
    11 : Mathematics science
    12 : Mythology
    13 : Sports
    14 : Geography
    15 : History
    16 : Politics
    17 : Arts
    18 : Celebrities
    19 : Animals
    20 : Vehicles
    21 : Comics
    22 : Gadget science
    23 : Manga/Anime
    24 : Cartoon/Animations
                                                            """) + 8
            typeselect = simpledialog.askstring("G-AIO - Setup Question Type","Please select the question type by typing the letter in brackets.\n[M]ultiple Choice\n[T]rue or False")
            typemap =  {"A":"Any","M":"multiple","T":"boolean"}
            typeselect = typemap[typeselect.upper()]
            questionget = self.geturl(numquestion,difselect,catselect,typeselect)
            automode = messagebox.askyesno("G-AIO - Setup mode","Do you want to enable auto mode?\nAuto mode is a feature where you do not need to select the question, program will do it automatically for you.")
            automap = {True:"Y",False:"N"}
            automode = automap[automode]
            forgivemode = messagebox.askyesno("G-AIO - Setup mode","Do you want to enable forgiveness mode?\nForgiveness mode is a feature where you can redo your failed questions.") if automode == "N" else "N"
            forgivemap = {True:"Y","N":"N",False:"N"}
            forgivemode = forgivemap[forgivemode]
            game = True
            done = []
            pts = 0
            choosequstion = 0
            while game == True:#the actual game. has lots of modes for different things
                self.l1.config(text=f"You have {pts} points.")
                if pts == numquestion:
                    x = messagebox.showinfo("G-AIO - Game Won","You won! Returning to main menu")
                    self.l1.config(text=f"Game Won! You have {pts} points")
                    return
                if automode == "Y":
                    if choosequstion == numquestion:
                        x = messagebox.showerror("G-AIO - Game Lost",f"You lost\nBy a mistake.\nPoints : {pts}")
                        self.l1.config(text="Game Lost!")
                        self.l2.config(text=f"By a mistake.\nPoints : {pts}")
                        return
                    question = html.unescape(str(questionget["results"][choosequstion]["question"]).replace("&quot;","'"))
                    if questionget["results"][choosequstion]["type"] == "multiple":
                        lcorrect = str(questionget["results"][choosequstion]["correct_answer"])
                        l1 = [questionget["results"][choosequstion]["correct_answer"]] + questionget["results"][choosequstion]["incorrect_answers"]
                        random.shuffle(l1)
                        O1 = l1[0]
                        O2 = l1[1]
                        O3 = l1[2]
                        O4 = l1[3]
                        answer = simpledialog.askinteger("G-AIO - Enter answer",f"{question}\nOption 1 : {O1}\nOption 2 : {O2}\nOption 3 : {O3}\nOption 4 : {O4}\nPlease enter the number corresponding to the correct answer.")
                        if l1[answer - 1] == lcorrect:
                            pts += 1
                            done.append(questionget["results"][choosequstion])
                            a = messagebox.showinfo("G-AIO - Correct Answer","Correct answer. 1 point added.")
                            choosequstion += 1
                        else:
                            correct = question["results"][choosequstion]["correct_answer"]
                            a = messagebox.showerror("G-AIO - Incorrect Answer",f"Incorrect answer. Correct answer was {correct}")
                            choosequstion += 1
                    else:
                        answer = simpledialog.askstring("G-AIO - Answer Question",f"{question}\n(T)rue/(F)alse? : ")
                        answer = answer.upper()
                        tfmap = {"T":"True","F":"False"}
                        answer = tfmap[answer]
                        if answer == questionget["results"][choosequstion]["correct_answer"]:
                            pts += 1
                            done.append(questionget["results"][choosequstion])
                            choosequstion += 1
                            a = messagebox.showinfo("G-AIO - Correct Answer","Correct answer. 1 point added.")
                        else:
                            correct = question["results"][choosequstion]["correct_answer"]
                            a = messagebox.showerror("G-AIO - Incorrect Answer",f"Incorrect answer. Correct answer was {correct}")
                            choosequstion += 1
                else:       
                    
                    choosequstion = simpledialog.askinteger("G-AIO - Select Question","You have selected : " + str(numquestion) + " questions and have to choose. Please choose the question number with the minimum being 1 and the maximum being the number you chose. \nEnter -1 to resign.")
                    if choosequstion == -1:
                        self.l1.config(text="Game lost!")
                        self.l2.config(text=f"By resignation.\nPoints : {pts}")
                        return
                    choosequstion = choosequstion - 1 
                    if questionget["results"][choosequstion] in done:
                        messagebox.showinfo("G-AIO - Completed","You have already completed this question before.")
                    question = str(questionget["results"][choosequstion]["question"]).replace("&quot;","'")
                    if questionget["results"][choosequstion]["type"] == "multiple":
                        lcorrect = str(questionget["results"][choosequstion]["correct_answer"])
                        l1 = [questionget["results"][choosequstion]["correct_answer"]] + questionget["results"][choosequstion]["incorrect_answers"]
                        random.shuffle(l1)
                        O1 = l1[0]
                        O2 = l1[1]
                        O3 = l1[2]
                        O4 = l1[3]
                        answer = simpledialog.askinteger("G-AIO - Enter answer",f"{question}\nOption 1 : {O1}\nOption 2 : {O2}\nOption 3 : {O3}\nOption 4 : {O4}\nPlease enter the number corresponding to the correct answer.")
                        if l1[answer - 1] == lcorrect:
                            pts += 1
                            done.append(questionget["results"][choosequstion])
                            a = messagebox.showinfo("G-AIO - Correct Answer","Correct answer. 1 point added.")
                        else:
                            if forgivemode == "N":
                                done.append(questionget["results"][choosequstion])
                            a = messagebox.showerror("G-AIO - Incorrect Answer","Incorrect answer.")
                    else:
                        answer = simpledialog.askstring("G-AIO - Answer Question",f"{question}\n(T)rue/(F)alse? : ")
                        if answer == questionget["results"][choosequstion]["correct_answer"]:
                            pts += 1
                            done.append(questionget["results"][choosequstion])
                            a = messagebox.showinfo("G-AIO - Correct Answer","Correct answer. 1 point added.")
                        else:
                            if forgivemode == "N":
                                done.append(questionget["results"][choosequstion])
                            a = messagebox.showerror("G-AIO - Incorrect Answer","Incorrect answer.")         
        except Exception as e:
            x = messagebox.showerror("G-AIO - Setup OpenTDB",f"Game or Setup failed. Error {e}")
    def geturl(self,amount=1,difficulty="easy",category=9,typee="multiple"):#geturl function calls opentdb.com and returns what it responds in JSON
        returnstring = "https://opentdb.com/api.php"
        returnstring += "?amount=" + str(amount)
        returnstring += "&category=" + str(category)
        returnstring += "&difficulty=" + difficulty
        returnstring += "&type=" + typee
        print(returnstring)
        returnurl = requests.get(returnstring)
        return html.unescape(returnurl.json())

class GamesMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Games Menu.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        tic_tac_toe_button = tk.Button(self, text="Tic-Tac-Toe.", command=self.play_tic_tac_toe,width=40)
        tic_tac_toe_button.pack(pady=5)
        opentdb = Button(self,text="Open Trivia Questions",command=lambda: controller.show_frame(OpenTDB),width=40)
        opentdb.pack(pady=5)
        not1game = Button(self,text="Not 1 Game",command=lambda: controller.show_frame(not1),width=40)
        not1game.pack(pady=5)
        errgen = Button(self,text="Error Generator",command=lambda: controller.show_frame(ErrorGen),width=40)
        errgen.pack(pady=5)
        rock = Button(self,text="Rock Paper Scissors",command=lambda: controller.show_frame(RPS),width=40)
        rock.pack(pady=5)
        hng = Button(self,text="Hang-Man",command=lambda: controller.show_frame(HangMan),width=40)
        hng.pack(pady=5)
        gn = Button(self,text="Guess the Number",command=lambda: controller.show_frame(GuessNumber),width=40)
        gn.pack(pady=5)# No, GN does not refer to Gamers Nexus, or Tech Jesus
        wff = Button(self,text="Windows File Format Game",command=self.windowsformatgame,width=40)
        wff.pack(pady=5)
        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu),width=40)
        back_button.pack(pady=10)

    def play_tic_tac_toe(self):
        self.controller.show_frame(TicTacToe)
    def windowsformatgame(self):
        character_set = 'Â¦Â¬`1!23Â£4$â‚¬5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'
        orgstr = ""
        for x in range(71):
            orgstr += random.choice(character_set)
        invalid_chars = ["|","\\",":","*","?","/","<",">",'"']
        for x in invalid_chars:
            corrected_str = orgstr.replace(x,"")
        x = simpledialog.askstring("Windows File Format Game",f"Put the string '{orgstr}' in a Windows Compatible File format).")
        if x == corrected_str:
            x = messagebox.showinfo("Windows File Format Game","Game Won, not bad eh")
        else:
            y = messagebox.showerror("Windows File Format Game",f"The string {x} is not a valid Windows File Format: Either too many characters were removed or invalid characters were kept.")

class TicTacToe(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.board = [" " for _ in range(9)]
        self.current_player = "X"

        label = tk.Label(self, text="Tic-Tac-Toe.", font=('Arial', 18, 'bold'))
        label.pack(pady=10)

        self.buttons = []
        for i in range(3):
            row_frame = tk.Frame(self)
            row_frame.pack()
            for j in range(3):
                button = tk.Button(row_frame, text=" ", font=('Arial', 20, 'bold'), width=8, height=4,
                                   command=lambda row=i, col=j: self.click(row, col))
                button.pack(side="left", padx=5, pady=5)
                self.buttons.append(button)

        #reset_button = tk.Button(self, text="Reset.", command=self.reset_game)
        #reset_button.pack(pady=10)

        back_button = tk.Button(self, text="Back to Games Menu.", command=lambda: controller.show_frame(GamesMenu),width=40)
        back_button.pack(pady=10)

    def click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe.", f"{self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tic-Tac-Toe.", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"
class HangMan(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Hang-Man", font=('Arial', 18, 'bold'),width=40)
        label.pack(pady=10, padx=10)  
        l1 = Label(self,text="You will have to guess the individual letters of a word to win, you have 8 wrong chances.")
        l1.pack(pady=5)      
        self.l2 = Label(self)
        self.l2.pack(pady=5)
        play = Button(self,text="Play!",command=lambda: self.hangman(requests.get("https://random-word-api.herokuapp.com/word").json()[0]),width=40)
        play.pack(pady=5)
        offline = Button(self,text="Legacy Offline Mode",command=lambda: self.hangman(random.choice(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon","car","chair","table","computer","dog","cat","football"])),width=40)
        offline.pack(pady=5) #word list from https://github.com/GamerSoft24/Software/blob/Main/PySoft/Games/hangman.py
        back = Button(self,text="Back to main menu", command=lambda: controller.show_frame(MainMenu),width=40)
        back.pack(pady=5) #backpack again for school season (written august 2024)
    def hangman(self,wrd):
        try:
            word = wrd
            wordlist = list(word)
            guesslist = ["-" for x in range(len(word))]
            wrong = 0
            success = False
            while wrong != 8:
                success = False
                if guesslist == wordlist:
                    x = messagebox.showinfo("G-AIO - Game won","You won!")
                    self.l2.config(text="Game Won!\nBy guessing the word.")
                    return
                guess = simpledialog.askstring("G-AIO",f"Enter a letter to guess. You may only enter 1 letter at a time, noting that everything is in lowercase. The length of the word is {len(word)}\nIf you think you know the whole word, you may play a gambit and tru to guess it. But if you guess incorrectly, you will lose the entire game.")
                if guess is None:
                    self.l2.config(text="Game abandoned.")
                    return
                if len(guess) == 0:
                    x = messagebox.showerror("G-AIO","Guess cannot be empty.\nIf you thought you could cheat due to a bug in this game, now you can't.") #naughty naughty.
                elif len(guess) > 1:
                    if guess == word:
                        x = messagebox.showinfo("G-AIO - Achievement Unlocked","You have guessed correctly!\nAchievement Unlocked : Mad Guesser.")
                        self.l2.config(text="Game Won!\nBy guessing the word on the first try.")
                        return
                    else:
                        x = messagebox.showerror("G-AIO",f"You guessed incorrectly. The word was {word}")
                        self.l2.config(text="Game Lost!\nBy failing to guess the word on the first try.")
                        return
                else:
                    wdlist = "".join(guesslist)
                    for x in range(len(wordlist)):
                        if guess in wordlist[x]:
                            guesslist[x] = wordlist[x]
                            wdlist = "".join(guesslist)
                            x = messagebox.showinfo("G-AIO",f"Correct at {x + 1}\n\nFilled : '{wdlist}'")
                            success = True
                    if success != True:
                        x = messagebox.showerror("G-AIO",f"Incorrect guess.\nRemaining guesses : {8-wrong}\nFilled : '{wdlist}'")
                        wrong += 1 
            x = messagebox.showerror("G-AIO - Game Lost",f"You lost by incorrect answers. The word was {word}")
            self.l2.config(text=f"Game Lost!\nBy making too many mistakes. The word was {word}")
        except Exception as e:
            x = messagebox.showerror("G-AIO",f"Failed to play game 'HANG-MAN'. Error : {e}")



class ToolsMenu(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Tools Menu", font=('Arial', 18, 'bold'),width=40)
        label.pack(pady=10, padx=10)   
        pwd = Button(self, text="Password Manager", command=lambda: controller.show_frame(PassManager),width=40)
        pwd.pack(pady=5)
        smsr = Button(self, text="Remove Start Menu Search Results",command=lambda: self.start(),width=40)#Windows Only, removes bing search results     
        smsr.pack(pady=5)
        verbose_msg = Button(self,text="Enable Verbose (detailed) boot messages",command=self.verbose_boot,width=40)
        verbose_msg.pack(pady=5)
        uacb = Button(self,text="UAC Bypass",command=lambda: self.uacbypass(),width=40)
        uacb.pack(pady=5)
        encsuite = Button(self,text="Encryption Suite",command=lambda: self.encryption(),width=40)
        encsuite.pack(pady=5)
        calc = Button(self,text="Calculator",command=lambda: controller.show_frame(Calculator),width=40)
        calc.pack(pady=5)
        diskmgr = Button(self,text="Disk Manager (in testing stage)", width=40, command=self.dm)
        diskmgr.pack(pady=5)
        back = Button(self,text="Back to main menu", command=lambda: controller.show_frame(MainMenu),width=40)
        back.pack(pady=5) #it's a backpack!
    def start(self):
        if os.name != 'nt':
            x = messagebox.showwarning("G-AIO","The 'Windows Start Menu Internet Search Results Remover' is not compatible with your operating system.")
            return
        a = os.system("reg add HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Explorer /v DisableSearchBoxSuggestions /t REG_DWORD /d 1 /f")
        if a != 0:
            x = messagebox.showerror("G-AIO","Please run this program with admin privileges for this function to work properly.")
        else:
            x = messagebox.askyesno("G-AIO","The operation has completed successfully. For the changes to take effect, the Windows Explorer must be restarted and will take a few moments. Restart?",icon=messagebox.QUESTION)
            if x:
                os.system('taskkill /f /im explorer.exe')
                os.system('explorer')
    def dm(self):
        x = messagebox.showwarning("G-AIO","The disk manager is not fully operational nor stable.\n\nBy continuing, you acknowledge that you are responsible for all actions and that the developers are not liable for any damages, as said in the GitHub GamerSoft24/Software repository licenses and warranty agreements.")
        self.controller.show_frame(Diskpart)
    def verbose_boot(self):
        if os.name != 'nt':
            x = messagebox.showwarning("G-AIO","Verbose Boot messages is not compatible with your operating system.")
            return
        a = os.system("reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v VerboseStatus /t REG_DWORD /d 1 /f")
        if a != 0:
            x = messagebox.showerror("G-AIO","Please run this program with admin privileges for this function to work properly.")
        else:
            x = messagebox.showinfo("G-AIO","Verbose Boot Messages have been enabled.")        

    def uacbypass(self):
        program = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if program:
            try:
                result = subprocess.run(f'cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "{program}"', shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    return
                else:
                    x=messagebox.showerror("G-AIO - Bypass Failed",f"Failed to bypass UAC. Error {result.stderr}")
            except Exception as e:
                x = messagebox.showerror("G-AIO", f"Failed to start program. Error: {str(e)}.")      
    def encryption(self):
        try:
            askkey = messagebox.askyesno("G-AIO","Do you have an encryption key?\nAn encryption key is used to lock and unlock a file.\nNote that only G-AIO (or Fernet-style) keys will work.")
            if not askkey:
                    key = Fernet.generate_key()
                    with open(filedialog.asksaveasfilename(filetypes=[("Fernet Key Files", "*.frn")]),"wb") as writekey:
                        writekey.write(key)
            askmode = messagebox.askyesno("G-AIO - Select Mode","Do you want to lock or unlock a file?\nPress YES for LOCKING\nPress NO for UNLOCKING")
            filename = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
            with open(filedialog.askopenfilename(filetypes=[("Fernet Key Files", "*.frn")]),"rb") as validkey:
                valdkey = validkey.read()
                if askmode:
                    with open(filename,"rb") as enc:
                        lock = enc.read()
                    actualkey = Fernet(valdkey)
                    encrypted = actualkey.encrypt(lock)
                    with open(filename,"wb") as encrypting:
                        encrypting.write(encrypted)
                    x = messagebox.showinfo("G-AIO - Operation Successful","The file has been encrypted successfully.")
                    return
                else:
                    with open(filename,"rb") as dec:
                        unlock = dec.read()
                    actualkey = Fernet(valdkey)
                    decrypted = actualkey.decrypt(unlock)
                    with open(filename,"wb") as decrypting:
                        decrypting.write(decrypted)
                    x = messagebox.showinfo("G-AIO - Operation Successful","The file has been decrypted successfully.")
                    return
        except Exception as e:
            x = messagebox.showerror("G-AIO - Operation failed",f"The encryption suite did not complete successfully. Error : {e}")
class GuessNumber(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller = controller
        l1 = Label(self,text="Guess the Number", font=('Arial',18,'bold'))
        l1.pack(pady=10,padx=10)#game from https://github.com/GamerSoft24/Software/blob/Main/PySoft/Games/guess%20a%20number%20(top%20100).py
        l2 = Label(self,text="Â© GamerSoftware Corporation\nSettings\nNumber 1")
        self.num1 = Entry(self,width=40)
        l2.pack(pady=5)
        self.num1.pack(pady=5)
        l3 = Label(self,text="Number 2")
        l3.pack(pady=5)
        self.num2 = Entry(self,width=40)
        self.num2.pack(pady=5)
        play = Button(self,text="Play!",width=40,command=self.guessnum)
        play.pack(pady=5)
        b4 = Button(self,text="Back to Main Menu",command=lambda: controller.show_frame(MainMenu),width=40)
        b4.pack(pady=5)
    def guessnum(self):
        num1 = int(self.num1.get())
        num2 = int(self.num2.get())
        if num1 >= num2:
            x = messagebox.showerror("G-AIO","Value of Number 1 needs to be smaller and not equal to value of Number 2")
            return
        number = random.randint(num1,num2)
        guess = 0
        tries = 0
        while guess != number:
            tries += 1
            guess = simpledialog.askinteger("G-AIO","Enter your guess")
            if guess > number:
                x = messagebox.showerror("G-AIO","Incorrect guess. Your number is too high.")
            elif guess < number:
                x = messagebox.showerror("G-AIO","Incorrect guess. Your number is too low.")
            elif not guess:
                return
        x = messagebox.showinfo("G-AIO",f"Correct! It took you {tries} tries.")
        return
                


class PassManager(Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)   
        self.controller = controller
        label = tk.Label(self, text="Password Manager", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)   
        b1 = Button(self,text="Generate password",command=lambda: self.gen(""),width=40)
        b1.pack(pady=5)
        b2 = Button(self,text="Retrieve password",command=lambda: self.retrieve(),width=40)
        b2.pack(pady=5)
        b3 = Button(self,text="List passwords",command=lambda: self.showall(),width=40)
        b3.pack(pady=5)
        b5 = Button(self,text="Advanced password generation",command=lambda: self.advanced(),width=40)
        b5.pack(pady=5)
        b4 = Button(self,text="Back to Main Menu",command=lambda: controller.show_frame(MainMenu),width=40)
        b4.pack(pady=5)
        self.t1 = Text(self,width=80,height=19)
        self.t1.pack(pady=10)
    def gen(self,setname1):
        charlen = simpledialog.askinteger("G-AIO","Enter password length")
        print(setname1)
        if setname1 == "": #originally I put != "" because... well idk really, just brainrot moment.
            setname = simpledialog.askstring("G-AIO","Enter password name")
        else:
            setname = setname1

        charset = 'Â¦Â¬`1!23Â£4$â‚¬5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'
        pwd = ""
        for x in range(charlen):
            pwd += random.choice(charset)
        filename = simpledialog.askstring("G-AIO","Please enter a valid file name. The format must be 'A:\Directory\Subdirectory\file.extension'.")
        try:
            with open(filename,"a") as add:
                add.write(f"\n{setname} -> {pwd}")
                x = messagebox.showinfo("G-AIO","Generated and saved successfully")
        except Exception as e:
            x = messagebox.showerror("G-AIO - Save failed",f"Save failed. Error : {e}")
    def retrieve(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            with open(filename,"r") as passopen:
                set1 = simpledialog.askstring("G-AIO","Enter password name")
                success = False
                for line in passopen:
                    if line.split(" -> ")[0] == set1:
                        success = True
                        x = messagebox.showinfo("G-AIO","The password is " + str({line.split(" -> ")[1]}))   
                        self.t1.delete("1.0",END)
                        self.t1.insert(END,"The password for the password name is ")
                        self.t1.insert(END,line.split(" -> ")[1])
                        return
                if success != True:
                    gotogen = messagebox.askquestion("G-AIO",f"The password '{set1}' does not exist. \nWould you like to create it?")
                    if gotogen == 'yes':#stupid function return 
                        self.gen(set1)
                    else:
                        gotogen = messagebox.showerror("G-AIO","The password could not be loaded.\nThe requested password was not found.")
    def showall(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filename:
            with open(filename,"r") as listall:
                self.t1.delete("1.0",END)
                self.t1.insert(END,"The passwords for this file are :\n")
                self.t1.insert(END,listall.read())
    def advanced(self):
        numbers = "1234567890"
        lwc = "qwertyuiopasdfghjklzxcvbnm"
        upc = "QWERTYUIOPASDFGHJKLZXCVBNM"
        spc = "`!$%^&*()_+-={}[]:;@'~#|<,>.?/"
        pwd = ""
        mix = ""
        x = messagebox.showwarning("G-AIO - User Warning","Note that the following values you will enter for your password will not be 100% accurate due to the mixing logic of this program.\nIf you want 5 digits in your password, you may only have 4 or 6.")
        for x in range(simpledialog.askinteger("G-AIO","Please enter the number of special characters for your password.")):
            pwd += random.choice(spc)
        for x in range(simpledialog.askinteger("G-AIO","Please enter the number of lowercase characters for your password")):
            pwd += random.choice(lwc)
        for x in range(simpledialog.askinteger("G-AIO","Please enter the number of uppercase characters for your password")):
            pwd += random.choice(upc)
        for x in range(simpledialog.askinteger("G-AIO","Please enter the number of digits in your password")):
            pwd += random.choice(numbers)
        for x in range(len(pwd)):
            mix += random.choice(pwd)
        with open(filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]),"a") as writing:
            writing.write(f"\n{mix}")
        x = messagebox.showinfo("G-AIO","The password has generated and saved successfully")
        return
if __name__ == "__main__":#uarte the martin víglen Nxd6+ blunder
        try:
            if len(sys.argv) > 1:
                if sys.argv[1] == "--setup":
                    a = os.system("reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v VerboseStatus /t REG_DWORD /d 1 /f")
                    b = os.system(f"copy {os.path.abspath(__file__)} C:\\WinAIO\\G-AIO.PY")
                    if len(sys.argv) > 2:
                        c = os.system(f'reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "{sys.argv[2][21:]} C:\\WinAIO\\G-AIO.py" /f')
                    else:    
                        c = os.system('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "C:\Windows\py.exe C:\\WinAIO\\G-AIO.py" /f')
                    if a != 0 or b != 0 or c != 0:
                        d = messagebox.showerror("WinAIO Setup","An error has occured while configuring your computer. Please see the terminal logs for more information (usually the black window with text).\n\nSetup will now exit.")
                        exit()
                    d = messagebox.askyesno("WinAIO Setup","Setup has finished configuring your computer. For the changes to take effect, you must restart your computer. Do you wish to do that now?")
                    if d:
                        os.system("shutdown /r /t 0 ")
                    else:
                        exit()
                if sys.argv[1] == "--unsetup":
                    a = os.system('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d C:\WINDOWS\EXPLORER.EXE /f')
                    if a != 0:
                        d = messagebox.askyesno("WinAIO Setup","Setup failed to configure your computer. Do you want to retry the operation?\n\nThe program will ")
                    d = messagebox.askyesno("WinAIO Setup","Setup has finished configuring your computer. For the changes to take effect, you must restart your computer. Do you wish to do that now?")
                    if d:
                        os.system("shutdown /r /t 0 ")
                    else:
                        exit()
                if sys.argv[1] == "--rd":
                    a = os.system("rd /q /s C:\\WinAIO")
                    if a == 0:
                        x = messagebox.showinfo("WinAIO Removal","Removal of C:\\WinAIO successful.")
                    else:
                        x = messagebox.showerror("WinAIO Removal","Error while removing C:\\WinAIO. Please see the logs for more info (usually the command line or the Python interpeter, usually seen with a snake icon)")              
            app = AssistantApp()
            app.geometry("800x600")
            app.resizable(width=False,height=False)
            app.mainloop()
        except SystemExit():
            exit("User has chosed to exit. Exiting...")
        except (ModuleNotFoundError,ImportError) as e:
            x = messagebox.showerror("G-AIO",f"A required module is not installed or an error has occured while importing it/\nError: {e}\nPlease make sure that all dependencies are installed as per the GitHub GamerSoft24/Software/PySoft requirements.txt requirements file. Read the README in that same folder for more information.\nThe program will exit.")
            exit()
        except Exception as e:
            x = messagebox.askyesno("G-AIO",f"An error has occured in G-AIO.\nError details: {e}\nAny data that was not save was lost. Do you want to restart the program?",icon=messagebox.ERROR)
            if x:
                os.system(f'start "" {os.path.abspath(__file__)}')
                exit()
            else:
                exit()
