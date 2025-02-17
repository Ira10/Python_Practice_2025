#### 4th Dec

## https://www.w3resource.com/python-exercises/python-functions-exercise-7.php

def calcul_letter():
    str_ = input("Enter the string ")
    lower = 0
    upper = 0
    for i in str_:
        if str.isupper(i):
            upper += 1
        elif str.islower(i):
            lower += 1
        else:
            pass 
    return upper, lower

print("The upper and lower is ", calcul_letter())

print(calcul_letter())

# Enter the string Indrani SArk#%
# (3, 8)

# Enter the string Urs&&lA
# The upper and lower is  (2, 3)

