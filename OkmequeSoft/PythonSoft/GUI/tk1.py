import tkinter as tk
import time

windows = tk.Tk()
windows.title("Okmeque1 Notepad (OkPad)")
label = tk.Label(windows,text= "test1").pack()
button1 = tk.Button(windows,text= "test1",bg= "green").pack()
windows.geometry("1024x768")
windows.mainloop()
