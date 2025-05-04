import requests
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

# Branding and data information
BRANDING_TEXT = (
    "GamerSoft24's GUI Time Display board for TFL London Underground - Station and Platform levels\n"
    "© Okmeque1 for original code. Original files can be found on /GamerSoft24/Software and /Okmeque1/software's GitHub repositories.\n"
    "Contains OS data © Crown copyright and database rights 2016' and Geomni UK Map data © and database rights [2019]\n"
    "Program core powered by TFL Open Data's APIs"
)

# Default configurations
DEFAULT_STATION_ID = "940GZZLUECT"  # Earl's Court Underground Station. Replace with your station's stop point ID, see https://api.tfl.gov.uk/StopPoint/Search/{query} for station ID
DEFAULT_LINE_NAME = "Piccadilly"
DEFAULT_DIRECTION = "outbound"
DEFAULT_AMT = 3
DEFAULT_REFRESH = 5

# Global variables for configuration
station_id = DEFAULT_STATION_ID
line_name = DEFAULT_LINE_NAME
direction = DEFAULT_DIRECTION
amt = DEFAULT_AMT
refresh = DEFAULT_REFRESH


def fetch_arrivals(stop_point_id, line_name=None, direction=None, is_platform=False):
    try:
        url = f"https://api.tfl.gov.uk/StopPoint/{stop_point_id}/Arrivals"
        response = requests.get(url)
        response.raise_for_status()
        arrivals = response.json()

        if is_platform:
            # Filter for platform-level data
            arrivals = [
                arrival for arrival in arrivals
                if arrival.get("lineName") == line_name and arrival.get("direction") == direction
            ]
        arrivals.sort(key=lambda x: x.get("timeToStation"))
        return arrivals
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Unable to connect to TFL Open Data Service.\nError: {e}")
        return []
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred.\nError: {e}")
        return []


def display_arrivals(arrivals, stop_point_id, is_platform=False):
    try:
        station_data = requests.get(f"https://api.tfl.gov.uk/StopPoint/{stop_point_id}").json()
        station_name = station_data.get('commonName', 'Unknown Station')
    except:
        station_name = "Unknown Station"

    current_time = datetime.now().strftime("%H:%M")
    display_text = f"{station_name}\n\n"

    if not arrivals:
        display_text += "No trains available.\n"
    else:
        for idx, arrival in enumerate(arrivals[:amt], start=1):
            destination = arrival.get("towards" if is_platform else "destinationName", "Unknown Destination")
            line = arrival.get("lineName", "Unknown Line")
            eta = arrival.get("timeToStation", 0) // 60
            display_text += f"{idx}. {line} to {destination:<50} {eta} mins\n"

    display_text += f"\nLast updated: {current_time}"
    return display_text


def update_board(is_platform):
    arrivals = fetch_arrivals(
        station_id,
        line_name=line_name if is_platform else None,
        direction=direction if is_platform else None,
        is_platform=is_platform
    )
    board_text.set(display_arrivals(arrivals, station_id, is_platform))
    root.after(refresh * 1000, lambda: update_board(is_platform))


def open_config_menu():
    global station_id, line_name, direction, amt, refresh

    def fetch_station_id():
        station_name = station_name_var.get()
        if not station_name:
            messagebox.showerror("Error", "Please enter a station name.")
            return

        try:
            # Fetch the Stop Point ID from the TFL API
            url = f"https://api.tfl.gov.uk/StopPoint/Search/{station_name} Underground Station"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if "matches" in data and data["matches"]:
                fetched_id = data["matches"][0]["id"]
                station_id_var.set(fetched_id)
                messagebox.showinfo("Success", f"Station ID for '{station_name}' fetched successfully: {fetched_id}")
            else:
                messagebox.showerror("Error", f"No matches found for station name: {station_name}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Unable to fetch Station ID.\nError: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred.\nError: {e}")

    def save_config():
        global station_id, line_name, direction, amt, refresh
        station_id = station_id_var.get()
        line_name = line_name_var.get()
        direction = direction_var.get()
        amt = int(train_amt_var.get())
        refresh = int(refresh_time_var.get())
        config_window.destroy()

    config_window = tk.Toplevel(root)
    config_window.title("Configuration Menu")

    # Station Name Input
    tk.Label(config_window, text="Station Name:").grid(row=0, column=0, sticky="w")
    station_name_var = tk.StringVar()
    tk.Entry(config_window, textvariable=station_name_var).grid(row=0, column=1)
    tk.Button(config_window, text="Fetch ID", command=fetch_station_id).grid(row=0, column=2)

    # Station ID Input
    tk.Label(config_window, text="Station ID:").grid(row=1, column=0, sticky="w")
    station_id_var = tk.StringVar(value=station_id)
    tk.Entry(config_window, textvariable=station_id_var).grid(row=1, column=1)

    # Line Name Input
    tk.Label(config_window, text="Line Name:").grid(row=2, column=0, sticky="w")
    line_name_var = tk.StringVar(value=line_name)
    tk.Entry(config_window, textvariable=line_name_var).grid(row=2, column=1)

    # Direction Input
    tk.Label(config_window, text="Direction (inbound/outbound):").grid(row=3, column=0, sticky="w")
    direction_var = tk.StringVar(value=direction)
    tk.Entry(config_window, textvariable=direction_var).grid(row=3, column=1)

    # Number of Trains Input
    tk.Label(config_window, text="Number of Trains:").grid(row=4, column=0, sticky="w")
    train_amt_var = tk.StringVar(value=str(amt))
    tk.Entry(config_window, textvariable=train_amt_var).grid(row=4, column=1)

    # Refresh Time Input
    tk.Label(config_window, text="Refresh Time (seconds):").grid(row=5, column=0, sticky="w")
    refresh_time_var = tk.StringVar(value=str(refresh))
    tk.Entry(config_window, textvariable=refresh_time_var).grid(row=5, column=1)

    # Save Button
    tk.Button(config_window, text="Save", command=save_config).grid(row=6, column=0, columnspan=2)


def choose_mode():
    mode = simpledialog.askstring(
        "Choose Mode",
        "Enter 'station' for Station Level or 'platform' for Platform Level:",
        parent=root
    )
    if mode and mode.lower() == "platform":
        update_board(is_platform=True)
    elif mode and mode.lower() == "station":
        update_board(is_platform=False)
    else:
        messagebox.showerror("Error", "Invalid mode selected. Please restart the program.")
        root.destroy()


# Initialize GUI
root = tk.Tk()
root.title("TFL Tube Times AIO - GUI mode")

# Branding and information
branding_label = tk.Label(root, text=BRANDING_TEXT, justify="left", font=("Arial", 10))
branding_label.pack(pady=10)

# Display board
board_text = tk.StringVar()
board_label = tk.Label(root, textvariable=board_text, justify="left", font=("Courier", 12))
board_label.pack(pady=10)

# Configuration button
config_button = tk.Button(root, text="Configuration Menu", command=open_config_menu)
config_button.pack(pady=5)

# Choose mode and start
choose_mode()
root.mainloop()
