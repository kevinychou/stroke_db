# stroke_db
Scripts used working with Dr Carlos Garcia-Esperon for analysing the Telestroke database. 

## Repo Contents
* find_and_code.py: Script used to replace a column of repetitive strings with numbers. (i.e. grouping drug management together)
* gmaps_calculator.py: Uses Google Maps API to calculate distance and time away from patient's home address and the hospital. Takes in a spreadsheet which expects the header "Address" with corresponding addresses.

## Use Notes
The repo expects the environment variables:
* API_KEY = Key for Google Maps API account. Go [here](https://developers.google.com/maps/documentation/distance-matrix/cloud-setup) more info.
* FILE_NAME = Name of input file with hospitals.
* OUTPUT_FILE_NAME = Name of output file with distance results.
* HOSPITALS = List of hospital names.