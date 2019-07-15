f1 = lambda z:z%2==0
def is_even(z):
    return z%2 == 0
    
numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]


print(list(filter(f1,numbers)))