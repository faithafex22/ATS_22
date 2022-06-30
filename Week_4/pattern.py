height = int(input("Enter the height of the triangle : "))
c = str(input("Enter the character you want to print the triangle : "))
for i in range(1,height+1):
  for j in range(1,i+1):
    print(c+" ", end='')
  print()

height = int(input("Enter the height of the triangle : "))
c = str(input("Enter the character you want to print the triangle : "))
for i in range(0,height):
  for j in range(0,height - i):
    print(c+" ", end='')
  print()

height = int(input("Enter the height of the triangle  : ")) 
for i in range(1, height + 1):
    for j in range(1, height + 1):
        if(j <= height - i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()

height = int(input("Enter the height of the triangle  : "))
for i in range(1, height + 1):
    for j in range(1, height + 1):
        if(j < i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()