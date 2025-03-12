#StealthCrew - PhantomToolX (SC_PtX) v1.3.2
#Author: Midnight_G0ldX
#About: This is a tool that can be used for Among Us from Steam and Epic Games for Among Us v2024.11.24 and higher. 
#Description: This tool can reveal the roles of other players (in standard or modded games) and the radar function to know where people are is getting implemented.
#IMPORTANT! Make sure that the "Polus.png" image is in the same directory as this file! (Even though its useless for now...)

import tkinter as tk
from tkinter import ttk
import threading
import keyboard
import pymem
import os
import sys
import subprocess
from PIL import Image, ImageTk
import time
 
class MemoryReader:
    def __init__(self, root, process_name):
        self.root = root
        self.process_name = process_name
        self.base_adderess = None
        self.auto_update_thread = None
        self.auto_update_flag = threading.Event()
        self.auto_update_interval = tk.DoubleVar(value=1.0)  # Default interval set to 1 second
        self.toggle_state = tk.BooleanVar(value=False)
        self.update_names_flag = False
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
 
        # self.steam_offset = 0x02322330
        # self.epic_offset = 0x022A5A84
        self.steam_offset = 0x0232F9D4
        self.epic_offset = 0x022A7A98
 
        # Add platform selection
        self.platform_var = tk.StringVar(value="steam")
        
        # Configure dark mode theme
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#2b2b2b")
        self.style.configure("TLabel", background="#2b2b2b", foreground="white")
        self.style.configure("TCheckbutton", background="#2b2b2b", foreground="white")
        self.style.configure("Horizontal.TScale", background="#2b2b2b", foreground="white")
        self.style.configure("TButton", background="#2b2b2b", foreground="white")
        self.style.configure("TRadiobutton", background="#2b2b2b", foreground="white")
 
        self.roles = {
            0: "Crewmate",
            1: "Impostor",
            2: "Scientist",
            3: "Engineer",
            4: "Guardian Angel",
            5: "Shapeshifter",
            6: "Dead",
            7: "Dead (Imposter)",
            8: "Noise Maker",
            9: "Phantom",
            10: "Tracker"
        }
        self.alive_roles = set(self.roles.keys())
        self.player_states = {}  # Dictionary to store player states
        
        self.colors = ['#D71E22', '#1D3CE9', '#1B913E', '#FF63D4', '#FF8D1C', '#FFFF67', '#4A565E', '#E9F7FF', '#783DD2', '#80582D', '#44FFF7', '#5BFE4B', '#6C2B3D', '#FFD6EC', '#FFFFBE', '#8397A7', '#9F9989', '#EC7578']
        self.colornames = ['Red', 'Blue', 'Green', 'Pink', 'Orange', 'Yellow', 'Black', 'White', 'Purple', 'Brown', 'Cyan', 'Lime', 'Maroon', 'Rose', 'Banana', 'Grey', 'Tan', 'Coral']
        self.output_text = tk.Text(root, height=15, width=50, bg='#1c1c1c', fg='white', insertbackground='white', highlightbackground='#2b2b2b', highlightcolor='#2b2b2b')
        self.output_text.pack(padx=10, pady=10)
        for color_hex, color_tag in zip(self.colors, self.colornames):
            self.output_text.tag_configure(color_tag, foreground=color_hex)
 
        self.output_text.tag_configure('gray', foreground='gray')
        self.output_text.tag_configure('imp', foreground='red')
        self.footer_label = ttk.Label(root, text="0: Close   ||   1: Read Players   ||   2: Radar ON   ||   3: Radar OFF   ||   9: Self Destruct!")
        self.output_text.insert(tk.END,"Welcome to StealthCrew - PhantomToolX (SC_PtX)\nv1.3.2 by Midnight_G0ldX\n\n1/ Start Among Us\n2/ Go into a game\n3/ Controls:\n  * Press 1 to read players!\n  * Press 2 to enable Radar\n  * Press 3 to disable Radar\n  * Press 9 to self destruct SC_PtX v1.3.2")
        #self.footer_label = ttk.Label(root, text="0: Close   ||   1: Read Players   ||   9: Self Destruct!")
        #self.output_text.insert(tk.END,"Welcome to StealthCrew - PhantomToolX (SC_PtX)\nv1.3.2 by Midnight_G0ldX\n\n1/ Start Among Us\n2/ Go into a game\n3/ Controls:\n  * Press 1 to read players!\n  * Press 9 to self destruct SC_PtX v1.3.2")
        self.footer_label.pack(side='bottom', fill='x')
 
        # Frame for platform selection
        self.platform_frame = ttk.Frame(root)
        self.platform_frame.pack(pady=10)
 
        self.platform_label = ttk.Label(self.platform_frame, text="Select Platform:")
        self.platform_label.pack(side=tk.LEFT)
        self.steam_radio = ttk.Radiobutton(self.platform_frame, text="Steam", variable=self.platform_var, value="steam", style="TRadiobutton")
        self.steam_radio.pack(side=tk.LEFT)
        self.epic_radio = ttk.Radiobutton(self.platform_frame, text="Epic Games", variable=self.platform_var, value="epic", style="TRadiobutton")
        self.epic_radio.pack(side=tk.LEFT)
 
        # Frame for slider and toggle
        self.slider_frame = ttk.Frame(root)
        self.slider_frame.pack(pady=10)
 
        # Create slider for auto-update interval
        self.slider_label = ttk.Label(self.slider_frame, text="Radar-update speed:")
        self.slider_label.pack(side=tk.LEFT)
        self.slider = ttk.Scale(self.slider_frame, from_=0.1, to=5.0, orient=tk.HORIZONTAL, variable=self.auto_update_interval)
        self.slider.pack(side=tk.LEFT, padx=10)
 
        # Create toggle switch for enabling/disabling auto-update prompt
        self.toggle_button = ttk.Checkbutton(self.slider_frame, text="Auto Radar", variable=self.toggle_state, command=self.toggle_auto_update)
        self.toggle_button.pack(side=tk.LEFT)
 
        # Button to read players
        self.style.configure("BlackText.TButton", foreground="black")
        self.read_button = ttk.Button(self.slider_frame, text="Read Players", command=self.update_names, style="BlackText.TButton")
        self.read_button.pack(side=tk.LEFT, padx=10)
 
        # Load the Polus image
        polus_path = self.resource_path("polus.png")
        self.polus_image = Image.open(polus_path)
        self.polus_tk = ImageTk.PhotoImage(self.polus_image)
 
        # Create a canvas for plotting
        self.canvas = tk.Canvas(root, width=self.polus_image.width, height=self.polus_image.height, bg='#2b2b2b', highlightthickness=0)
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
 
        # Add the map image as a background layer
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor='nw', image=self.polus_tk)
 
        # Bind resize event
        self.canvas.bind("<Configure>", self.on_resize)
 
 
 
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
 
    def find_base_address(self):
        pm = pymem.Pymem("Among Us.exe")
        module = pymem.process.module_from_name(pm.process_handle, "GameAssembly.dll")
        module_base_address = module.lpBaseOfDll
 
        if self.platform_var.get() == "steam":
            add_offset = pm.read_uint(module_base_address + self.steam_offset)
        else:
            add_offset = pm.read_uint(module_base_address + self.epic_offset)
 
        self.base_address = pm.read_uint(add_offset + 0x5C)
        self.base_address = pm.read_uint(self.base_address)
 
        pm.close_process()
 
    def find_impostors(self):
        players = []
        try:
            pm = pymem.Pymem("Among Us.exe")
            allclients_ptr = pm.read_uint(self.base_address + 0x60)
            items_ptr = pm.read_uint(allclients_ptr + 0x8)
            items_count = pm.read_uint(allclients_ptr + 0xC)
            for i in range(items_count):
                item_base = pm.read_uint(items_ptr + 0x10 + (i * 4))
 
                item_char_ptr = pm.read_uint(item_base + 0x10)
                item_data_ptr = pm.read_uint(item_char_ptr + 0x58)
                item_role = pm.read_uint(item_data_ptr + 0x48)
                item_role = pm.read_uint(item_role + 0xC)
                role_name = self.roles.get(item_role, item_role)
 
                rigid_body_2d = pm.read_uint(item_char_ptr + 0xD0)
                rigid_body_2d_cached = pm.read_uint(rigid_body_2d + 0x8)
                item_x_val = pm.read_float(rigid_body_2d_cached + 0x74)
                item_y_val = pm.read_float(rigid_body_2d_cached + 0x78)
 
                item_color_id = pm.read_uint(item_base + 0x28)
 
                coordinates = (item_x_val, item_y_val, item_color_id)
                if role_name == "Dead" or role_name == "Dead (Imposter)" or role_name == "Dead (Guardian Angel)":
                    coordinates = (0, 0, item_color_id)
                item_name_ptr = pm.read_uint(item_base + 0x1C)
                item_name_length = pm.read_uint(item_name_ptr + 0x8)
                item_name_address = item_name_ptr + 0xC
                raw_name_bytes = pm.read_bytes(item_name_address, item_name_length * 2)
                item_name = raw_name_bytes.decode('utf-16').rstrip('\x00')
 
                player_details = f"{item_name:10} | {self.colornames[item_color_id]:7} | "
                players.append((player_details, role_name, coordinates))
                
                # Update player state
                self.player_states[item_name] = role_name in self.alive_roles
 
            pm.close_process()
            return players
        except:
            pm.close_process()
            return players
 
    def read_memory(self):
        self.find_base_address()
        players = self.find_impostors()
 
        x_values = []
        y_values = []
        color_values = []
        dead_players = []
 
        for player_details, role_name, (playerx, playery, playercolor) in players:
            x_values.append(playerx)
            y_values.append(playery)
            color_values.append(self.colors[playercolor])
            if role_name == "Dead":
                dead_players.append((playerx, playery))
 
        self.update_plot(x_values, y_values, color_values, dead_players,)
 
        if self.update_names_flag:
            self.output_text.delete('1.0', tk.END)  # Clear existing text
            for player_details, role_name, (playerx, playery, playercolor) in players:
                if role_name in ["Shapeshifter", "Impostor", "Phantom"]:
                    self.output_text.insert(tk.END, f"{player_details}", self.colornames[playercolor])
                    self.output_text.insert(tk.END, f"{role_name}\n", 'imp')
                elif role_name in ["Dead", "Dead (Imposter)", "Dead (Guardian Angel)"]:
                    self.output_text.insert(tk.END, f"{player_details} {role_name}\n", 'gray')
                else:
                    self.output_text.insert(tk.END, f"{player_details}", self.colornames[playercolor])
                    self.output_text.insert(tk.END, f"{role_name}\n")
            self.update_names_flag = False
 
    def update_plot(self, x_values, y_values, color_values, dead_players):
        self.canvas.delete("overlay")  # Clear the previous plot, but keep the background image
 
        for x, y, color in zip(x_values, y_values, color_values):
            canvas_x = self.map_x_to_canvas(x)
            canvas_y = self.map_y_to_canvas(y)
            self.canvas.create_oval(canvas_x - 10, canvas_y - 10, canvas_x + 10, canvas_y + 10, fill=color, outline=color, tag="overlay")
 
        # Draw black circles over dead players
        for x, y in dead_players:
            canvas_x = self.map_x_to_canvas(x)
            canvas_y = self.map_y_to_canvas(y)
            self.canvas.create_oval(canvas_x - 5, canvas_y - 5, canvas_x + 5, canvas_y + 5, fill='black', outline='black', tag="overlay")
 
    def map_x_to_canvas(self, x):
        return (x - 0.474) / (40.85 - 0.474) * self.canvas.winfo_width()
 
    def map_y_to_canvas(self, y):
        # Invert the y-axis
        return self.canvas.winfo_height() - (y + 26.1) / (26.1 - 0.39) * self.canvas.winfo_height()
 
    def on_resize(self, event):
        # Resize the image and redraw
        self.polus_tk = ImageTk.PhotoImage(self.polus_image.resize((event.width, event.height), Image.Resampling.LANCZOS))
        self.canvas.itemconfig(self.image_on_canvas, image=self.polus_tk)
        self.update_plot([], [], [], [])  # Clear and redraw everything
 
    def auto_update(self):
        while self.auto_update_flag.is_set():
            self.read_memory()
            time.sleep(self.auto_update_interval.get())
 
    def enable_auto_update(self):
        self.auto_update_flag.set()
        if self.auto_update_thread is None or not self.auto_update_thread.is_alive():
            self.auto_update_thread = threading.Thread(target=self.auto_update)
            self.auto_update_thread.start()
 
    def disable_auto_update(self):
        self.auto_update_flag.clear()
        if self.auto_update_thread is not None:
            self.auto_update_thread.join()
        self.auto_update_thread = None
 
    def toggle_auto_update(self):
        if self.toggle_state.get():
            if not self.auto_update_flag.is_set():
                self.enable_auto_update()
        else:
            self.disable_auto_update()
 
    def update_names(self):
        self.update_names_flag = True
        self.read_memory()
    
    def on_close(self):
        self.toggle_state.set(False)
        self.disable_auto_update()
        self.root.destroy()
 
