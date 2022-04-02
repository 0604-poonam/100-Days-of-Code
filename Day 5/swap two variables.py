# Python program to swap two variables

#using temp variable

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

x = 20
y = 10

# create a temporary variable and swap the values
temp = x
x = y
y = temp


print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

