#This is where the simple calculator will be built and run


#Useful code:

    #Get input and turn into int then output as string
        # print("What is the first number?: ")
        # x = int(input())
        # print("What is the second number?: ")
        # y = int(input())
        # z = x+y
        # print("The sum is: " + str(z))

    #Continue till broken
        # while True:
        #     user_input = input("HUH?: ")
        #     if user_input == "1":
        #         break




#How I want it to work:
    # User inputs the sign then the amount of number until 'q'

import time as tm
import math as mt

def goodbye():
    print("Goodbye and Come Again!")

def exit_msg():
    print("To exit the operation enter = \n")

def error_msg():
    print("\nNot a valid input please try again! \n")
    tm.sleep(2)

def mult():
    tm.sleep(1)
    res = 1
    exit_msg()
    while True:
        M_user_i = input("Enter a value: ")
        if M_user_i == "=" :
            break
        try:
            res *= int(M_user_i)
        except:
            error_msg()

    print("The Output is: " + str(res) + '\n')                 
    # return res

def add():
    tm.sleep(1)
    res = 0
    exit_msg()
    while True:
        M_user_i = input("Enter a value: ")
        if M_user_i == "=" :
            break
        try:
            res += int(M_user_i)
        except:
            error_msg()

    print("The Output is: " + str(res) + '\n')  

def sub():
    tm.sleep(1)
    num = 0
    while True:
        Snum = input("Enter the number you wish to subtract from: ")
        try:
            num = int(Snum)
            break
        except:
            error_msg()    
            tm.sleep(1)

    res = num
    exit_msg()
    while True:
        M_user_i = input("Enter a value: ")
        if M_user_i == "=" :
            break
        try:
            res -= int(M_user_i)
        except:
            error_msg()

    print("The Output is: " + str(res) + '\n')  

def div():
    tm.sleep(1)
    num = 0
    while True:
        Snum = input("Enter the number you wish to divide from: ")
        try:
            num = int(Snum)
            break
        except:
            error_msg()    
            tm.sleep(1)

    res = num
    exit_msg()
    while True:
        M_user_i = input("Enter a value: ")
        if M_user_i == "=" :
            break
        try:
            mod = int(M_user_i)
            if mod == 0:
                error_msg()
                continue
            else:
                res /= int(M_user_i)
        except:
            error_msg()

    print("The Output is: " + str(res) + '\n')  

def expo():
    tm.sleep(1)
    base = 0
    power = 0
    while True:
        sBase = input("Enter the number you wish to raise : ")
        sPower = input("Enter the power: ")
        try:
            base = int(sBase)
            power = int(sPower)
            break
        except:
            error_msg()    
            tm.sleep(1)

    num = mt.pow(base,power)

    print("The output is: " + str(num)+ "\n")

def root():
    tm.sleep(1)
    base = 0
    power = 0
    while True:
        sBase = input("Enter the number you wish to root : ")
        sPower = input("Enter the power: ")
        try:
            base = int(sBase)
            power = int(sPower)
            if power == 0:
                print("The result is not possible try again \n")
                tm.sleep(1)
                continue
            break
        except:
            error_msg()    
            tm.sleep(1)

    power = 1.00/power

    num = mt.pow(base,power)

    print("The output is: " + str(num) + "\n")            



    


while True:
    user_choice = input(
        '''Main menu \n ----------------------- \nChoose one of the following options \n --------------------- \n +) Addition \n -) Subtraction \n /) Division \n *) Multiplication \n ^) Exponential \n //) Root \n q = Quit \n---------------------------------- \n : ''')
    match user_choice:
        case 'q':
            goodbye()
            break
        case '*':
            mult()
        case '/':
            div()
        case '+':
            add()
        case '-':
            sub()
        case '^':
            expo()
        case "//":
            root()    

        case _: # This is the defualt so if its not one of the 5 options
            error_msg()            


    # if user_choice not in ['+','-','/','*','q']:
    #     error_msg()
    # if user_choice == 'q':
    #     goodbye()
    #     break

    # if user_choice == '*':
    #     mult()