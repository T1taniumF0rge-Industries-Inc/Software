try:
    def stop():
            global buttonsoricons
            global icons
            global choices
            buttonsoricons = ["showerror","showwarning","showinfo","askokcancel","askquestion","askretrycancel","askyesno","askyesnocancel"]#possible buttons/icons, pretty obvious
            icons = ["messagebox.ERROR","messagebox.INFO","messagebox.WARNING","messagebox.QUESTION"]#possible icons, pretty obvious
            # 1st part of choices = base, 2nd part is the buttonsoricons list that needs to be, 3rd is the parenthesis to start, 4th is msgbox title, 5th is comma, 6th is message string and the (non-existent) 7th part is for the icon 
            choices = ["messagebox.","","(","",",",""]#this was part of trying to eval() the thing but got way to complicated and I gave up...
            return
    def u1():#U functions. They change the buttons and/or icon. From options 3-7 you need to choose an icon
        choices[1] = buttonsoricons[0]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u2():
        choices[1] = buttonsoricons[1]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u3():
        choices[1] = buttonsoricons[2]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u4():
        choices[1] = buttonsoricons[3]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u5():
        choices[1] = buttonsoricons[4]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u6():
        choices[1] = buttonsoricons[5]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u7():
        choices[1] = buttonsoricons[6]
        x = messagebox.showinfo("Info","Complete.")
        return
    def u8():
        choices[1] = buttonsoricons[7]
        x = messagebox.showinfo("Info","Complete.")
        return
    def i3():# I functions, not because it i9 won't run on an i3, but it changes the icons needed for buttonsoricons 3-7. Note the try/except to do this,which you shouldn't
        try:
            choices[6] = icons[0]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            choices.append(icons[0])
            x = messagebox.showinfo("Info","Complete.")
            return
    def i5():
        try:
            choices[6] = icons[1]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            choices.append(icons[1])
            x = messagebox.showinfo("Info","Complete.")
            return
    def i7():
        try:
            choices[6] = icons[2]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            choices.append(icons[2])
            x = messagebox.showinfo("Info","Complete.")
            return
    def i9():
        try:
            choices[6] = icons[3]
            x = messagebox.showinfo("Info","Complete.")
            return
        except IndexError:
            choices.append(icons[3])
            x = messagebox.showinfo("Info","Complete.")
            return
    def gen(titl,mst) -> None:#The REAL stuff, this is where generation happens and it's clunky due to the way I made it just work by jamming code...
            windows.withdraw()#remove da window
            if buttonsoricons[0] == choices[1]:
                z = messagebox.showerror(titl,mst)
                windows.deiconify()#deiconify() puts back the window after putting the button
                return
            elif buttonsoricons[1] == choices[1]:
                z = messagebox.showwarning(titl,mst)
                windows.deiconify()
                return
            elif buttonsoricons[2] == choices[1]:
                z = messagebox.showinfo(titl,mst)
                windows.deiconify()
                return
            elif buttonsoricons[3] == choices[1]:
                if icons[0] in choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.ERROR)
                    windows.deiconify()
                    return
                elif icons[1] in choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.INFO)
                    windows.deiconify()
                    return
                elif icons[2] in choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.WARNING)
                    windows.deiconify()
                    return
                elif icons[3] in choices:
                    z = messagebox.askokcancel(titl,mst,icon=messagebox.QUESTION)
                    windows.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                    windows.deiconify()
                    return  
            elif buttonsoricons[4] == choices[1]:
                if icons[0] in choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.ERROR)
                    windows.deiconify()
                    return
                elif icons[1] in choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.INFO)
                    windows.deiconify()
                    return
                elif icons[2] in choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.WARNING)
                    windows.deiconify()
                    return
                elif icons[3] in choices:
                    z = messagebox.askquestion(titl,mst,icon=messagebox.QUESTION)
                    windows.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                    windows.deiconify()
                    return  
            elif buttonsoricons[5] == choices[1]:
                if icons[0] in choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.ERROR)
                    windows.deiconify()
                    return
                elif icons[1] in choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.INFO)
                    windows.deiconify()
                    return
                elif icons[2] in choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.WARNING)
                    windows.deiconify()
                    return
                elif icons[3] in choices:
                    z = messagebox.askretrycancel(titl,mst,icon=messagebox.QUESTION)
                    windows.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                    windows.deiconify()
                    return  
            elif buttonsoricons[6] == choices[1]:
                if icons[0] in choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.ERROR)
                    windows.deiconify()
                    return
                elif icons[1] in choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.INFO)
                    windows.deiconify()
                    return
                elif icons[2] in choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.WARNING)
                    windows.deiconify()
                    return
                elif icons[3] in choices:
                    z = messagebox.askyesno(titl,mst,icon=messagebox.QUESTION)
                    windows.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                    windows.deiconify()
                    return  
            elif buttonsoricons[7] == choices[1]:
                if icons[0] in choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.ERROR)
                    windows.deiconify()
                    return
                elif icons[1] in choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.INFO)
                    windows.deiconify()
                    return
                elif icons[2] in choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.WARNING)
                    windows.deiconify()
                    return
                elif icons[3] in choices:
                    z = messagebox.askyesnocancel(titl,mst,icon=messagebox.QUESTION)
                    windows.deiconify()
                    return
                else:
                    z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                    windows.deiconify()
                    return  
            else:
                z = messagebox.showerror("Error","Required parameter missing. Please use the How to use button for more information.")
                windows.deiconify()
                return
    def about_htu():
        x = messagebox.showinfo("Info/HTU","This is the Okmeque1 Error message creator and can generate as many errors as tkinter wants.\n\nTo use this program, you can choose from the 1st 8 buttons BUT from buttons 4-8 you NEED to select an icon. Otherwise generation might fail aswell as your whole computer.")
        return
    import tkinter as tk
    from tkinter import *
    from tkinter import messagebox
    sample = messagebox
    buttonsoricons = ["showerror","showwarning","showinfo","askokcancel","askquestion","askretrycancel","askyesno","askyesnocancel"]#possible buttons/icons, pretty obvious
    icons = ["messagebox.ERROR","messagebox.INFO","messagebox.WARNING","messagebox.QUESTION"]#possible icons, pretty obvious
    # 1st part of choices = base, 2nd part is the buttonsoricons list that needs to be, 3rd is the parenthesis to start, 4th is msgbox title, 5th is comma, 6th is message string and the (non-existent) 7th part is for the icon 
    choices = ["messagebox.","","(","",",",""]#this was part of trying to eval() the thing but got way to complicated and I gave up...
    windows = Tk()#starting buttons and main windows...
    windows.geometry("800x600")
    windows.title("Error message generator")
    l1 = Label(windows,text="Title string : ")
    TString = Entry(windows,width=40)
    l2 = Label(windows,text="Error message string : ")
    MSGString = Entry(windows,width=40)
    ErrorOk = Button(windows,text="MSGBOX Show Error",command=u1,width=40)
    WarningOk = Button(windows,text="MSGBOX Show Warning",command=u2,width=40)
    InfoOk = Button(windows,text="MSGBOX Show Info",command=u3,width=40)
    okcan = Button(windows,text="MSGBOX Buttons OK and CANCEL",command=u4,width=40)
    ques = Button(windows,text="MSGBOX QUESTION",command=u5,width=40)
    racecar = Button(windows,text="MSGBOX Buttons RETRY and CANCEL",command=u6,width=40)#some of these names you have to understand by reading the string
    yesrefuse = Button(windows,text="MSGBOX Buttons YES and NO",command=u7,width=40)
    yescancelno = Button(windows,text="MSGBOX Buttons YES, NO and CANCEL",command=u8,width=40)
    useerroricon = Button(windows,text="Use ERROR icon",command=i3,width=40)
    useinfoicon = Button(windows,text="Use INFO icon",command=i5,width=40)
    usewarningicon = Button(windows,text="Use WARNING icon",command=i7,width=40)
    usequestionicon = Button(windows,text="Use QUESTION icon",command=i9,width=40)
    generate = Button(windows,text="Generate!",command=lambda: gen(TString.get(),MSGString.get()),width=40)
    log = Button(windows,text="How to use/About",command=about_htu,width=40)
    stopbutton = Button(windows,text="STOP",command=stop,width=40)#STOP button is the same one used in this video https://www.youtube.com/watch?v=1Fnso7KcgAw&t=75s
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
    windows.mainloop()#looping the window
except BaseException:#error handling wow!
    x = messagebox.showerror("Error","This program has encountered an error and needs to close.\nError code : 770A")
    exit()
