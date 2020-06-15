import csv
import json
import sys
csvFilePath = sys.argv[0:]
jsonFilePath = sys.argv[1:]
csvFilePath = "Engagementques.csv"
jsonFilePath = "Engagementques.json"

# reading
data = {}
with open(csvFilePath, encoding='utf-8-sig') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        id = csvRow['id']
        data[id] = csvRow
# writing
with open('jsonFilePath', 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
