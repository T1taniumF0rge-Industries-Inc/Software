import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
def generate(length,filename,setname):
    chars = '¦¬`1!23£4$€5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~#\|zZxXcCvVbBnNmMm,<.>/?'
    try:
        endpass = ""
        length = int(length)
        for x in range(length):
            endpass += random.choice(chars)
        if filename == "":
            filename = "G:\python\demo\demo.pc"
        with open(filename,"a") as writing:
            writing.write(setname + " -> " + endpass + "\n")
            x = messagebox.showinfo("GUI-PWD","Saved.")
            return
    except ValueError:
        x = messagebox.showerror("GUI-PWD","Save failed.Enter a valid number(1,53,45645) and try again.\nError code : 0211")
        return
    except FileNotFoundError:
        x = messagebox.showerror("GUI-PWD","Save failed.Make sure the file exists and try again\nError code : 6510B")
        return
    except BaseException:
        x = messagebox.showerror("GUI-PWD","Save failed.Check parameters and try again\nError code : 770A")
        return
def retrieve(filename,setname):
    if filename == "":
        filename = "G:\python\demo\demo.pc"
    try:
        with open(filename,"r") as reading:
                reding = reading.readlines()
                for line in reding:
                    print(line)
                    if line.split(" -> ")[0] == setname and line.split(" -> ")[1] != "":
                        displaypass.delete("1.0",END)
                        displaypass.insert(END,line.split(" -> ")[1])
                        print(line.split(" -> ")[1])
                        return
    except FileNotFoundError:
        x = messagebox.showerror("GUI-PWD","Load failed.Make sure the file exists and try again.\nError code : 6510B")
        return
    except BaseException:
        x = messagebox.showerror("GUI-PWD","Load failed.Check parameters and try again\nError code : 770A")
def realdelete(state,filename):
    import os
    if state == True:
        try:
            os.remove(filename)
            x = messagebox.showinfo("GUI-PWD","File deleted.")
            return
        except FileNotFoundError:
            x = messagebox.showerror("GUI-PWD","Deletion failed.\nError code : 6510B")
    else:
        x = messagebox.showerror("GUI-PWD","Aborted.")
        return
def delete(filename):
        deleteconfirm = messagebox.askyesno("GUI-PWD","You are about to delete a file.This operation will delete the file IRREVOKABLY.Do you wish to proceed?",icon=messagebox.ERROR)
        if deleteconfirm:
            realdelete(True,filename)
        else:
            realdelete(False,None)
        return
def changepwd(fn,sn,newpwd):
    try:
        with open(fn,"r") as rpwd:
            r1 = rpwd.readlines()
            for b in range(len(r1)):
                if r1[b].strip("\n").split(" -> ")[0] == sn:
                            setnarme = r1[b].strip("\n").split(" -> ")[0] + " -> "
                            newsetpwd = setnarme + newpwd + "\n"
                            r1[b] = newsetpwd
        with open(fn,"w") as changepwd:
                    for a in range(len(r1)):
                        changepwd.writelines(r1[a]) 
        x = messagebox.showinfo("GUI-PWD","Your password has been changed.")
        return
    except FileNotFoundError:
        x = messagebox.showerror("GUI-PWD","Load failed. Make sure the file exists and try again.\nError code : 6510B")
        return
    except PermissionError:
        x = messagebox.showerror("GUI-PWD","Change failed. Make sure you have the appropriate permissions to change or read the file and try again.\nError code : 0210")
        return
    except BaseException:
        x = messagebox.showerror("GUI-PWD","Load failed. Check parameters and try again.\nError code : 770A")
        return
def realdelete(state,filename):
    import os
    if state == True:
        try:
            os.remove(filename)
            x = messagebox.showinfo("GUI-PWD","File deleted.")
            return
        except FileNotFoundError:
            x = messagebox.showerror("GUI-PWD","Deletion failed.\nError code : 6510B")
    else:
        x = messagebox.showerror("GUI-PWD","Aborted.")
        return
