def add(a,b):
    c = a+ b
    return c;

print(add(10,5))

def minus(a,b):
    c = a-b
    return c;

print(minus(10,5))

def multiply(a,b):
    c = a * b
    return c;

print(multiply(10,5))

def divide(a,b):
    c = a/b
    return c;

print(divide(10,5))

def greeting(name):
    greet = f"welcome here {name}"
    return greet;

print(greeting("Faith"))

def operations(a,b):
    output = add(a,b), minus(a,b), multiply(a,b), divide(a,b)
    return output;

print(operations(10,5))


