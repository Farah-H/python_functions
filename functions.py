# let's create a function

#takes user's name
name = input('Please enter your name.').title()

def greeting(name):
    print(f'Welcome on board, {name}!')

# to run a function you need to call it
greeting(name)

# creating an add function that takes two arguments and adds them 
def add(num1, num2):
    print(num1 + num2)

# calling add 
add(4587,38724)

#creating a function that would subtract the two values
def subtract(num1,num2):
    print(num1 - num2)

subtract(234,100)