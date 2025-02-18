#### 12th Dec
## https://www.w3resource.com/python-exercises/python-functions-exercise-18.php

# Define a string variable 'mycode' containing a Python code as a string
mycode = 'print("hello world")'

# Define a multi-line string variable 'code' containing Python code as a string
code = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
"""

# Execute the Python code represented by the string stored in the variable 'mycode'
exec(mycode)

# Execute the Python code represented by the multi-line string stored in the variable 'code'
exec(code) 
