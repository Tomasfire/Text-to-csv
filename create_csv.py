import re, csv

pattern = r"(.*):.(.*)"
row = []
header = ("ID", "Jmeno", "Prijmeni", "Auto")

with open("report.csv","w") as csv_file:
    csv_object = csv.writer(csv_file)
    csv_object.writerow(header)
    with open("text.txt") as f:
        for line in f.readlines():
            match = re.match(pattern, line)
            if match.group(1) == "ID":
                if row:
                    csv_object.writerow(row)
                row = []
                row.append(match.group(2))
            else:
                row.append(match.group(2))
        csv_object.writerow(row)