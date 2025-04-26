try: 
    import tkinter as tk
    from tkinter import *
    from tkinter import messagebox
    from tkinter import simpledialog
    def clearscreen():
        for widget in windows.winfo_children():
            widget.destroy()
        return
    def wg(cr,nextquestion,points,reason):
        x = messagebox.showerror("Wrong Answer!","You have answered incorrectly. The correct answer was number " + str(cr) + ". This is because " + reason)
        if nextquestion == 2:
            question_2(points + 0)
        elif nextquestion == 3:
            question_3(points + 0)
        else:
            finish(points)
    def cr(nextquestion,points):
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
        text.insert(END,"Question 1 : How do you import a module onto your Python program?")
        text.config(state="disabled")
        b1 = Button(windows,text="1 : pip install module_name",command=lambda: wg(3,2,points,"'pip install' is used to install modules onto your computer, not import them."))
        b2 = Button(windows,text="3 : pip import module_name",command=lambda: wg(3,2,points,"the pip program is used to install modules onto your computer. However import module_name is a valid way to import modules."))
        b4 = Button(windows,text="3 : install module_name",command=lambda: wg(3,2,points,"this is not a valid expression. You have to IMPORT the modules. To install modules, you have to use pip."))
        b3 = Button(windows,text="4 : import module_name",command=lambda: cr(2,points))
        text.pack()
        b1.pack()
        b2.pack()
        b4.pack()
        b3.pack()
    def question_2(points):
        clearscreen()
        text = Text(windows,height=2.5,width=100)
        text.insert(END,"Question 2 : How do you make a function return a value?")
        text.config(state="disabled")
        b4 = Button(windows,text="1 : return variable_name",command=lambda: cr(3,points))
        b1 = Button(windows,text="2 : exit(variable_name)",command=lambda: wg(1,3,points,"this would make the program close itself with the closing message being whatever value was stored in variable_name."))
        b2 = Button(windows,text="3 : variable_name = func_name()",command=lambda: wg(1,3,points,"that would assign variable_name to the function itself."))
        b3 = Button(windows,text="4 : func_name().return(variable_name)",command=lambda: wg(1,3,points,"return is an expression, not a function."))
        text.pack()
        b4.pack()
        b1.pack()
        b2.pack()
        b3.pack()
    def question_3(points):
        clearscreen()
        text = Text(windows,height=2.5,width=100)
        text.insert(END,"Question 3 : What is the correct way to do a power (ex 2^2=4) in Python?")
        text.config(state="disabled")
        b1 = Button(windows,text="1 : a ^ b",command=lambda: wg(2,NONE,points,"this is an XOR function, which is a binary format that is rather complicated, and is not intuitively the power operator as you might expect. The correct way to power a number is using the ** expression."))
        b2 = Button(windows,text="2 : a ** b",command=lambda: cr(NONE,points))
        b3 = Button(windows,text="3 : a * b",command=lambda: wg(2,NONE,points,"that would multiply a by b (ab)"))
        b4 = Button(windows,text="4 : a ^^ b",command=lambda: wg(2,NONE,points,"this expression is invalid and does not exist.."))
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
