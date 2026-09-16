import math

def add_Two():
    num1 = input("First Number?: ")
    num2 = input("Second Number?: ")
    
    return int(num1)+int(num2)

# print(add_Two())

def find_Mod(z):
    num = int(input("Num to divide by: "))
    mod = num % z
    
    return mod

# print(find_Mod(3))

def find_Type():
    data = input("Whats the data?: ")
    res = "something"
    try:
        int(data)
        res = "class <int>"
    except:
        try:
            float(data)
            res = "class <float>"
        except:        
            res = "class <string>"
    
    return res

# print(find_Type())        

def find_Max():
    a = float(input("First Value? : "))
    b = float(input("Second Value? : "))
    
    res = ""
    
    if a > b:
        res = "a is larger than b"
    else:
        res = "a is smaller than b"
        
    return res        
    
# print(find_Max())    

def find_Average():
    a = float(input("First Value? : "))
    b = float(input("Second Value? : "))
    
    avg = (a+b)/2
    
    return avg

# print(find_Average())

def find_square(num):
    res = num ** 2
    
    return res

# print(find_square(float(input("?:"))))

