class Hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)] # this is an implementation of list comprehension method, and this will have 100 none in the list

    # def __repr__(self):
    #     return f"Hashble({self.arr})"
    
    def __str__(self):
        return str(self.arr)
    # The above two functions are necessary to read the list itself cause python does not know how to print the data at its end so it needs clarity to check wher is what.
    

    def get_hash(self,text):
        h = 0
        for char in text:
            h += ord(char) # ord function returns the ascii values of a character
        return h % self.max 

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
            if self.arr[index] == []:
               self.arr[index]= [key,value]

            elif self.arr[index] != []:
               for i in range(len(self.arr)):
                  index = index + 1
                  if index > (len(self.arr) - 1):
                     index = 0
                  else:
                     index

                  if self.arr[index] == []:
                     self.arr[index]= [key,value]
                     found = True
                     break
                  
            if not found:
                    raise Exception("Hash table is full")
                  
    def __getitem__(self,key):
        for i in self.arr:
            if len(i) == 2:
             if i[0] == key:
              return i
    
    def __delitem__(self,key):
         for i in self.arr:
            if len(i) == 2:
             if i[0] == key:
               self.arr.remove(i)
         

t = Hashtable()
t['march 6']= 30
t['march 6']= 45
t['march 8']= 454
t['aug 16']= 2345
t['march 17']= 98
del t['march 17']
print(t)




