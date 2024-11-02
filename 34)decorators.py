import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ + 'took' + str((end - start)*1000) + 'mil sec')
        return result
    return wrapper





@time_it
def calc_sqr(numbers):
    result = [ number*number for number in numbers ]
    return result


def dec_fact(func):
    def wrapper(*args,**kwargs):
        if args[0] <=0:
            raise ValueError('Number should be greater than 0')
        result = func(*args,**kwargs)
        return result
    return wrapper
       


@dec_fact
def factorial(num):
    if num <=1:
        return 1
    return num * factorial(num - 1)


print(factorial(-1))
    