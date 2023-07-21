def add (n1, n2) :
    return n1 + n2

def subtract (n1, n2) :
    return n1 - n2

def multiply (n1, n2) :
    return n1 * n2

def divide (n1, n2) :
    return n1 / n2

operations = {
    '+' : add, 
    '-' : subtract, 
    '*' : multiply, 
    '/' : divide
}

def calculator () :
    num1 = int (input ("enter first number : "))
    for key in operations :
        print (key)

    operation_key = input ("Enter the operation you want to perform : ")
    num2 = int (input ("enter second number : "))

    result1 = operations[operation_key](num1, num2)

    print(f"{num1} {operation_key} {num2} = {result1}")

    if (input("wanna continue? (y/n) : ") == 'y') :
        opt = True
    else :
        opt = False
        calculator()
    res = result1
    while opt :
        operation_key = input ("Enter the operation you want to perform : ")
        num3 = int (input ("enter your next number : "))

        result2 = operations[operation_key](res, num3)

        print(f"{res} {operation_key} {num3} = {result2}")
        res = result2

        if (input ("wanna continue? (y/n) : ") != 'y') :
            opt = False
            calculator()

calculator()