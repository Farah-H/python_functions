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
    return num1 - num2

subtract(234,100)

# create  a function to  multiply
def multiply(a,b):
    return a * b	

# create a function to devide
def devide(a,b):
    return a / b 

# create a function to % 
def modulus(a,b):
    return a % b

print(modulus(4,2))

# storing the outcome of the return statement into a variable 
subtracted_value = subtract(2,3)
print(subtracted_value)
