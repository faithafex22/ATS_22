import csv

#with open("C:\\Users\\FaithOdunayoAdeosun\\Documents\\ATS_22\\Week_3\\data.csv", "r") as f:
    #handler = csv.reader(f)
    ##print(rows)

with open("C:\\Users\\FaithOdunayoAdeosun\\Document9s\\ATS_22\\Week_3\\new.csv", "w") as f:
    handler = csv.writer(f)
    handler.writerow(["Firstname"],["Lastname"],["Age"],["Year"])