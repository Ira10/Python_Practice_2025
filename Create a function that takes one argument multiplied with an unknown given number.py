#### 18th Feb

## https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-2.php

# Define a function 'func_compute' that takes a parameter 'n' and returns a lambda function
# The returned lambda function multiplies its argument 'x' by 'n'
def func_compute(n):
    return lambda x: x * n

# Assign the result of calling func_compute with argument 2 to the variable 'result'
result = func_compute(2)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Double the number of 15 =", result(15))

# Reassign 'result' with the result of calling func_compute with argument 3
result = func_compute(3)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Triple the number of 15 =", result(15))

# Reassign 'result' with the result of calling func_compute with argument 4
result = func_compute(4)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Quadruple the number of 15 =", result(15))

# Reassign 'result' with the result of calling func_compute with argument 5
result = func_compute(5)
# Print the result of calling the lambda function stored in 'result' with argument 15
print("Quintuple the number 15 =", result(15))
