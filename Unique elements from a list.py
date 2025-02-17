#### 17th Feb

## https://www.w3resource.com/python-exercises/python-functions-exercise-8.php

### Write a Python function that takes a list and returns a new list with distinct elements from the first list.


## 1 ## my solution

def unique_list(L):
    L_new = []
    for i in L:
        if i not in L_new:
            L_new.append(i)
            # L = L[1:]    # this step is not needed
    return L_new



L = [3,8,12,21,3,2,1,0,3]
print(unique_list(L))  ## [3, 8, 12, 21, 2, 1, 0]


M = ['dude', 'Indrani', 'Oh honey', 33,33,44,44,2,2]
print(unique_list(M))   # ['dude', 'Indrani', 'Oh honey', 33, 44, 2]
