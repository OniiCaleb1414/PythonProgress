# l1 = [1,8,7,2,21,15]
# print(l1)


# l1.insert(2,5)
# print(l1)



def store_Fruits():
    l1 = []
    done = False
    while not done:
        fruit_var = input("fruit: ")
        if fruit_var == "q":
            done = True
        else:    
            l1.append(fruit_var)    
    return l1

# print(store_Fruits())    

def store_Marks():
    l1 = []
    done = False
    while not done:
        mark_var = input("Mark: ")
        if mark_var == "q":
            done = True
        else:    
            num = float(mark_var)
            l1.append(num)    
    l1.sort()
    return l1

# print(store_Marks())

def check_Tuple(tpl):
    try:
        tpl.append("2")
    except:
        print("Its not possible.")

# check_Tuple(("1","8","3","4"))

def Sum_list(ls):
    sum = 0.0;
    for i in range(3):
        sum += ls[i]
    return sum    

print(Sum_list([2,3,2,4]))