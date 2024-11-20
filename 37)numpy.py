import numpy as np

a1 = np.array([1,2,4])
a2 = np.array([2,3,4])
print(a1 + a2) # this is one of the utilies of the arrays. This can be used for all mathemetical functions and is much easier to use when compared to the lists.


print(f'THis is jsut me testing the range{np.arange(1,10,2)}') # this is just like the range function with the lists that we use . Just like range we can also have a start point to start and an end point till which it will come but it will not be included and also it does have a step count.
print(a1[0:2]) # this is how you can do the slicing for arrays, negative indexing also works the same way

#there are n dimensional arrays. the last number of consecutive brackets should give you an idea on the dimension of ths array.

a = np.array([[1,2],[3,4],[5,6]])
print(a.ndim) # returns the dimension of the array without you stressing over to count the brackets

#itemsize property will print us the size of each property. Suppose if the given data type is an integer the size that you will be getting will be 4, and suppose if they do contain float values then the itemsize is going to be 8.

print(a.itemsize)
print(a.dtype) # this will help us to know what type of data we are dealing with

# you can change the datatype when initializing.
a = np.array([[1,2],[3,4],[5,6]],dtype = np.int32)
print(a.itemsize)
print(a.dtype) 


#size gives you the size that is the number of elements in the array
print(a.size)

#shape gives you the dimension of the array that is like the rows and columns of the array, considering it like a matrix. Like if it has seperated after each comma into another row. So this one has 3 rows and 2 columns.
print(a.shape)

#suppose you want to intialize your array with placeholder numbers then you can follow these methods.like with zereos or ones and in what shape do you want them. Like whether you want the shape to be (3,2)

print(np.zeros((3,2)))
print(np.ones((3,2)))

#linspace(start,stop,partitions) linspace breaks the numbers between the start and the stop into each partitions, last number included
print(np.linspace(1,10,11))

#you can also respace your array if it following the rules of matrix size like rows*columns should be the same.
a.reshape(2,3)
a.reshape(2,6)

#ravel() ravel for any array makes it flat like 1*1 size
a.ravel()

print(a)
#now you will observe that you can done so many changes nothing happened to the original array. Now this is something that you need to understand that nothing will happen to the original array and changes will happen only if you store it another place.


a.min() # will return the minimum element in the array
a.max() #will return the maximum element in the array
a.sum() #will return the sum of all the elements in the array

a.sum(axis=0) #adds vertically
a.sum(axis =1 ) #adds horizontally

np.sqrt(a) #returns the squareroot of each elements.


# Slicing through multiple dimension arrays, which means that there are rows and columns adn what happens if slicing also is involved in them. 

a6 = np.array([[6,7,8],[1,2,4],[9,3,2]])
print(a6[1,2]) # here the first parameter stand for the row and the second parameter stands for the column. Rows and columns start with 0 index just like usual.

#what is I introduce slicing also in this

print(a6[0:2,2]) #this means you will be getting two values. First one being 0 row and 2 column, and also 1 row and 2 column. You will not the second row because it stops at index 1.

print(a6[:,2]) # this helps us go through all the rows at once


# iterating through arrays

for a in a6:
    print(a)

#also you can flattent the array and loop through each and every cell so that you can check that.

for a in a6.flat:
    print(a)

# also there are better ways to loop through the array. You can use the nditer() function. Check the web document to know its full functionalities.There if F order, C order and also order.

for a in np.nditer(a6,order = 'F'):
    print(a)

# you can also navigate through two arrays at once using nditer function.


#stacking together two arrays horizontally and vertically. remember that the argument inside it is a tuple. Either the shape should be same or they should have the same broadcasting rules.

np.vstack((a1,a2))
np.hstack((a1,a2))

#splitting the big array into small pieces

a4 = np.arange(30).reshape(2,15)
print(a4)


#splitting the big list into smaller parts.
np.hsplit(a4,3) #this is split the array into 3 smaller parts horizontally
np.vsplit(a4,2) #this will make in two parts vertically


# you can also create an array using boolean values

b = a4 > 4 #now when you try to print b the result would be an array with the same dimensions and also it would compare each element and then it would check with condition and return true or false.

a4[b] # this will return all the elements with true condition in b


