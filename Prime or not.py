#### 4th Dec

## https://www.w3resource.com/python-exercises/python-functions-exercise-9.php

# Define a function named 'test_prime' that checks if a number 'n' is a prime number
def test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True

print(test_prime(9))
