number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0 
while index < len(number_list):
    if number_list[index] % 2 == 0:
        print(number_list[index])
    index = index+1

for number in number_list:
    if number % 2 == 0:
        print(number)              