def delete(filename):
        deleteconfirm = messagebox.askyesno("GUI-PWD","You are about to delete a file.This operation will delete the file IRREVOKABLY.Do you wish to proceed?",icon=messagebox.ERROR)
        if deleteconfirm:
            realdelete(True,filename)
        else:
            realdelete(False,None)
        return
windows = Tk()
windows.title("GUI-PWD - Okmeque1 Real edition")
windows.geometry("1200x1200")
windows.resizable(width=False, height=False)
l0 = Label(windows,text="Default file is G:\Python\Demo\Demo.PC on ALL options with file names apart from deleting.")
displaypass = Text(windows,height=1,width=40)
l1 = Label(windows,text="Generate Passwords")
filabel = Label(windows,text="File name :")
filename = Entry(windows,width=40)
numberabel = Label(windows,text="Password length : ")
number = Entry(windows,width=40)
setlabel = Label(windows,text="Set name : ")
setname = Entry(windows,width=40)
save = Button(windows,text="Generate and save",command=lambda: generate(number.get(),filename.get(),setname.get()))
l2 = Label(windows,text="\n\nRetrieve password")
filabele = Label(windows,text="File name :")
filenamee = Entry(windows,width=40)
setlabele = Label(windows,text="Set name")
setnamee = Entry(windows,width=40)
continu = Button(windows,text="Retrieve",command=lambda: retrieve(filenamee.get(),setnamee.get()))
rp = Label(windows,text="Retrieved password : ")
l3 = Label(windows,text="\n\nFile name : ")
filedel = Entry(windows,width = 40)
confirm = Button(windows,text="Delete file",command = lambda: delete(filedel.get()))
l33 = Label(windows,text="\n\nChange a password")
l4 = Label(windows,text="File Name")
e4 = Entry(windows,width=40)
l5 = Label(windows,text="Set Name")
e5 = Entry(windows,width=40)
l6 = Label(windows,text="New Password")
e6 = Entry(windows,width=40)
b7 = Button(windows,text="Change password",command = lambda: changepwd(e4.get(),e5.get(),e6.get()))
exi = Button(windows,text="Quit",command=exit)
string = "This program is open source and made by Okmeque1.If you desire to copy this program,please keep a mention of Okmeque1 in the code as so the original code is not lost to time.This program can create a secure password of your length,8 to 19 characters is recommended for a secure password(DO NOT MAKE YOUR PASSWORD TOO LONG AS IT CAN OVERLOAD THE BUFFER ON THE COMPUTER AND CRASH IT.),can retrieve the password(this function is only useful if the file extention is foreign) and can erase the password file in case of hacking.For maximum compatability,run this program in Python 3+ and Windows 7 or higher(Please note that you can run it lower than those versions but the program might throw errors in lower version of windows(XP,Vista,etc) and some python functions might not exist in lower versions of python).\nThe program will run on macOS and Linux but the filepath format will vary as neither of those use drive letters (eg A:\directory\file.ext).The structure for those OS's will either be : \n1 : macOS : The file structure may be /path/path1/pwdfile.extention\n2 : Linux : The file structure is unclear as there are so many Linux distros out there but the structure may be /dev/sda/mountpoint1/folder/pwdfile.extention.\nPlease note that in both cases,DO NOT USE FOREIGN FILE EXTENTIONS(.dell,pc or any non-standard file format that can't be read by a text editor.) as the disk check utility might assume that the file is corrupt and delete it.\nPlease do NOT modify this program as the file may become unoriginal and might cause program breakage.This program took HOURS to complete and be at its current state."
l0.pack()
l1.pack()
filabel.pack()
filename.pack()
numberabel.pack()
number.pack()
setlabel.pack()
setname.pack()
save.pack()
l2.pack()
filabele.pack()
filenamee.pack()
setlabele.pack()
setnamee.pack()
continu.pack()
rp.pack()
displaypass.pack()
l3.pack()
filedel.pack()
confirm.pack()
exi.pack()
l33.pack()
l4.pack()
e4.pack()
l5.pack()
e5.pack()
l6.pack()
e6.pack()
b7.pack()
windows.mainloop()
