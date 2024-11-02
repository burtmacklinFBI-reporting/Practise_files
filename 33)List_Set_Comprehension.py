#list comprehension is a way to convert one list from another list

numbers = [1,2,3,4,5,6]
even = []
for i in numbers:
    if i%2 ==0:
        even.append(i)

# this is a long way of writing it

even = [ i for i in numbers if i%2 == 0]

#this is a short way of writing it


# set is unordered and it only has unique values. So for set comprehension method we replace the old square brackets with {}
#set(numbers) provides a unique set

even2 =  {i for i in set(numbers) if i%2 ==0}


#dictionary comprehension

cities = ['mumbai','new york','paris']
countries = ['india','usa','france']
z = zip(cities, countries) #this zips or in some case we can say as join where the first parameter becomes the key and the second parameter becomes the value and the key,value will be in a tuple format
d = { city:country for city,country in zip(cities,countries)} 
#this is called as dictionary comprehension


integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
z = zip(integer,binary)
print({i:j for i,j in z })

integer_list = [1,2,3,4,5,6]
print([ i*(-1) for i in integer_list])

integer = [1, -1, 2, -2, 3, -3]
print(set([i*i for i in integer]))