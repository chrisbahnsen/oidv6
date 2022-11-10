import json
import csv

with open("all.classes.overview.json", 'r') as f:
    classOverview = json.load(f)

fieldnames = ['class', 'train', 'test', 'validation']

with open('classInfo.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for className, info in classOverview.items():
        csvInfo = dict()
        csvInfo['class'] = className

        for stage, count in info.items():
            csvInfo[stage] = count

        writer.writerow(csvInfo)


