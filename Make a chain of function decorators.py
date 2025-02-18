#### 18th Feb

## https://www.w3resource.com/python-exercises/python-functions-exercise-17.php

# Define a decorator 'make_bold' that adds bold HTML tags to the wrapped function's return value
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

# Define a decorator 'make_italic' that adds italic HTML tags to the wrapped function's return value
def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

# Define a decorator 'make_underline' that adds underline HTML tags to the wrapped function's return value
def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

# Apply multiple decorators (@make_bold, @make_italic, @make_underline) to the 'hello' function
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"

# Print the result of the decorated 'hello' function, which adds HTML tags for bold, italic, and underline

print(hello()) ## returns "<b><i><u>hello world</u></i></b>"
