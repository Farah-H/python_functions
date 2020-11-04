# Functions in Python

### What are functions and why are they useful?
__DRY__: Don't Repeat Yourself
Functions help avoid repetition of commonly used blocks of code. `print()` is an example of a function. 

Functions help structure your code to make it more readable and more efficient.

### How to Create a Function:
Syntax: 
```python
def name_of_function(arguments_the_function_takes, there_can_be_multiple): # note the colon!!
    # note indentation, very important
    do_something
    return outcome # return is not necessary but it's nice
```

Functions do not run unless you *call them* using the following syntax or by calling it indirectly using another function:
```python
# calling the function directly
name_of_function()

# calling the function indirectly
increment = True
while increment: 
    greeting()
    increment = False # this would run the function once
```
### Return VS Print
``print`` displays the output, ``return`` actually makes the function equal to the output, so we can use it later if we want to. For example:
```python
def multiply(a,b):
    return a * b 
## in this case multiply(a,b) = a * b 

def multiply_print(a,b):
    print(a * b)
## multiple(a,b) = print(a*b) 
```
i think it's an important distinction because you can do more stuff with the former than the latter for example I can do 
```python
print(8 * multiply(2,3))
```
but that wouldn't work for ``multiply_print`` because multiple_print is not a number, it's a print statement.

## Function Best Practices:
__KIS__: Keep It Simple! 
- Ideally, a function will do one and only one job. It should be a small block. 
- pseudo coding, one line of explanation.
- HINTs: create hints in simple bullet points or pointers
- comments regarding your functoin results

### Local vs Global Variables
- if you declare a variable *inside* a function, the rest of your program 'doesn't know about it' so it does not need to be unique to that function for example

```python
def function_a(num1):
    print(num1)

def function_b(num1)
    print(num1, num1)
```
this is absolutely fine to do because in this case num1 is not a variable, it is an argument, so a *placeholder* for a variable that you will define when you call the function. However, it is good practice to make your placeholders descriptive if that is necesasry to avoid confusion. For example in the case above, both functions are taking in two numbers, so `num1`and `num2`are fine, but if one of the functions was taking in a string and capitalising it, the following could be a better argument: 

```python
def capitalize(string_input):
    return string_input.upper()

def add(num1, num2):
    return num1 + num2
```

__In this case the choice of argument helps make the code more readable and explains what kind of input is allowed.__ If the user tries to put in an integer, it would cause an error (integers cannot be capitalised), when they look at the code, `string_input` would immediately let them know where they went wrong. 

## Tasks 
1. Create functions for adding, multiplying, subtracting and finding the modulus of two numbers. What is the difference between ``print()`` and ``return``? 