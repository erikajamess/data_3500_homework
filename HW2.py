#2.3 
grade = int(input('What is your current grade?'))
if grade >= 90: 
   print('Congrats! You passed the course!') 
else: 
    print('You tried your best!')


#2.4 
a = 27.5
b = 2
addition = a + b
print(addition)
subtraction = a - b
print(subtraction)
multiplication = a * b
print(multiplication)
division = a/b
print(division)
floor_division = a//b
print(floor_division)
exponent = a**b
print(exponent)


#2.5
pi = 3.14159
r = 2
diameter = r * 2
print(diameter)
circumference = 2 * pi * r
print(circumference)
area = pi * r**2
print(area)


#2.6
number = int(input('Please enter a number:'))
a = number % 2
if a == 0: 
    print('even')
else:
    print('odd')

#2.7
a = 1024
b = 10 
if a % 4 == 0 and b % 2 == 0:
    ##print('nice.')

#2.8
print('Number\tSquare\tCube"')
for i in range(6):
    print(i, '\t', i**2, '\t', i**3)