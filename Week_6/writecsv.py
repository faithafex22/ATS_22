import csv

#header = ['name', 'area', 'code1', 'code2']
#data =  [['Albania', 28748, 'AL', 'ALB'],
#        ['Algeria', 2381741, 'DZ', 'DZA'],
#        ['American', 199, 'AS', 'ASM'],
#        ['Andorra', 468, 'AD', 'AND'],
#        ['Angola', 1246700, 'AO', 'AGO']]
#with open('file2.csv', 'w', encoding= 'utf8', newline="") as f:
#    writer = csv.writer(f)
#    writer.writerow(header)
    #writer.writerows(data)

#writing to a csv file using dictclass
fieldnames = ['name', 'area', 'country_code2', 'country_code3']
# csv data
data = [
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]

with open('file3.csv', 'w', encoding='utf8', newline='' ) as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)



