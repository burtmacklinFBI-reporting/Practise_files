#Q1) Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line

street = 'adarhsnagar'
city = 'visakhaptnam'
country = 'India'
tot_add = (street + ' ' + city + ' ' + country)
addrs = '{} {} {}'.format(street,city,country) # this is concatenation using the format method
addrs2 = f'{street}-{city}-{country}' # this is concatenation using the f-string method
print(tot_add)
print(addrs)
print(addrs2)
print(street,city,country,sep='\n')# this way you can use a seperator when you want anything between the variables which might reduce the effort.

#Q2) Create a variable to store the string "Earth revolves around the sun"

strng = 'Earth revolves around the sun'


#Q3) Print "revolves" using slice operator

strng = 'Earth revolves around the sun'
print(strng[6:15]) #two ways to use the slice operator 
print(strng[slice(6,15)])



#Q4) Print "sun" using negative index
strng = 'Earth revolves around the sun'
print(strng[-3:])

#Q5) Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

x = 10
y=4
print(f'I eat {x} veggies and {y} fruits daily')

#Q6) I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.ˀ

s='maine 200 banana khaye'
s=s.replace('banana','samosa')
s=s.replace('200','10')
print("Using two line replace:",s)

s='maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200','10')
print("Using single line:",s)