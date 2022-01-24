# Find square root of real or complex numbers

# Importing the complex math module

import cmath

num1 = 11+2.5j

# To take input from the user
num2 = eval(input('Enter a number: '))

num1_sqrt = cmath.sqrt(num1)
num2_sqrt = cmath.sqrt(num2)

print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num1 ,num1_sqrt.real,num1_sqrt.imag))
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num2 ,num2_sqrt.real,num2_sqrt.imag))


