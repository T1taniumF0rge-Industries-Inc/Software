import requests
import time
from datetime import datetime
import os
print("Okmeque1 Time Display board for TFL London Underground - Station Level board")
STOP_POINT_ID = "940GZZLUECT"  # Replace with your station's stop point ID, see https://api.tfl.gov.uk/StopPoint/Search/{query} for station ID
amt = 5 #default amount, you can have more trains show up.
refresh = 5 #amount of time to wait before board refreshes. Lower refresh time may increase CPU usage
print("Contains OS data © Crown copyright and database rights 2016' and Geomni UK Map data © and database rights [2019]")
print("Powered by TFL Open Data\nPlease wait, program is loading...")
time.sleep(3)
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
def fetch_arrivals(stop_point_id):
    try:
        url = f"https://api.tfl.gov.uk/StopPoint/{stop_point_id}/Arrivals"
        params = {"app_key": ""}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Load Error - Can't fetch arrivals\nError {response.status_code}")
            input("Press ENTER to EXIT")
            exit()
    except requests.exceptions.ConnectionError as e:
        print(f"Load Error - Unable to connect to TFL Open Data Service\nPlease check your connection, API keys or service status\nError : 1E/08 : {e}")
        input("Press ENTER to EXIT")
        exit()
    except Exception as e:
        print(f"Load Error: {e}")
        input("Press ENTER to EXIT")
        exit()
def format_arrivals(data,AMT):
    arrivals = []
    for item in data:
        destination = item.get("destinationName", "Unknown")
        line_name = item.get("lineName", "Unknown")
        time_to_station = item.get("timeToStation", 0) // 60
        arrivals.append((line_name, destination, time_to_station))
    arrivals = sorted(arrivals, key=lambda x: x[2])
    return arrivals[:AMT]
def display_board(arrivals,stop_point_id):
    current_time = datetime.now().strftime("%H:%M")
    if not arrivals:
        print("Powered by TfL Open Data - London Underground\nLondon Underground services are not available. Please check your connection, API keys or the service status.")
    else:
        unformatted = requests.get(f"https://api.tfl.gov.uk/StopPoint/{stop_point_id}")
        data = unformatted.json()
        station_name = data.get('commonName', 'Unknown Station')
        print(f"{station_name}")
        for idx, (line, destination, eta) in enumerate(arrivals, start=1):
            print(f"{idx} {destination:<55} {eta} mins")
        print(f"{current_time} - Press CTRL-C to enter CONFIGURATION MENU")
def main(refresh,amt,STOP_POINT_ID):
    print("Fetching TfL train arrivals, please wait...")
    try:
        while True:
            arrivals_data = fetch_arrivals(STOP_POINT_ID)
            arrivals = format_arrivals(arrivals_data,amt)
            os.system("cls")
            display_board(arrivals,STOP_POINT_ID)
            time.sleep(refresh)
    except KeyboardInterrupt:
            flag = True
            STATION_ID1 = STOP_POINT_ID
            amt1 = amt
            refresh1 = refresh
            while flag:
                clear()
                print("*** CONFIGURATION MENU ***")
                print("[1] Set STATION ID")
                print("[2] Set TRAIN AMOUNT")
                print("[3] Set Refresh Time")
                print("[4] Save and return to program")
                print("[5] Discard and return to program")
                print("[6] Reset Defaults")
                print("[7] View configuration")
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
                            station_name = input(
                                "Enter station name - The name must be written exactly and must include all symbols and have its first letters capitalized: ")
                            unformatted = requests.get(
                                f"https://api.tfl.gov.uk/StopPoint/Search/{station_name} Underground Station")
                            jsoned = unformatted.json()
                            STATION_ID1 = jsoned["matches"][0]["id"]
                            input("Station ID successfully set. Press ENTER to continue...")
                        except requests.exceptions.RequestException as e:
                            print(
                                f"Load Error - Unable to connect to TFL Open Data Service\nPlease check your connection, API keys or service status\nError : 1E/08 : {e}")
                            input("Press ENTER to return to CONFIGURATION MENU")
                        except Exception as e:
                            print(f"Load Error: {e}")
                            input("Press ENTER to return to CONFIGURATION MENU")
                    else:
                        pass
                elif option == 2:
                    print(
                        "*** TRAIN AMOUNT ***\nThis option will change how many trains will display on the arrival board.")
                    amt1 = int(input("Enter the amount of trains being displayed: "))
                    input("Train amount successfully set. Press ENTER to continue...")
                elif option == 3:
                    print(
                        "*** REFRESH TIME ***\nThis option will set how many seconds to wait before refreshing. Note that low refresh times may increase CPU usage")
                    refresh1 = int(input("Enter refresh time in seconds: "))
                    input("Refresh time successfully set. Press ENTER to continue...")
                elif option == 4:
                    STOP_POINT_ID = STATION_ID1
                    amt = amt1
                    refresh = refresh1
                    flag = False
                    input("Station ID successfully set. Press ENTER to return to main program...")
                    main(refresh, amt,STOP_POINT_ID)
                elif option == 5:
                    flag = False
                    main()
                elif option == 6:
                    STATION_ID = "940GZZLUECT"  # Earl's Court
                    amt = 3  # default, shows trains
                    refresh = 5  # refresh time. Putting it on low amounts may increase CPU usage
                    input("Reset defaults. Press ENTER to continue...")
                elif option == 7:
                    clear()
                    print("*** VIEW CONFIGURATION ***")
                    print(f"STATION ID: {STATION_ID1}")
                    unformatted = requests.get(f"https://api.tfl.gov.uk/StopPoint/{STATION_ID1}")
                    data = unformatted.json()
                    station_name = data.get('commonName', 'Unknown Station')
                    print(f"STATION NAME: {station_name}")
                    print(f"TRAIN AMOUNT: {amt1}")
                    print(f"REFRESH TIME: {refresh1}")
                    input("Press ENTER to return to CONFIGURATION MENU")
                elif option == 8:
                    print("*** ABOUT THIS PROGRAM ***")
                    print("This version of the TFL/London Underground Time board is made to see the arrivals of trains in any London Underground Station. In particular, this version is at a station level and is exactly what you were at the entrance of the station")
                    input("Press ENTER to return to CONFIGURATION MENU")
    except Exception as e:
        print(f"Failed to load arrivals: {e}")
if __name__ == "__main__":
    main(refresh,amt,STOP_POINT_ID)
