try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, simpledialog
    import os

    def new_file():
        text.delete("1.0", tk.END)

    def open_file():
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "r") as file:
                    content = file.read()
                text.delete("1.0", tk.END)
                text.insert("1.0", content)

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text.get("1.0", tk.END))
            messagebox.showinfo("Info", "File saved successfully!")
        
    def about():
        messagebox.showinfo("About", "Python Text Editor\nCreated by GamerSoft24.\n© GamerSoftware Corporation™. All rights reserved.")

    def get_user_input():
        result = simpledialog.askstring("Input", "Enter something:")
        if result:
            text.insert(tk.END, result)

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
    edit_menu.add_command(label="Input ", command=get_user_input)

    help_menu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about)

    text = tk.Text(root)
    text.pack(fill=tk.BOTH, expand=True)

    root.geometry("800x600")
    root.mainloop()

except FileExistsError:
    exit()
except FileNotFoundError:
    exit()
except OSError:
    x = messagebox.showerror("GUI Text Editor","A system error has occured. Exiting...\nError Code: 0271")
    exit()
except ValueError:
    x = messagebox.showerror("GUI Text Editor","You have entered a wrong value or this program has been tampered with. Exiting...\nError Code: 0211")
    exit()
except KeyboardInterrupt:
    print("LOG: User has chosen to exit. Exiting...")
    exit()
except EOFError:
    print("LOG: User has chosen to exit. Exiting...")
    exit()
except BaseException:
    x = messagebox.showerror("GUI Text Editor","Unhandled Exception at 0x0000024066EF3E20. Exiting...\nError Code: 770A")
    exit()
except IOError:
    x = messagebox.showerror("GUI Text Editor","I/O error. You have unplugged a device or a device on the host is malfunctioning. Exiting...\nError Code: 0272")
    exit()
except:
    x = messagebox.showerror("GUI Text Editor","Unhandled Exception at 0x0000024066EF3E20. Exiting...\nError Code: 770A")
    exit()
