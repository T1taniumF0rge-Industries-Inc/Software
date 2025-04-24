import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
def load(filename=None,access=None,pwd=None,encoder="utf-8"):
    text.delete("1.0",END)
    try:
        success = False
        with open(filename,"r",encoding=encoder) as returnname:
            b = returnname.readline()
            if b.strip("\n").split("=")[1] == access:
                 c = returnname.readline()
                 if c.strip("\n").split("=")[1] == pwd:
                      success = True
                      if success == True:
                        actuallyread = returnname.read()#do I need to explain?
                        text.insert(END,actuallyread)
                        return
                      else:
                          x = messagebox.showerror("Error","Load failed. Check your credentials and try again.\nError number : 3")
                          return
                 else:
                     x = messagebox.showerror("Error","Load failed. Please check your credentials and try again.\nError number : 2")
                     return
            else:
                x = messagebox.showerror("Error","Load failed. Check your credentials and try again.\nError number : 1")
                return
    except FileNotFoundError:
        filenotfound = messagebox.showerror("Error","Load failed.Make sure that the file exists and try again.\nError code : 6510B")
        return
    except PermissionError:
           permissionserr = messagebox.showerror("Error","Load failed.Make sure that you have the proper permissions and try again\nError code : 0210")
           return
    except LookupError:#stupid encoder madness
        lookuperr = messagebox.showerror("Error","Load failed. Please use a valid encoder(UTF-8 or ANSI) and try again.\nError code : 1E/18")
        return
    except UnicodeDecodeError:
        undecerr = messagebox.showerror("Error","Load failed. The specified encoder failed to parse the file. Please use the alternative encoder(if you were using UTF-8, try using ANSI) and try again.\nError code : 1E/10")
        return
    except BaseException:
        baseexec = messagebox.showerror("Error","Load failed.Check the file and permissions and try again.\nError code : 770A")
        return
def find(filename=None,tofind=None,toreplace=None,parameter="utf-8"):
    try:
        counter = 0
        counter1 = 0
        match = False
        passon = {}
        with open(filename,"r",encoding=parameter) as read1:
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
                        b = x - 2
                        adsf = messagebox.showinfo("G-Editor","Line where found : " + str(b+1) + "\nPosition in line : " + str(a+1))
                        if b not in passon:
                            passon[b] = [a]
                        else:
                            passon[b].append(a)
                    if counter1 == 0:
                        counter += 1
                counter = 0
            return tofind,toreplace,passon, len(tofind), len(toreplace),filename
    except FileNotFoundError:#wow error handling!
        filenotfound = messagebox.showerror("Error","Load failed .Make sure that the file exists and try again.\nError code : 6510B")
        return
    except PermissionError:
           permissionserr = messagebox.showerror("Error","Load failed .Make sure that you have the proper permissions and try again\nError code : 0210")
           return
    except BaseException:
        baseexec = messagebox.showerror("Error","Load failed .Check the file and permissions and try again.\nError code : 770A")
        return
def freplace(tofind=None,toreplace=None,indexes="utf-8",lentofind=None,filename=None):
        counter = 0
        counter1 = 0
        match = False
        passon = {}
        with open(filename,"r",encoding=indexes) as read1:
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
                        adsf = messagebox.showinfo("G-Editor","Line where found : " + str(b+1-2) + "\nPosition in line : " + str(a+1))
                        if b not in passon:
                            passon[b] = [a]
                        else:
                            passon[b].append(a)
                    if counter1 == 0:
                        counter += 1
                counter = 0
            with open(filename,"r",encoding=indexes) as replaceit:
                lines = replaceit.readlines()
                for x in passon:
                    for y in passon[x]:
                        lines[x] = lines[x][:y] + toreplace + lines[x][y + len(tofind):]
            with open(filename,"w") as actuallyreplace:
                for x in range(len(lines)):
                    actuallyreplace.writelines(lines[x])
            x = messagebox.showinfo("Note","The replace operation is complete. The file must be reloaded for the changes to take effect.")
            return 
def save(text,filename,access,pwd):
    try:
        with open(filename,"r") as verifycredentials:
            b = verifycredentials.readline()
            if b.strip("\n").split("=")[1] == access:
                 c = verifycredentials.readline()
                 if c.strip("\n").split("=")[1] == pwd:                
                    with open(filename,"w") as writing:
                        writing.write(b)
                        writing.write(c)
                        writing.write(text)
                        success = messagebox.showinfo("G-Editor - Password Edition","Save complete!")
                        return
                 else:
                     x = messagebox.showerror("Error","Save failed. Check your credentials and try again.\nError number : 2")
            else:
                x = messagebox.showerror("Error","Save failed. Check your credentials and try again.\nError number : 1")
    except FileExistsError:
        fileexist = messagebox.showerror("Error","Save failed.Choose a different file name and try again\nError code : 6510A")
        return
    except PermissionError:
           permissionserr = messagebox.showerror("Error","Save failed.Make sure that you have the proper permissions and try again\nError code : 0210")
           return    
    except BaseException:
         baseexec = messagebox.showerror("Error","Save failed.Check file names,permissions and disk space and try again.\nError code : 770A")
         return
