import tkinter as tk
from tkinter import *
from tkinter import messagebox
def load(filename=None,encoder="utf-8"):
    text.delete("1.0",END)#not very complicated, readds the file and pastes it into text window
    try:
        with open(filename,"r",encoding=encoder) as returnname:
            a = returnname.read()
            text.insert(END,a)
            return
    except FileNotFoundError:#wow error handling!
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
def save(text,filename):
    try:
        with open(filename,"w") as writing:#more simple, you should be able to read it.
            writing.write(text)
            success = messagebox.showinfo("G-Editor","Save complete!")
            return
    except FileExistsError:#wow error handling!
        fileexist = messagebox.showerror("Error","Save failed.Choose a different file name and try again\nError code : 6510A")
        return
    except PermissionError:
           permissionserr = messagebox.showerror("Error","Save failed.Make sure that you have the proper permissions and try again\nError code : 0210")
           return    
    except BaseException:
         baseexec = messagebox.showerror("Error","Save failed.Check file names,permissions and disk space and try again.\nError code : 770A")
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
                        b = x
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
                        adsf = messagebox.showinfo("G-Editor","Line where found : " + str(b+1) + "\nPosition in line : " + str(a+1))
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
            load(filename,indexes)
def about():
    abou = messagebox.showinfo("G-Editor - About","About this program\nWritten by Okmeque1 starting Thu 28/09/2023 finishing Sat 09/30/2023 15:41\nThis program is run by tkinter and is open-source.You may copy it onto any form of media whether it be a : \n-USB,CD or DVD\n-Cloud storage(NAS or Google drive)\n-Or on Github...\nso long you mention Okmeque1 in the code.\n\nThe save button can save or create a file,so long the file isn't obstructing with any present files.When loading,make sure the file exists.")
windows = Tk()
windows.geometry("1024x768")
windows.title("G-Editor")
windows.resizable(width=False, height=False)
loop = True
text = Text(windows,height=29.71,width=100)
file_name = None
l1 = Label(windows,text="File name : ")
ldl = Entry(windows,width=40)
l2 = Label(windows,text="Find : ")
l2l = Entry(windows,width=40)
l3 = Label(windows,text="Replace with : ")
l3l = Entry(windows,width=40)
l4 = Label(windows,text="Encoder(utf-8 or ansi)")
l4l = Entry(windows,width=40)
ld = Button(windows,text="Load",command = lambda: load(ldl.get(),l4l.get()),width=40,activebackground="gray")
sv = Button(windows,text="Save",command = lambda: save(text.get("1.0",END),ldl.get()),width=40,activebackground="gray")
ab = Button(windows,text="About",command = about,width = 40,activebackground="gray")
finds = Button(windows,text="Find text",command = lambda: find(ldl.get(),l2l.get(),l3l.get(),l4l.get()),width=40)
replaceit = Button(windows,text="Find & Replace",command=lambda: freplace(l2l.get(),l3l.get(),l4l.get(),None,ldl.get()),width=40)
text.pack()
l1.pack()
ldl.pack()
l2.pack()
l2l.pack()
l3.pack()
l3l.pack()
l4.pack()
l4l.pack()
ld.pack()
sv.pack()
ab.pack()
finds.pack()
replaceit.pack()
windows.mainloop()
