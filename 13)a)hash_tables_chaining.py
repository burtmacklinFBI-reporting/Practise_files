class Hashtable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)] # this is an implementation of list comprehension method, and this will have 100 none in the list


    def get_hash(self,text):
        h = 0
        for char in text:
            h += ord(char) # ord function returns the ascii values of a character
        return h % 100

    # def add_item_hash(self,key,value):
    #     index = self.get_hash(key)
    #     self.arr[index] = value

    # def get_item_hash(self,key):
    #     index = self.get_hash(key)
    #     return self.arr[index]

# now if you want to retreive the value from the above two methods then you write like this 
# t.add_item_hash('march 6',130)
# print(t.get_item_hash('march 6'))

# and wouldnt it be better if we can write like dictionary itself like. So for we have operators which are premade like __setitem__ and __getitem__
# t['march 6'] = 130
# print(t['march 6'])


    def __setitem__(self,key,value):
            index = self.get_hash(key)
            found = False
            for ind,i  in enumerate(self.arr[index]):
             if len(i) == 2 and i[0] == key :
              self.arr[index][ind] = (key, value)
              found = True
            if not found:
              self.arr[index].append((key,value))
              
             


    def __getitem__(self,key):
        index = self.get_hash(key)
        for ind, i in enumerate(self.arr[index]):
            if i[0] == key:
             return self.arr[index][ind][1]
    
    def __delitem__(self,key):
         index = self.get_hash(key)
         for ind, i in enumerate(self.arr[index]):
             if i[0] == key:
              del self.arr[index][ind]
         

t = Hashtable()
t['march 6']= 30
t['march 6']= 45
t['march 8']= 454
t['aug 16']= 2345
t['march 17']= 98
del t['march 17']
print(t['march 8'])




