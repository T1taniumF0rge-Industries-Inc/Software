try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, simpledialog
    global encoder
    def new_file():
        text.delete("1.0", tk.END)

    def open_file():
            try:
                global encoder
                file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
                if file_path: # Check if user actually put a file
                    with open(file_path, "r",encoding=encoder) as file:
                        content = file.read()
                    text.delete("1.0", tk.END)
                    text.insert("1.0", content)
            except LookupError as e:
                x = messagebox.showerror("GUI Text Editor",f"Could not load the specified encoder. Make sure that it is valid and that you typed it correctly. Note that if you were doing a save operation, the last changes were not saved to the file but are still in the editor, and you will have to re-save the file.\nError code: 1E/18\nDetails: {e}")
            except UnicodeDecodeError as e:
                x = messagebox.showerror("GUI Text Editor",f"Encoder failed to parse the specified file. Try using a different encoder (if you were using UTF-8, try ANSI) and try again. Note that if you were doing a save operation, the last changes were not saved to the file but are still in the editor, and you will have to re-save the file.\nError Code: 1E/10\nDetails: {e}")
            except FileExistsError as e: # Error codes can be found at https://github.com/GamerSoft24/Software/blob/Main/PySoft/Errors%20chart.md
                x = messagebox.showerror("GUI Text Editor",f"The file that you specified is conflicting with another file. Delete or rename the conflicting file, or choose an alternative file name. Note that if you were doing a save operation, the last changes were not saved to the file but are still in the editor, and you will have to re-save the file.\nError Code: 6510A\nDetails: {e}")
            except FileNotFoundError as e:
                x = messagebox.showerror("GUI Text Editor",f"The file that you specified is not valid. Make sure the file exists and that you typed it correctly.\nError Code: 6510B\nDetails: {e}")
            except PermissionError as e:
                x = messagebox.showerror("GUI Text Editor",f"Access violation in file. Make sure you can use the file, then try again.\nError Code: 6510C\nDetails: {e}")
            except Exception as e:
                x = messagebox.showerror("GUI Text Editor",f"Unhandled Exception 0x0000024066EF3E20 has occured in this program. Review the GitHub GamerSoft24/Software PySoft error chart and the Python manual for more info.\nError Code: 770A\nDetails: {e}")
    def save_file():
        try:
            global encoder
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path: # Same thing checking
                with open(file_path, "w",encoding=encoder) as file:
                    file.write(text.get("1.0", tk.END))
                messagebox.showinfo("Info", "File saved successfully!")
        except LookupError as e:
                x = messagebox.showerror("GUI Text Editor",f"Could not load the specified encoder. Make sure that it is valid and that you typed it correctly. Note that if you were doing a save operation, the last changes were not saved to the file but are still in the editor, and you will have to re-save the file.\nError code: 1E/18\nDetails: {e}")
        except UnicodeDecodeError as e:
            x = messagebox.showerror("GUI Text Editor",f"Encoder failed to parse the specified file. Try using a different encoder (if you were using UTF-8, try ANSI) and try again. Note that if you were doing a save operation, the last changes were not saved to the file but are still in the editor, and you will have to re-save the file.\nError Code: 1E/10\nDetails: {e}")
        except FileExistsError as e: # Error codes can be found at https://github.com/GamerSoft24/Software/blob/Main/PySoft/Errors%20chart.md
            x = messagebox.showerror("GUI Text Editor",f"The file that you specified is conflicting with another file. Delete or rename the conflicting file, or choose an alternative file name. Note that if you were doing a save operation, the last changes were not saved to the file but are still in the editor, and you will have to re-save the file.\nError Code: 6510A\nDetails: {e}")
        except FileNotFoundError as e:
            x = messagebox.showerror("GUI Text Editor",f"The file that you specified is not valid. Make sure the file exists and that you typed it correctly.\nError Code: 6510B\nDetails: {e}")
        except PermissionError as e:
            x = messagebox.showerror("GUI Text Editor",f"Access violation in file. Make sure you can use the file, then try again.\nError Code: 6510C\nDetails: {e}")
        except Exception as e:
            x = messagebox.showerror("GUI Text Editor",f"Unhandled Exception 0x0000024066EF3E20 has occured in this program. Review the GitHub GamerSoft24/Software PySoft error chart and the Python manual for more info.\nError Code: 770A\nDetails: {e}")

    def about():
        messagebox.showinfo("About", "Python Text Editor\nCreated by GamerSoft24.\n© GamerSoftware Corporation™. All rights reserved.\n© Find/Replace feature by Okmeque1 Software")
    def configure_encoder():
        global encoder
        encoder = simpledialog.askstring("Encoder configuration","Choose an encoder:\n[1] UTF-8 (most common in modern systems)\n[2] ANSI (most common in Windows Pre-Vista)\n[3] Custom")
        if encoder == "1":
            encoder = 'utf-8'
        elif encoder == "2":
            encoder = 'ansi'
        else:
            encoder = simpledialog.askstring("Custom Encoder configuration","Enter name of encoder: ")
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
    encoder = 'utf-8'
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
    edit_menu.add_command(label="Configure encoder", command=configure_encoder)
    help_menu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about)

    text = tk.Text(root)
    text.pack(fill=tk.BOTH, expand=True)

    root.geometry("800x600")
    root.resizable(width=True, height=True)
    root.mainloop()
except Exception as e:
    x = messagebox.showerror("GUI Text Editor",f"Unhandled Exception 0x0000024066EF3E20 has occured in this program. Review the GitHub GamerSoft24/Software PySoft error chart and the Python manual for more info.\nError Code: 770A\nDetails: {e}")


