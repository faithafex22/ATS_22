# Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
# Create  a method called testPrims() allowing to test if two numbers are prime between them.
# Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer

class Computation:
    def __init__(self):
        pass

    def factorial(self, num:int):
        try:
            int(num)
        except ValueError:
           print("number must be an integer")
        factorial = 1
        for i in range (1, num + 1):
            factorial = factorial*i
        return factorial

    def add_nthterm(self, term:int):
        try:
            int(term)
        except ValueError:
            print("number must be an integer")
        addition = 0
        for i in range(1, term+1):
            addition = addition + i
        return addition 

    def check_prime(self, number):
        try:
            int(number)
        except ValueError:
            print("number must be an integer")
        for i in range(2, number):
                if number%i == 0:
                    return("This is not a prime number")
        else:
            return("This is a prime number")

    def tableMult(self, digit):
        try:
            int(digit)
        except ValueError:
            print("number must be an integer")   
        for i in range(1, 13):
            print(i, "*", digit, "=", i * digit)
    
    def multitable(self):
        for i in range (1, 10):
            for j in range(1, 13):
                print(i, "*", j, "=",  i * j)

    @staticmethod
    def listdiv(num):
        try:
            int(num)
        except ValueError:
            print("number must be an integer")
        divlist = []
        for i in range(1, num+1):
            if num % i == 0:
                divlist.append(i)
        return divlist
    
   # @staticmethod
    def listdivprime(self, no):
        try:
            int(no)
        except ValueError:
            print("number must be an integer")
        newlist = []
        factors = Computation.listdiv(no)
        print(factors)
        for j in factors:
            if j > 1:
                for i in range(2, j):
                 if j%i == 0:
                    break
                else:
                    newlist.append(j)
        return newlist

            
                
             
integer1 = Computation()
print(integer1.listdivprime(30))