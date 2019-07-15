numbers = range(1,50)
print ("'y' is odd numbers and 'x' is even numbers")

x = [n for n in numbers if n%2 != 0]
y = [n for n in numbers if n%2 == 0]
print("y =", y)
print("x =", x)

