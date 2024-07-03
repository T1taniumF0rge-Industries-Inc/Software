import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime
import requests
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
import random
import os
import json

class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033{4m'
    END = '\033[0m'

class AssistantApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Assistant App.")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, CurrentDateTime, OpenWebPage, SendEmail, RandomJoke, SystemCommand, GamesMenu, TicTacToe):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Main Menu.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        options = [
            ("Display Current Date and Time.", lambda: controller.show_frame(CurrentDateTime)),
            ("Open a Web Page.", lambda: controller.show_frame(OpenWebPage)),
            ("Send an Email.", lambda: controller.show_frame(SendEmail)),
            ("Fetch a Random Joke.", lambda: controller.show_frame(RandomJoke)),
            ("Execute a System Command.", lambda: controller.show_frame(SystemCommand)),
            ("Games Menu.", lambda: controller.show_frame(GamesMenu)),
            ("Exit.", self.quit)
        ]

        for text, command in options:
            button = tk.Button(self, text=text, width=40, height=2, command=command)
            button.pack(pady=5)

class CurrentDateTime(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Current Date and Time.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        now = datetime.datetime.now()
        datetime_str = now.strftime('%Y-%m-%d %H:%M:%S')

        datetime_label = tk.Label(self, text=datetime_str, font=('Arial', 14))
        datetime_label.pack(pady=10)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

class OpenWebPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=10, padx=10)

        open_button = tk.Button(self, text="Open.", command=self.open_webpage)
        open_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def open_webpage(self):
        url = self.url_entry.get()
        webbrowser.open(url)

class SendEmail(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Send an Email.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        self.to_label = tk.Label(self, text="To:.")
        self.to_label.pack()

        self.to_entry = tk.Entry(self, width=50)
        self.to_entry.pack(pady=5)

        self.subject_label = tk.Label(self, text="Subject:.")
        self.subject_label.pack()

        self.subject_entry = tk.Entry(self, width=50)
        self.subject_entry.pack(pady=5)

        self.message_label = tk.Label(self, text="Message:.")
        self.message_label.pack()

        self.message_text = tk.Text(self, width=50, height=10)
        self.message_text.pack(pady=5)

        send_button = tk.Button(self, text="Send.", command=self.send_email)
        send_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def send_email(self):
        smpt = simpledialog.askstring("SMTP Server","Enter an SMTP server for your mail provider. Default is 'smtp.gmail.com'\nIf you do not spell it correctly, you will get an error!")
        port = simpledialog.askinteger("SMTP Server Port","Enter a port for your SMTP server. Default for GMail is 587")
        mail = simpledialog.askstring("Email address","Enter an email address that corresponds to your provider. This will affect how the password works.")
        pwd = simpledialog.askstring("Password","Enter an app or regular password. Gmail requires app passwords due to security restrictions, which can be found at https://myaccount.google.com/apppasswords.\nIf with another email provider, check for more info.")
        to_email = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        from_email = mail
        app_pwd_or_std_pwd = pwd # Replace with your Gmail App Password. Most attempts using regular password will not work due to security restrictions. If you want to use an other mail provider, check their security restrictions to see if you need an app password like Gmail or not.

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP(smpt, port) # You can change the SMTP server and port here if you want a different mail provider like Outlook or Yahoo. Search online for more information.
            server.starttls()
            server.login(from_email, app_pwd_or_std_pwd)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            messagebox.showinfo("Email.", "Email sent successfully.")
        except Exception as e:
            messagebox.showerror("Email.", f"Failed to send email. Error: {str(e)}.")

        self.to_entry.delete(0, tk.END)
        self.subject_entry.delete(0, tk.END)
        self.message_text.delete("1.0", tk.END)

class RandomJoke(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Random Joke.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        self.joke_label = tk.Label(self, text="", font=('Arial', 14))
        self.joke_label.pack(pady=10)

        fetch_button = tk.Button(self, text="Fetch Joke.", command=self.fetch_joke)
        fetch_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def fetch_joke(self):
        try:
            response = requests.get('https://official-joke-api.appspot.com/random_joke')
            if response.status_code == 200:
                joke = response.json()
                self.joke_label.config(text=f"{joke['setup']}\n{joke['punchline']}.")
            else:
                messagebox.showerror("Joke.", "Failed to fetch joke from API.")
        except Exception as e:
            messagebox.showerror("Joke.", f"Failed to fetch joke. Error: {str(e)}.")

class SystemCommand(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="System Command.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        self.command_entry = tk.Entry(self, width=50)
        self.command_entry.pack(pady=10)

        execute_button = tk.Button(self, text="Execute.", command=self.execute_command)
        execute_button.pack(pady=5)

        self.output_text = tk.Text(self, width=80, height=10)
        self.output_text.pack(pady=10)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def execute_command(self):
        command = self.command_entry.get()
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, f"Command executed successfully.\nOutput:\n{result.stdout}.")
            else:
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert(tk.END, f"Command failed with error:\n{result.stderr}.")
        except Exception as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Failed to execute command. Error: {str(e)}.")

class GamesMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Games Menu.", font=('Arial', 18, 'bold'))
        label.pack(pady=10, padx=10)

        tic_tac_toe_button = tk.Button(self, text="Tic-Tac-Toe.", command=self.play_tic_tac_toe)
        tic_tac_toe_button.pack(pady=5)

        flappy_bird_button = tk.Button(self, text="Flappy Bird (Coming Soon).", state=tk.DISABLED)
        flappy_bird_button.pack(pady=5)

        back_button = tk.Button(self, text="Back to Menu.", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def play_tic_tac_toe(self):
        self.controller.show_frame(TicTacToe)

class TicTacToe(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.board = [" " for _ in range(9)]
        self.current_player = "X"

        label = tk.Label(self, text="Tic-Tac-Toe.", font=('Arial', 18, 'bold'))
        label.pack(pady=10)

        self.buttons = []
        for i in range(3):
            row_frame = tk.Frame(self)
            row_frame.pack()
            for j in range(3):
                button = tk.Button(row_frame, text=" ", font=('Arial', 20, 'bold'), width=8, height=4,
                                   command=lambda row=i, col=j: self.click(row, col))
                button.pack(side="left", padx=5, pady=5)
                self.buttons.append(button)

        reset_button = tk.Button(self, text="Reset.", command=self.reset_game)
        reset_button.pack(pady=10)

        back_button = tk.Button(self, text="Back to Games Menu.", command=lambda: controller.show_frame(GamesMenu))
        back_button.pack(pady=10)

    def click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe.", f"{self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tic-Tac-Toe.", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for combo in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"

if __name__ == "__main__":
    app = AssistantApp()
    app.geometry("600x500")
    app.mainloop()
