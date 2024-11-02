class Remotecrontrol():
    def __init__(self):
        self.channels =  ['HBO','Max','Gemini','Star Maa']
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index >= len(self.channels):
            raise StopIteration
        
        return self.channels[self.index]
        
r = Remotecrontrol()
itr=r.__iter__()
print(itr.__next__())
print(itr.__next__())


# or when we are dealing with iterators you can also write the code like this
# r = RemoteControl()
# itr=iter(r)
# print(next(itr))


class LimitExceeded(Exception):
    pass


class Fibanochi():
    def __init__(self):
        self.series = [0,1]
        self.limit = 10
        return self

    def __iter__(self):
        return self
    
    def __next__(self):
        l = self.series.__len__()
        if self.series[-1] > self.limit or self.series[ l- 1] + self.series[l-2] > self.limit :
          raise LimitExceeded
         
        self.series.append(self.series[ l- 1] + self.series[l-2])

        return self.series[l - 1] + self.series[l -2]

class Fibonacci:
    def __init__(self, limit):
        # default constructor
        self.previous = 0
        self.current = 1
        self.n = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.limit:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.n += 1
            return result
        else:
            raise StopIteration


# init the fib_iterator
fib_iterator = iter(Fibonacci(5))
while True:
    # print the value of next fibonacci up to 5th fibonacci
    try:
        print(next(fib_iterator))
    except StopIteration:
        break