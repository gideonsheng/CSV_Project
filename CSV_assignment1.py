import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file_dv = open("death_valley_2018_simple.csv", "r")
open_file_sk = open("sitka_weather_2018_simple.csv", "r")

csv_file_dv = csv.reader (open_file_dv, delimiter = ",")
csv_file_sk = csv.reader (open_file_sk, delimiter = ",")

header_row_dv = next(csv_file_dv)
header_row_sk = next(csv_file_sk)

highs_dv = []
dates_dv = []
lows_dv = []

highs_sk = []
dates_sk = []
lows_sk = []

for row in csv_file_dv:
    try:
        high_dv= int(row[4])
        low_dv = int(row[5])
        current_date_dv = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print (f"Missing Data for {current_date_dv}")
    else:
        highs_dv.append(high_dv)
        lows_dv.append(low_dv)
        dates_dv.append(current_date_dv)



for row in csv_file_sk:
    try:
        high_sk= int(row[4])
        low_sk = int(row[5])
        current_date_sk = datetime.strptime(row[2],'%Y-%m-%d')
    except ValueError:
        print (f"Missing Data for {current_date_sk}")
    else:
        highs_sk.append(high_sk)
        lows_sk.append(low_sk)
        dates_sk.append(current_date_sk)



fig, ax = plt.subplots(2,1)

plt.plot(dates_dv, highs_dv, color='red', alpha=0.5)
plt.plot(dates_dv, lows_dv, color='blue',alpha=0.5)
plt.fill_between(dates_dv,highs_dv,lows_dv, facecolor='blue',alpha=0.1)
plt.title("Daily high temps for Death Valley", fontsize=16)
plt.xlabel("",fontsize=10)
plt.ylabel("Temperature(F)",fontsize=12)
plt.tick_params(axis='both',which='major',labelsize=12)

fig.autofmt_xdate()

plt.show()