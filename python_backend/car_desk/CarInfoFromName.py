import csv
import json



parameters = ["Cylinders", "Displacement", "DriveTR", "Manufacturer", "Model", "Trany", "MkYear","TurboCharger","SuperCharger", "ChargeTime", "Start/Stop"]

def car_info(carName):
    
    yearCheck = False
    with open("carData.json", "w") as outfile:
        
        #Get Data From CarInfo CSV and find data with model year and put it in a json
        with open('CarInfoSorted.csv', "r") as f:
                
                csvreader = csv.reader(f,delimiter=',', quotechar='"')

                for row in csvreader:
                    if any(row):
                        if row[3] in carName and row[4] in carName and row[6] in carName:
                            yearCheck = True
                            specs_dictionary = dict(zip(parameters, row))
                            outfile.write(json.dumps(specs_dictionary, indent=11))
                            
                        

        #Get Data From CarInfo CSV and find data with NO model year and put it in a json
        with open('CarInfoSorted.csv', "r") as f:
         
                csvreader = csv.reader(f,delimiter=',', quotechar='"')

                for row in csvreader:
                    if any(row):
                        if yearCheck == False:
                            if row[3] in carName and row[4] in carName:
                                specs_dictionary = dict(zip(parameters, row))
                                outfile.write(json.dumps(specs_dictionary, indent=11))                  
        

car_info("Volkswagen Golf 2021")

    