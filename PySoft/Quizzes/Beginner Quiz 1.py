try: 
    import tkinter as tk
    from tkinter import *
    from tkinter import messagebox
    from tkinter import simpledialog
    def clearscreen():
        for widget in windows.winfo_children():
            widget.destroy()
        return
    def wrong(correct,nextquestion,points,reason):
        x = messagebox.showerror("Wrong Answer!","You have answered incosrrectly. The correct answer was number " + str(correct) + ". This is because " + reason)
        if nextquestion == 2:
            question_2(points + 0)
        elif nextquestion == 3:
            question_3(points + 0)
        else:
            finish(points)
    def correct(nextquestion,points):
        x = messagebox.showinfo("Correct Answer!","This is the correct answer.")
        if nextquestion == 2:
            question_2(points + 1)
        elif nextquestion == 3:
            question_3(points + 1)
        else:
            finish(points + 1)
    def finish(points):
        if points <= 1:
            x = messagebox.showerror("Oh no!","You have only gotten " + str(points) + " points. This means you do not know the basics of python. Please seek assistance.")
        elif points == 2:
            x = messagebox.showwarning("Uh Oh","You have gotten 2 points, so you may need to revise your skills. ")
        elif points >= 3:
            x = messagebox.showinfo("Congratulations!","You have passed the quiz. Show this to beginner coders!")
        exit()
    def question_1(points):
        windows.geometry("640x480")
        clearscreen()
        text = Text(windows,height=2.5,width=100)
        text.insert(END,"Question 1 : How do you call a function? Press the correct button!")
        text.config(state="disabled")
        b1 = Button(windows,text="1 : call func_name()",command=lambda: wrong(3,2,points,"'call' is not a thing in any Python version."))
        b2 = Button(windows,text="2 : import func_name()",command=lambda: wrong(3,2,points,"'import' is used for importing entire modules, not a function"))
        b3 = Button(windows,text="3 : func_name()",command=lambda: correct(2,points))
        b4 = Button(windows,text="4 : func_name",command=lambda: wrong(3,2,points,"calling the function without parentheses will just return the memory address like this : '<function func_name at 0x000002C099933E20>'"))
        text.pack()
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()
    def question_2(points):
        clearscreen()
        text = Text(windows,height=2.5,width=100)
        text.insert(END,"Question 2 : How do you make the user input something? Press the correct button!")
        text.config(state="disabled")
        b1 = Button(windows,text="1 : user.input('Prompt>')",command=lambda: wrong(4,3,points,"'user.' does not exist in any version of Python. The input() function within does exist however."))
        b2 = Button(windows,text="2 : input 'prompt>'",command=lambda: wrong(4,3,points,"it is not the correct syntax."))
        b3 = Button(windows,text="3 : make input() with values[prompt] as 'prompt>'",command=lambda: wrong(4,3,points,"because only the 'input()' function within exists. The rest does not exist."))
        b4 = Button(windows,text="4 : input('prompt')",command=lambda: correct(3,points))
        text.pack()
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()
    def question_3(points):
        clearscreen()
        text = Text(windows,height=2.5,width=100)
        text.insert(END,"Question 3 : How do you print something to the screen? Press the correct button!")
        text.config(state="disabled")
        b1 = Button(windows,text="1 : print 'some text'",command=lambda: wrong(2,NONE,points,"this syntax is not valid in Python 3.*, and only functions in Python 2"))
        b2 = Button(windows,text="2 : print('some text')",command=lambda: correct(NONE,points))
        b3 = Button(windows,text="3 : screen.print('some text')",command=lambda: wrong(2,NONE,points,"'screen.' does not exist. The 'print()' function within does exist however."))
        b4 = Button(windows,text="4 : terminal.createtext('some text')",command=lambda: wrong(2,NONE,points,"this command and its functions do not exist."))
        text.pack()
        b1.pack()
        b2.pack()
        b3.pack()
        b4.pack()
    windows = Tk()
    windows.geometry("640x120")
    windows.title("Python Quiz - Beginner - © Okmeque1 Computers.")
    text = Text(windows,height=2.5,width=100)
    text.insert(END,"Welcome to the GamerSoftware-Okmeque1 Python Quiz. Test your skillz now for the ultimate coding adventure!")
    text.config(state="disabled")
    sbutton = Button(windows,text="Start the Quiz!",activebackground="green",command=lambda: question_1(0))
    text.pack()
    sbutton.pack()
    windows.mainloop()
except SystemExit:
    exit()
except BaseException:
    x = messagebox.showerror("Error","Program has been tampered with. Exiting...")
    exit()
