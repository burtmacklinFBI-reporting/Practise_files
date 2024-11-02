def fib():
    a,b = 0,1
    while True:
        yield a # yield is like a return statement once it is done it just comes out from the loop.
        a,b = b,a+b

for f in fib():
    if f > 100:
        break
    print(f)



def sqr():
    a = 0
    while True:
        yield a
        a= a+1

for a in sqr():
    if a > 10:
        break
    print(a**2)


