try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, simpledialog

    def new_file():
        text.delete("1.0", tk.END)

    def open_file():
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path: # Check if user actually put a file
                with open(file_path, "r") as file:
                    content = file.read()
                text.delete("1.0", tk.END)
                text.insert("1.0", content)

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path: # Same thing checking
            with open(file_path, "w") as file:
                file.write(text.get("1.0", tk.END))
            messagebox.showinfo("Info", "File saved successfully!")
        
    def about():
        messagebox.showinfo("About", "Python Text Editor\nCreated by GamerSoft24.\n© GamerSoftware Corporation™. All rights reserved.\n© Find/Replace feature by Okmeque1 Software")

    def find_replace(parameter=False):
        tofind = simpledialog.askstring("Find","Enter value to find in file: ")
        toreplace = ''
        if parameter is True:
            toreplace = simpledialog.askstring("Replace","Enter replacement value: ")
        window = text.get("1.0", tk.END) # Get Text
        splits = window.split('\n') # Split using \n to split every line
        success = False # Used if no matches are found
        for x in range(len(splits)):
            pointer = 0 # Set pointer to 0 for start of string
            temp = 0 # Temporary value to prevent infinite loop in while True:
            while True:
                position = splits[x][pointer:].find(tofind) # Find value in one line starting from the pointer position
                if position == -1: # Can't find scenario
                    break
                if temp > position: # Prevents infinite loop
                    break
                pointer = position + 1 # Increase pointer by 1 to skip last match
                temp = position # Keep a record of position
                messagebox.showinfo("Found matches",f"Found at line {x}, position {position}. ")
                success = True
        if success is not True:
            messagebox.showinfo("No matches","No matches found.")
        if parameter is True:
            window = window.replace(tofind, toreplace) # Very simple replace no big deal
            text.delete("1.0",tk.END)
            text.insert(tk.END, window)
    root = tk.Tk()
    root.title("Python Text Editor")

    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    edit_menu = tk.Menu(menu)
    menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Find ", command=find_replace)
    edit_menu.add_command(label="Find/Replace", command=lambda: find_replace(parameter=True))
    help_menu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about)

    text = tk.Text(root)
    text.pack(fill=tk.BOTH, expand=True)

    root.geometry("800x600")
    root.resizable(width=True, height=True)
    root.mainloop()
except FileExistsError as e: # Error codes can be found at https://github.com/GamerSoft24/Software/blob/Main/PySoft/Errors%20chart.md
    x = messagebox.showerror("GUI Text Editor",f"The file that you specified is conflicting with another file. Delete or rename the conflicting file, or choose an alternative file name.\nError Code: 6510A\nDetails: {e}")
except FileNotFoundError as e:
    x = messagebox.showerror("GUI Text Editor",f"The file that you specified is not valid. Make sure the file exists and that you typed it correctly.\nError Code: 6510B\nDetails: {e}")
except PermissionError as e:
    x = messagebox.showerror("GUI Text Editor",f"Access violation in file. Make sure you can use the file, then try again.\nError Code: 0211\nDetails: {e}")

except IOError as e:
    x = messagebox.showerror("GUI Text Editor",f"I/O error. You have unplugged a device or a device on the host is malfunctioning. Program will now exit\nError Code: 0272\nDetails: {e}")
    exit()
except OSError as e:
    x = messagebox.showerror("GUI Text Editor",f"A system error has occured. Check for disk corruption, faulty/loosely connected hardware. Program will now exit\nError Code: 0271\nDetails: {e}")
    exit()
except ValueError as e:
    x = messagebox.showerror("GUI Text Editor",f"You have entered a wrong value or this program has been tampered with. When asked for a value, enter the CORRECT values that are demanded.\nError Code: 0211\nDetails: {e}")
except KeyboardInterrupt:
    print("LOG: User has chosen to exit. Exiting... (0270)")
    exit()
except EOFError:
    print("LOG: User has chosen to exit. Exiting... (0250)")
    exit()
except SystemExit:
    exit()
except Exception as e:
    x = messagebox.showerror("GUI Text Editor",f"Unhandled Exception at 0x0000024066EF3E20 has occured in this program. Review the GitHub GamerSoft24/Software PySoft error chart and the Python manual for more info.\nError Code: 770A\nDetails: {e}")

