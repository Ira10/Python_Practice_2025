#### 12th Dec

### https://www.w3resource.com/python-exercises/python-functions-exercise-16.php

start_range = int(input("start range plox "))
end_range = int(input("end range plox "))

def square_range(start_range, end_range):
    return [i**i for i in range(start_range, end_range+1)]


print(square_range(start_range, end_range))
 
# 5×5, which equals 25. 
# 5×5×5×5×5, which equals 3125.