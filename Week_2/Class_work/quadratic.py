def quadratic(a,b,c):
    import cmath

    d = (b**2)-(4*a*c)
    value1 = (-b-cmath.sqrt(d))/(2*a)
    value2= (-b+cmath.sqrt(d))/(2*a)

    print(f"x = {value1},{value2}")

quadratic(1,2,1)

def solve_quadratic_equation(a:int, b:int, c:int):
    product = a * c
    factors = []
    if product < 0:
        for i in range(product, -(product - 1)):
            if i == 0:
                continue
            elif product % i == 0 and i != 0:
                factors.append(i)
    elif product > 0:
        for i in range(-(product), product + 1):
            if i == 0:
                continue
            elif product % i == 0 and i != 0:
                factors.append(i)
    else:
        print(f"This equation is not a quadratic equation.")
    working_factors = []
    for i in factors:
        for j in range(len(factors)):
            if i + factors[j] == b and i * factors[j] == product:
                working_factors.append(i)
    if a == 1 and len(working_factors) == 1:
        print(f"x = {-(working_factors[0])} two times")
    elif a == 1 and len(working_factors) == 2:
        print(f"x = {-(working_factors[0])} and {-(working_factors[1])}")
    elif a > 1 and len(working_factors) == 2:
        print(f"x = {-(working_factors[0])/a} and {-(working_factors[1])/a}")
    elif a < 0 and len(working_factors) == 1:
        print(f"x = {-(working_factors[0])/a} two times")
    elif a < 0 and len(working_factors) == 2:
        print(f"x = {-(working_factors[0])/a} and {-(working_factors[1])/a}")


