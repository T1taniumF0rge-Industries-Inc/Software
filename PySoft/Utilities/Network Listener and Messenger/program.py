import os
import socket
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import nmap
from scapy.all import ARP, Ether, srp
import threading


class NetworkMessengerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Messenger")

        # GUI elements
        self.label = tk.Label(root, text="Enter Network Range (e.g., 192.168.1.0/24):")
        self.label.pack(pady=5)

        self.network_entry = tk.Entry(root, width=30)
        self.network_entry.pack(pady=5)

        self.scan_button = tk.Button(root, text="Scan Network", command=self.scan_network)
        self.scan_button.pack(pady=10)

        self.message_label = tk.Label(root, text="Message to Send:")
        self.message_label.pack(pady=5)

        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.pack(pady=5)

        self.devices_list = tk.Listbox(root, width=70, height=15)
        self.devices_list.pack(pady=10)

        self.send_button = tk.Button(root, text="Send Popup", command=self.send_popup)
        self.send_button.pack(side=tk.LEFT, padx=10)

        self.chat_button = tk.Button(root, text="Start Chat", command=self.start_chat)
        self.chat_button.pack(side=tk.RIGHT, padx=10)

        # Popup and chat listener threads
        threading.Thread(target=self.start_popup_listener, daemon=True).start()
        threading.Thread(target=self.start_chat_server, daemon=True).start()

    def scan_network(self):
        """Scan the network for devices and update the listbox."""
        network_range = self.network_entry.get()
        if not network_range:
            messagebox.showerror("Error", "Please enter a valid network range.")
            return

        self.devices_list.delete(0, tk.END)
        devices = self._scan_network(network_range)
        if devices:
            for device in devices:
                device_info = f"IP: {device['ip']} | MAC: {device['mac']}"
                self.devices_list.insert(tk.END, device_info)
        else:
            messagebox.showinfo("Scan Complete", "No devices found on the network.")

    def send_popup(self):
        """Send a popup message to the selected device."""
        selected = self.devices_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a device from the list.")
            return

        message = self.message_entry.get()
        if not message:
            messagebox.showerror("Error", "Please enter a message.")
            return

        device_info = self.devices_list.get(selected[0])
        ip = device_info.split(" | ")[0].split(": ")[1]

        try:
            self._send_popup(ip, message)
            messagebox.showinfo("Success", f"Popup sent to {ip}.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send popup: {e}")

    def start_chat(self):
        """Start a chat session with the selected device."""
        selected = self.devices_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Please select a device from the list.")
            return

        device_info = self.devices_list.get(selected[0])
        ip = device_info.split(" | ")[0].split(": ")[1]

        chat_message = simpledialog.askstring("Chat", "Enter your message:")
        if chat_message:
            try:
                reply = self._send_chat_message(ip, chat_message)
                messagebox.showinfo("Reply", f"Reply from {ip}: {reply}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send chat message: {e}")

    def start_popup_listener(self):
        """Start a listener for incoming popup messages."""
        def popup_server():
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(("0.0.0.0", 5000))
            server_socket.listen(5)

            while True:
                client_socket, addr = server_socket.accept()
                message = client_socket.recv(1024).decode()
                client_socket.close()
                self._show_popup(message)

        threading.Thread(target=popup_server, daemon=True).start()

    def start_chat_server(self):
        """Start a simple chat server for two-way communication."""
        def chat_server():
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(("0.0.0.0", 6000))
            server_socket.listen(5)

            while True:
                client_socket, addr = server_socket.accept()
                message = client_socket.recv(1024).decode()
                reply = simpledialog.askstring("Chat Reply", f"Message from {addr[0]}: {message}\nEnter your reply:")
                client_socket.send(reply.encode())
                client_socket.close()

        threading.Thread(target=chat_server, daemon=True).start()

    def _scan_network(self, ip_range):
        """Perform ARP-based network scanning."""
        arp_request = ARP(pdst=ip_range)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

        devices = []
        for element in answered_list:
            devices.append({'ip': element[1].psrc, 'mac': element[1].hwsrc})
        return devices

    def _send_popup(self, ip, message):
        """Send a popup notification to the target device."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, 5000))  # Assumes target device has a listener on port 5000
        sock.send(message.encode())
        sock.close()

    def _show_popup(self, message):
        """Display a popup message."""
        messagebox.showinfo("Popup Notification", message)

    def _send_chat_message(self, ip, message):
        """Send a chat message to the target device."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, 6000))  # Assumes target device has a listener on port 6000
        sock.send(message.encode())
        reply = sock.recv(1024).decode()
        sock.close()
        return reply


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkMessengerApp(root)
    root.mainloop()
