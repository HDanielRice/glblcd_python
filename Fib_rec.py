def fib_rec(f):
    #if f == 0:
        #return f
    
    if f == 1:
        return f

    else:
        return fib_rec(f-1) + fib_rec(f-2)
    
print(list(map(fib_rec, range(1,11))))