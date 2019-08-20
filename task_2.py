import math
from decimal import *
#task_1
number_1 = int(input("Please enter first number: "))
number_2 = int(input("Please enter second number: "))
print("Sum is {0}".format(number_1+ number_2))
print("Product is {0}".format(number_1 * number_2))

#task_2
number = int(input("Please enter a number: "))
print("Square is {0}".format(number**2))
print("Cube is {0}".format(number**3))

#task_3
number_1 = int(input("Please enter first number: "))
number_2 = int(input("Please enter second number: "))
number_3 = int(input("Please enter third number: "))
print("Total sum is {0}".format(number_1*2 + number_2-3 + number_3**2))

#task_4
number_1 = Decimal(input("Please enter first number: "))
number_2 = Decimal(input("Please enter second number: "))
number_3 = Decimal(input("Please enter third number: "))
getcontext().prec = 2  # Мне нравится.
print("Average is {0}".format(Decimal(number_3+number_2+number_1)/Decimal(3.00)))
print("Difference is {0}".format((number_3+number_1)*2-number_2*3))
# Но можно и "Average is {0:10.2f}".format(...)
# Или '%10.2f' % ...


#task_5
side_length = int(input("Please enter square side length: "))
print("Perimeter is {0}".format(side_length*4))
print("Area is {0}".format(side_length**2))

#task_6
cookie_price = int(input("Please enter cookie price: "))
candy_price = int(input("Please enter candy price: "))
print("First purchase is {0}".format(0.3*candy_price + 0.4*cookie_price))
print("Second purchase is {0}".format((1.8*candy_price + 2*cookie_price)*3))

#task_7
time = int(input("Please enter minutes: "))
km = int(input("Please enter kilometers: "))
print("Speed is {0} m per s".format(km*1000/time*60))

#task_8
side_1 = int(input("Please enter the triangle side 1: "))
side_2 = int(input("Please enter the triangle side 2: "))
hypotenuse = math.sqrt(side_2**2+side_1**2) # Корень можно считать без math 
                                            # result ** 0.5

print("Area is {0}".format(side_1*side_2/2))
print("Hypotenuse is {0}".format(hypotenuse))
print("Perimeter is {0}".format(side_1+side_2+hypotenuse))

#task_9
temperature = float(input("Please enter the temperature in Celsius: "))
print("Temperature in Fahrenheit is {0}".format((temperature * 9/5) + 32))
# Тут надо округлить, или отформатировать float.
