print'*Welcome to calculator*'
print'Press 1 for addition'
print'Press 2 for subtraction'
print'Press 3 for multiplication'
print'Press 4 for division'
print'\n'
a=input('select your choice:')
print'\n'
x=input('Enter first number:')
y=input('Enter second number:')
if a==1:
    print'\nYou have opted for addition. '
    z=x+y
    print'Addition is',z
if a==2:
    print'\nYou have opted for subtraction.'
    z=x-y
    print'Subtraction is',z
if a==3:
    print'\nYou have opted for multiplication.'
    z=x*y
    print'Multiplication is',z
if a==4:
    print'\nYou have opted for division.'
    z=x/y
    r=x%y
    print'Division is',z
    print'Remainder is',r
else:
    print'\nError in choice selection'
    print'Please select correct choice'
    
