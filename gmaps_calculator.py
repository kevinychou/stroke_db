import pandas as pd
import requests
import os
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()
HOSPITALS = os.getenv('HOSPITALS')
OUTPUT_FILE_NAME = os.getenv('OUTPUT_FILE_NAME')
FILE_NAME = os.getenv('FILE_NAME')
API_KEY = os.getenv('API_KEY')

def main():
    # Read excel with data, and read-in "Address" column
    addresses = pd.read_excel(FILE_NAME, usecols=["Address"], sheet_name=0) # Change sheet_name based on sheet index
    # Create lists to contain distance/time for hospitals
    hosp1_data = []
    hosp2_data = []
    
    # Create dict for faster iteration
    addresses_dict = addresses.to_dict("records")
    for row in tqdm(addresses_dict):
        patient_loc = row["Address"]
        print(patient_loc)
        # Check if patient_loc empty
        if patient_loc:
            # Calculate hospital distances with patient location
            hosp1_data.append(get_distance_time(patient_loc, HOSPITALS[0]))
            hosp2_data.append(get_distance_time(patient_loc, HOSPITALS[1]))
        else:
            hosp1_data.append([])
            hosp2_data.append([])
    
    # Append new data to dataframe
    addresses = addresses.join(pd.DataFrame(hosp1_data, columns=[HOSPITALS[0] + " Distance (km)", HOSPITALS[0] + " Time (min)"]))
    addresses = addresses.join(pd.DataFrame(hosp2_data, columns=[HOSPITALS[1] + " Distance (km)", HOSPITALS[1] + " Time (min)"]))

    # Write to excel
    addresses.to_excel(OUTPUT_FILE_NAME)
    return


def get_distance_time(loc1, loc2):
    # Use Distance Matrix API to get data
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&key={}".format(loc1, loc2, API_KEY)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    json = response.json()
    rows = json["rows"][0]["elements"][0]
    # Obtain values from json, and round to 1dp and 0dp
    try:
        distance = round(rows["distance"]["value"]/1000, 1)
        time = round(rows["duration"]["value"]/60)
    except KeyError:
        print("Invalid address")
        return (None, None)
    return (distance, time)


if __name__ == "__main__":
    main()
