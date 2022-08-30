#from random import randint
#num = randint(1, 99)
#print(num)
Primes = [0] * 500001
def SieveOfEratosthenes(n) :
    Primes[0] = 1
    i = 3
    while(i*i <= n) :
        if (Primes[i // 2] == 0) :
            for j in range(3 * i, n+1, 2 * i) :
                Primes[j // 2] = 1
                 
        i += 2
         
# Driver Code
if __name__ == "__main__":
 
    n = 1000
    SieveOfEratosthenes(n)
    for i in range(1, n+1) :
        if (i == 2) :
            print( i, end = " ")
        elif (i % 2 == 1 and Primes[i // 2] == 0) :
            print( i, end = " ")