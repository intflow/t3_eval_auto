import os
import csv
import json


with open('500_sel_results_t.json') as json_file:
    json_data = json.load(json_file)

with open('lab_GC19_pseudotrue.csv', 'r', encoding='utf-8-sig') as csv_file:
    csv_data = csv.reader(csv_file)
    i = 0
    for line in csv_data:
        print(line)
        json_data['track3_results'][i]['angle'] = int(line[0])
        i+=1
        
with open('lab_GC19_pseudotrue.json', "w") as json_file:
    json.dump(json_data, json_file, indent=4)
    