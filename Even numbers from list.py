# https://www.w3resource.com/python-exercises/python-functions-exercise-10.php

# 17th Feb

# Python Exercise: Print the even numbers from a given list

## 1  ## my solution

def even_list():  ## without giving arguments
    X = []
    for i in L:
        if i%2 == 0:
            X.append(i)
    return X


L = [1,2,3,4,5,6,7,8,9,10]
print(even_list())  ## [2, 4, 6, 8, 10]

M = [12,13,44,54,67,89,31245,66,73,10]
print(even_list())  ## [2, 4, 6, 8, 10]     ## it wouldn't work!!!!!!!!!




## --------------------------------------------------------------------------------------------------------------


def even_list(L):  ## with  arguments
    X = []
    for i in L:
        if i%2 == 0:
            X.append(i)
    return X


L = [1,2,3,4,5,6,7,8,9,10]
print(even_list(L))  ## [2, 4, 6, 8, 10]

M = [12,13,44,54,67,89,31245,66,73,10]
print(even_list(M))  ## [12, 44, 54, 66, 10]

