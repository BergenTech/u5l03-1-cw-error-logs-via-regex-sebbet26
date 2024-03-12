import csv, json, re

with open("logs.json") as jsonFile:
    data = json.load(jsonFile)
    pattern = r"ERROR"
    li = []
    for entry in data:
        match = re.match(pattern, entry["level"], re.IGNORECASE)
        li.append(match)
    with open("logs.csv", "w+", newline='') as csvFile:
        for item in li:
            if item != None:
                writer = csv.DictWriter()
                writer.writeheader("timestamp", "level", "message")