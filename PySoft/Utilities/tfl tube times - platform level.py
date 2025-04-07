import requests
import time
from datetime import datetime
import os
print("Okmeque1 Time Display board for TFL London Underground - Platform Level board")
print("Contains OS data © Crown copyright and database rights 2016' and Geomni UK Map data © and database rights [2019]")
print("Powered by TFL Open Data\nPlease wait, program is loading...")
time.sleep(3)
API_URL = "https://api.tfl.gov.uk/StopPoint/{station_id}/Arrivals"
STATION_ID = "940GZZLUECT"  # Replace with the StopPoint ID of the station
LINE_NAME = "Piccadilly"  # make sure to spell it properly
DIRECTION = "outbound"
amt = 3 #default, shows trains
refresh = 5 #refresh time. Putting it on low amounts may increase CPU usage
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
def fetch_arrivals(station_id, line_name, direction):
    try:
        response = requests.get(API_URL.format(station_id=station_id))
        response.raise_for_status()
        arrivals = response.json()
        filtered_arrivals = [
            arrival for arrival in arrivals
            if arrival.get("lineName") == line_name and arrival.get("direction") == direction
        ]
        filtered_arrivals.sort(key=lambda x: x.get("timeToStation"))
        return filtered_arrivals
    except requests.exceptions.RequestException as e:
        print(f"Load Error - Unable to connect to TFL Open Data Service\nPlease check your connection, API keys or service status\nError : 1E/08 : {e}")
        input("Press ENTER to EXIT, CTRL-C to enter CONFIGURATION MENU")
        exit()
    except Exception as e:
        print(f"Load Error: {e}")
        input("Press ENTER to EXIT, CTRL-C to enter CONFIGURATION MENU")
        exit()
def display_board(arrivals,AMT,direction, line_name, station_id):
    current_time = datetime.now().strftime("%H:%M")
    unformatted = requests.get(f"https://api.tfl.gov.uk/StopPoint/{station_id}")
    data = unformatted.json()
    station_name = data.get('commonName', 'Unknown Station')
    if not arrivals:
        print(f"{station_name}: {direction} {line_name} line trains.")
        print(f"{current_time} - Press CTRL-C to enter CONFIGURATION MENU")
    else:
        print(f"{station_name}: {direction} {line_name} line trains.")
        for idx, train in enumerate(arrivals[:AMT], start=1):
            destination = train.get("towards", "Unknown Destination")
            time_to_arrival = train.get("timeToStation", 0) // 60
            print(f"{idx} {destination:<50} {time_to_arrival} mins")
        print(f"{current_time} - Press CTRL-C to enter CONFIGURATION MENU")