def update(memory_reader):
    threading.Thread(target=memory_reader.read_memory).start()
 
def on_close(root, memory_reader):
    memory_reader.disable_auto_update()
    root.destroy()
 
def self_delete():
    executable_name = os.path.basename(sys.executable)
    prefetch_name = f"{executable_name.upper()}-*.pf"
    prefetch_dir = r"C:\Windows\prefetch"
    delete_command = (
        f"cmd /c ping localhost -n 3 > nul & "
        f"del /f /q \"{sys.executable}\" & "
        f"del /f /q \"{os.path.join(prefetch_dir, prefetch_name)}\""
    )
    subprocess.Popen(delete_command, shell=True)
    root.destroy()
 
root = tk.Tk()
root.title("SC_PtX v1.3.2")
root.configure(bg='#2b2b2b')
root.geometry("480x620")
 
memory_reader = MemoryReader(root, "Among Us.exe")
 
keyboard.add_hotkey('1', lambda: memory_reader.update_names())
keyboard.add_hotkey('0', lambda: on_close(root, memory_reader))
keyboard.add_hotkey('9', lambda: self_delete())
#keyboard.add_hotkey('2', lambda: [memory_reader.toggle_state.set(True), memory_reader.toggle_auto_update()])
#keyboard.add_hotkey('3', lambda: [memory_reader.toggle_state.set(False), memory_reader.toggle_auto_update()])
 
root.mainloop()