# Define a function named 'test' that takes a parameter 'a'
def test(a):
    # Define a nested function 'add' that takes a parameter 'b'
    def add(b):
        # Declare 'a' from the outer scope as nonlocal to modify its value
        nonlocal a
        
        # Increment the value of 'a' by 1
        a += 1
        
        # Return the sum of 'a' (modified by the nonlocal statement) and 'b'
        return a + b
    
    # Return the inner function 'add' and its scope is retained due to closure
    return add

# Call the 'test' function with an argument '4' and assign the returned function to 'func'
func = test(4)

# Call the function 'func' with argument '4' and print the result
print(func(4)) 
