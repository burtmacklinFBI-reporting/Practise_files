class employee:
    def __init__(self,i,n):
        self.id = i
        self.name = n

    def display(self):
      print(f'The emp id is {self.id} and their name is {self.name}')

emp = employee(1,'rahul') 
emp.display()

del emp.id
try:
   print(emp.id)
except NameError:
   print("emp.id not defined")
   
del emp
try:
   print(emp)
except NameError:
   print("emp.id not defined")