def main(STATION_ID, LINE_NAME, DIRECTION, refresh, amt):
    try:
        while True:
            arrivals = fetch_arrivals(STATION_ID, LINE_NAME, DIRECTION)
            clear()
            display_board(arrivals,amt,DIRECTION,LINE_NAME,STATION_ID)
            time.sleep(refresh)
    except KeyboardInterrupt:
        flag = True
        STATION_ID1 = STATION_ID
        LINE_NAME1 = LINE_NAME
        DIRECTION1 = DIRECTION
        amt1 = amt
        refresh1 = refresh
        while flag:
            clear()
            print("*** CONFIGURATION MENU ***")
            print("[1] Set STATION ID")
            print("[2] Set TUBE LINE")
            print("[3] Set TRAIN AMOUNT")
            print("[4] Change Direction")
            print("[5] Set Refresh Time")
            print("[6] Save and return to program")
            print("[7] Discard and return to program")
            print("[8] Reset Defaults")
            print("[9] View configuration")
            print("[10] About")
            option = int(input("Select an an option: "))
            if option == 1:
                clear()
                print("*** STATION ID ***\nThis option will select the desired station to show arrivals")
                print("[1] Enter station ID manually")
                print("[2] Enter station name")
                print("[3] Return to CONFIGURATION MENU")
                stations = int(input("Select an option: "))
                if stations == 1:
                    STATION_ID1 = input("Enter STATION ID: ")
                    input("Station ID successfully set. Press ENTER to continue...")
                elif stations == 2:
                    try:
                        station_name = input("Enter station name - The name must be written exactly and must include all symbols and have its first letters capitalized: ")
                        unformatted = requests.get(f"https://api.tfl.gov.uk/StopPoint/Search/{station_name} Underground Station")
                        jsoned = unformatted.json()
                        STATION_ID1 = jsoned["matches"][0]["id"]
                        input("Station ID successfully set. Press ENTER to continue...")
                    except requests.exceptions.RequestException as e:
                        print(f"Load Error - Unable to connect to TFL Open Data Service\nPlease check your connection, API keys or service status\nError : 1E/08 : {e}")
                        input("Press ENTER to return to CONFIGURATION MENU")
                    except Exception as e:
                        print(f"Load Error: {e}")
                        input("Press ENTER to return to CONFIGURATION MENU")
                else:
                    pass
            elif option == 2:
                print("*** LINE ***\nThis option will set the desired line for arrivals")
                LINE_NAME1 = input("Enter the name of the line. The first letter must be capitalized.: ")
                input("Line name successfully set. Press ENTER to continue...")
            elif option == 3:
                print("*** TRAIN AMOUNT ***\nThis option will change how many trains will display on the arrival board.")
                amt1 = int(input("Enter the amount of trains being displayed: "))
                input("Train amount successfully set. Press ENTER to continue...")
            elif option == 4:
                if DIRECTION1 == "inbound":
                    DIRECTION1 = "outbound"
                else:
                    DIRECTION1 = "inbound"
                input(f"Direction is now {DIRECTION1}. Press ENTER to continue...")
            elif option == 5:
                print("*** REFRESH TIME ***\nThis option will set how many seconds to wait before refreshing. Note that low refresh times may increase CPU usage")
                refresh1 = int(input("Enter refresh time in seconds: "))
                input("Refresh time successfully set. Press ENTER to continue...")
            elif option == 6:
                STATION_ID = STATION_ID1
                LINE_NAME = LINE_NAME1
                DIRECTION = DIRECTION1
                amt = amt1
                refresh = refresh1
                flag = False
                input("Station ID successfully set. Press ENTER to return to main program...")
                main(STATION_ID, LINE_NAME, DIRECTION, refresh, amt)
            elif option == 7:
                flag = False
                main()
            elif option == 8:
                STATION_ID = "940GZZLUECT"  # Earl's Court
                LINE_NAME = "Piccadilly"  # make sure to spell it properly
                DIRECTION = "inbound" #The train now approaching is to Heathrow Terminals 4 and Terminals 2 & 3, please stand back from the platform edge.
                amt = 3  # default, shows trains
                refresh = 5  # refresh time. Putting it on low amounts may increase CPU usage
                input("Reset defaults. Press ENTER to continue...")
            elif option == 9:
                clear()
                print("*** VIEW CONFIGURATION ***")
                print(f"STATION ID: {STATION_ID1}")
                unformatted = requests.get(f"https://api.tfl.gov.uk/StopPoint/{STATION_ID1}")
                data = unformatted.json()
                station_name = data.get('commonName', 'Unknown Station')
                print(f"STATION NAME: {station_name}")
                print(f"LINE: {LINE_NAME1}")
                print(f"DIRECTION: {DIRECTION1}")
                print(f"TRAIN AMOUNT: {amt1}")
                print(f"REFRESH TIME: {refresh1}")
                input("Press ENTER to return to CONFIGURATION MENU")
            elif option == 10:
                print("*** ABOUT THIS PROGRAM ***")
                print("This version of the TFL/London Underground Time board is made to see the arrivals of trains in any London Underground Station. In particular, this version is at a platform level and is exactly what you would see if you were on the platform.")
                input("Press ENTER to return to CONFIGURATION MENU")
if __name__ == "__main__":
    main(STATION_ID, LINE_NAME, DIRECTION, refresh, amt)
