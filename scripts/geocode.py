import csv
from gridref2latlng import gridref2latlng

CSV_IN = "../Collision Data/accident-2010-13.csv"
CSV_OUT = "../Collision Data/accident-2010-13-geocoded.csv"

def main():
    with open(CSV_IN) as csvfile:

        reader = csv.reader(csvfile)
        header = next(reader)

        csv_out = []    

        for line in reader:
            (easting, northing) = line[27:29]
            
            lat, lng = gridref2latlng(float(easting), float(northing), verbose=False)
            
            
            #date = datetime.datetime(int(year), 1, 1, 12, 0, 0).isoformat()
            csv_out.append(line+[lat, lng])
            
    with open(CSV_OUT, 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header + ['latitude', 'longitude'])
            writer.writerows(csv_out) 
            print('Writing text to %s' % CSV_OUT)    


if __name__ == "__main__":
    main() 