def about():
    abou = messagebox.showinfo("G-Editor - Password Edition - About","About this program\nWritten by Okmeque1 starting Wednesday 14/02/2024 finishing Sat 09/30/2023 15:41\nThis program is run by tkinter and is open-source.You may copy it onto any form of media whether it be a : \n-USB,CD or DVD\n-Cloud storage(NAS or Google drive)\n-Or on Github...\nso long you mention Okmeque1 in the code.\n\nThe save button can save or create a file,so long the file isn't obstructing with any present files.When loading,make sure the file exists.")
    return
def makenewfilepwd(fn,access,pwd):
    try:
        with open(fn,"w") as mkfilepwd:
            mkfilepwd.write("access=" + access + "\npassword=" + pwd + "\n")
            x = messagebox.showinfo("G-Editor - Password Edition","File created.")
            return
    except FileExistsError:
        fileexist = messagebox.showerror("Error","Creation failed.Choose a different file name and try again\nError code : 6510A")
        return
    except PermissionError:
           permissionserr = messagebox.showerror("Error","Creation failed.Make sure that you have the proper permissions and try again\nError code : 0210")
           return    
    except BaseException:
         baseexec = messagebox.showerror("Error","Creation failed.Check file names,permissions and disk space and try again.\nError code : 770A")
         return
def checkchangecredentials(fn,axess,pwd,encoder):
    try:
        success = False
        with open(fn,"r") as readpwd:
            read1 = readpwd.readline()
            if read1.strip("\n").split("=")[1] == axess:
                read2 = readpwd.readline()
                if read2.strip("\n").split("=")[1] == pwd:
                    success = True
                    if success == True:
                        changecredentials(success,fn,encoder)
                    else:
                        x = messagebox.showerror("G-Editor - Password Edition","Credential check failed. Check your credentials and try again.\nError number : 3")
                        return
                else:
                    x = messagebox.showerror("G-Editor - Password Edition","Credential check failed. Check your credentials and try again.\nError number : 2")
                    return
            else:
                x = messagebox.showerror("G-Editor - Password Edition","Credential check failed. Check your credentials and try again.\nError number : 1")
                return
    except FileNotFoundError:
        filenotfound = messagebox.showerror("Error","Load failed.Make sure that the file exists and try again.\nError code : 6510B")
        return
    except PermissionError:
           permissionserr = messagebox.showerror("Error","Load failed.Make sure that you have the proper permissions and try again\nError code : 0210")
           return
def changecredentials(successstate,filename,encoder):
    if successstate == True:
        with open(filename,"r",encoding=encoder) as readl:
            readl1 = readl.readlines()
            readl1[0] = 'access=' + simpledialog.askstring("New access","Please enter a new access for your file.") + '\n'
            readl1[1] = 'password=' + simpledialog.askstring("New password","Please enter a new password for your file.") + '\n'
            print(readl1)
            readl.close()
        with open(filename,"w") as addline:
            for x in range(len(readl1)):
                addline.writelines(readl1[x])
        x = messagebox.showinfo("G-Editor - Password Edition","Your credentials have been changed. To make changes to the file, you must reload it by entering the new credentials and the same file name then press LOAD.")
        load(filename,encoder)


windows = Tk()
windows.geometry("1024x860")
windows.title("G-Editor - Password Edition")
windows.resizable(width=False, height=False)
loop = True
text = Text(windows,height=25,width=100)
file_name = None
l1 = Label(windows,text="File name : ")
ldl = Entry(windows,width=40)
l2 = Label(windows,text="Access : ")
l2l = Entry(windows,width=40)
l3 = Label(windows,text="Password : ")
l3l = Entry(windows,width=40)
l4 = Label(windows,text="Find : ")
l4l = Entry(windows,width=40)
l5 = Label(windows,text="Replace with : ")
l5l = Entry(windows,width=40)
l6 = Label(windows,text="Encoder(utf-8 or ansi)")
l6l = Entry(windows,width=40)
ld = Button(windows,text="Load",command = lambda: load(ldl.get(),l2l.get(),l3l.get(),l6l.get()),width=40,activebackground="gray")
sv = Button(windows,text="Save",command = lambda: save(text.get("1.0",END),ldl.get(),l2l.get(),l3l.get()),width=40,activebackground="gray")
svpwd = Button(windows,text="Make new file",command = lambda: makenewfilepwd(ldl.get(),l2l.get(),l3l.get()),width=40)
chpwd = Button(windows,text="Change access & password credentials",command = lambda: checkchangecredentials(ldl.get(),l2l.get(),l3l.get(),l6l.get()),width=40)
ab = Button(windows,text="About",command = about,width = 40,activebackground="gray")
finds = Button(windows,text="Find text",command = lambda: find(ldl.get(),l4l.get(),l5l.get(),l6l.get()),width=40)
replaceit = Button(windows,text="Find & Replace",command=lambda: freplace(l4l.get(),l5l.get(),l6l.get(),None,ldl.get()),width=40)
text.pack()
l1.pack()
ldl.pack()
l2.pack()
l2l.pack()
l3.pack()
l3l.pack()
l4.pack()
l4l.pack()
l5.pack()
l5l.pack()
l6.pack()
l6l.pack()
ld.pack()
sv.pack()
ab.pack()
svpwd.pack()
chpwd.pack()
finds.pack()
replaceit.pack()
windows.mainloop()
