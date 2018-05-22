from Functions import add_two_nums
from Functions import multipy_two_nums
from Functions import Circle
from Functions import Triangle

print('The result of adding 10 + 25 using the imported function: ', add_two_nums(10, 25))
print('The result of multiplying 12 * 12 using the imported function: ', multipy_two_nums(12, 12))

newCircle = Circle(3)

print('The area of my newCircle Object is: ', newCircle.area())

newTriangle = Triangle(3, 5)

print('The area of my newTriangle object is: ',newTriangle.area())

