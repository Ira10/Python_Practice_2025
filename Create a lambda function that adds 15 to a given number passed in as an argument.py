#### 18th Feb 

# https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-1.php#google_vignette

def func(n):
    return (lambda n: n + 15)(n)
    # return lambda n: n + 15

print(func(2))          # 17
print(func(432))        # 447


# Define a lambda function 'r' that takes a single argument 'a' and returns 'a + 15'
r = lambda a: a + 15

# Print the result of calling the lambda function 'r' with argument 10
print(r(10))   ### 25

# Reassign 'r' to a new lambda function that takes two arguments 'x' and 'y' and returns their product
r = lambda x, y: x * y

# Print the result of calling the updated lambda function 'r' with arguments 12 and 4
print(r(12, 4))   # 48
