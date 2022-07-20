import csv
#with open("file3.csv", encoding="utf8") as f:
#    csv_reader = csv.DictReader(f)
#    print(csv_reader)
#    h =[]
#    for line in csv_reader:
#        h.append(line)
#    print(h[0])
#
#with open("file3.csv", encoding="utf8") as f:
#    csv_reader = csv.reader(f)
#    print(csv_reader)
#    for line in csv_reader:
#        print(line)
#
#with open('file3.csv', encoding="utf8") as f:
#    csv_reader = csv.reader(f)
#    for line_no, line in enumerate(csv_reader, 1):
#        if line_no == 1:
#            print('Header:')
#            print(line)  # header
#            print('Data:')
#        else:
#            print(line)  # data
fieldname = ['name', 'area', 'code1', 'code2']
with open('file3.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f, fieldname)

    # skip the first row
    next(csv_reader)

    # show the data
    for line in csv_reader:
        print(line)
