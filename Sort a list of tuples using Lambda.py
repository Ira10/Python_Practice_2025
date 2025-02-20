### 19th Feb

#### https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-3.php

# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# print(subject_marks[0][1])  ### 88


# Sort the 'subject_marks' list of tuples based on the second element of each tuple (the marks),
# using a lambda function as the sorting key to extract the second element
subject_marks.sort(key=lambda x: x[1])   ## they keys are the scores, now it sorts asceding

# Display the sorted list of tuples to the console
print("\nSorting the List of Tuples:")
print(subject_marks) 

a = [5,4,2,6,1]
print(a.sort())  ## None
print(a)        ## [1, 2, 4, 5, 6]

a = [5,4,2,6,1]
print(a)        # [5, 4, 2, 6, 1]
print(sorted(a))    # [1, 2, 4, 5, 6]

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)
