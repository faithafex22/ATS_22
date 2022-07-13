# #array = [1,2,3,4,5]
# #for i in range (len(array)):
#    # print(i)

# def binarySearch(array, searchelement, low, high):
#     if high >= low:
    
#         mid = low + (high - low)//2

#         # If found at mid, then return it
#         if array[mid] == searchelement:
#             return mid

#         # Search the left half
#         elif array[mid] > searchelement:
#             return binarySearch(array, searchelement, low, mid-1)

#         # Search the right half
#         else:
#             return binarySearch(array, searchelement, mid + 1, high)

#     else:
#         return -1


# array = [4, 8, 10, 12, 15, 17, 18]
# searchelement = 12

# result = binarySearch(array, searchelement, 0, len(array)-1)

# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")

salesperson = [{'sp1':400, 'sp2':300, 'sp3':500, 'sp4':1000},
            {'sp1':500, 'sp2':600, 'sp3':700, 'sp4':200},
            {'sp1':800, 'sp2':1000, 'sp3':400, 'sp4':900}, 
            {'sp1':750, 'sp2':859, 'sp3':950, 'sp4':650},
            {'sp1':600, 'sp2':700, 'sp3':850,  'sp4':250}]
    
salespersonlist = []

salesperson1 = sum(item['sp1'] for item in salesperson)
salespersonlist.append(salesperson1)
salesperson2 =sum(item['sp2'] for item in salesperson)
salespersonlist.append(salesperson2)
saleperson3 = sum(item['sp3'] for item in salesperson)
salespersonlist.append(saleperson3)
saleperson4 = sum(item['sp4'] for item in salesperson)
salespersonlist.append(saleperson4)
print(salespersonlist)

sum1 = 0 
for i in salespersonlist:
    sum1 = sum1 + i
    i = i + 1
print(sum1)
totalsalesbysalesperson = sum1

products = [{'pd1':400, 'pd2':500, 'pd3':800, 'pd4':750, 'pd5':600},
            {'pd1':300, 'pd2':600, 'pd3':1000, 'pd4':850, 'pd5':700},
            {'pd1':500, 'pd2':700, 'pd3':400, 'pd4':650 , 'pd5': 850}, 
            {'pd1':1000, 'pd2':200, 'pd3':900, 'pd4':950, 'pd5':250}]
            

productlist = []

product1 = sum(item['pd1'] for item in products)
productlist.append(product1)
product2 =sum(item['pd2'] for item in products)
productlist.append(product2)
product3 = sum(item['pd3'] for item in products)
productlist.append(product3)
product4 = sum(item['pd4'] for item in products)
productlist.append(product4)
product5 = sum(item['pd5'] for item in products)
productlist.append(product5)
print(productlist)

sum2 = 0
for i in productlist:
    sum2 = sum2 + i
    i = i + 1
print(sum2)
salesbyproduct = sum