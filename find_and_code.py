import pandas as pd
from tqdm import tqdm

FILE_NAME = "input.xlsx"
OUTPUT_FILE_NAME = "output.xlsx"

CODES = {
    #Antiplatelet Management 
    "dapt": 1, "stop plavix": 1, "aspirin": 1, "clopidogrel": 1, "antiplatelet": 1, "prasugrel": 1, 
    # OAC Managememt 
    "Oac": 2, "warfarin": 2, "apixaban": 2, "rivaroxaban": 2, "dabigatran": 2, 
    # Antiepileptic Management 
    "antiepileptic": 3, "tegretrol": 3, "lamotrigine": 3, "carbamazepine": 3, "valproate": 3, 
    # Antihypertensive Management 
    "antihypertensive": 4, "propaOlol": 4, "propanolol": 4,
    # Statin Management 
    "statin": 5, "atorva": 5, "crestor": 5, 
    # Other 
    "melatonin": 6, "quetiapine": 6, 
    }


def main():
    # Read excel with data, and read-in "Address" column
    meds = pd.read_excel(FILE_NAME, usecols=["If change in meds (or dose), describe"])
    # Create list for med codes
    med_codes = []

    # Create dict for faster iteration
    meds_dict = meds.to_dict("records")
    for row in tqdm(meds_dict):
        med_note = row["If change in meds (or dose), describe"]
        current_med = ""
        print(med_note)
        # Check if med_note empty
        if med_note and not pd.isnull(med_note):
            # Check if keys are present in string
            values = [val for key, val in CODES.items() if key in med_note.lower()]
            for code in values:
                current_med += str(code) + ", "
            current_med = current_med[:-2]

        med_codes.append(current_med)

    meds = meds.join(pd.DataFrame(med_codes, columns=["Change in meds (Coded)"]))

    # Write to excel
    meds.to_excel(OUTPUT_FILE_NAME)
    return


if __name__ == "__main__":
    main()
