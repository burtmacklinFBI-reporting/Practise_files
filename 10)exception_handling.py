x = input("Enter a number") 
y = input("Enter another number") 
try: 

 z= int(x)/int(y) 

except Exception as e: 

 print('This is the exception name',type(e).__name__) 

 z= None 

 print('Division is ',z) 


# now this will help you understand what is the error that you would be getting and after knowing this you can simply write what the error is 

x = input("Enter a number") 

y = input("Enter another number") 

try: 

 z= int(x)/int(y) 

except ZeroDivisionError as e: 

 print('This is the zero exception') 

 z= None 

 print('Division is ',z) 