########   11th Dec 

##### https://www.w3resource.com/python-exercises/python-functions-exercise-15.php

str_ = 'green-red-black-white'

items = str_.split('-')

print(items)   # ['green', 'red', 'black', 'white']

print(' '.join(items))  # green red black white

print('-'.join(sorted(items)))  ### black-green-red-white