copu = {'China':143,'India':136,'USA':32,'Pakistan':21}
copu = {key.lower(): value for key, value in copu.items()}
def user_input(option='query'):
   if option =='print':
       for i,j in copu.items():
           print(f'{i.lower()}==>{j}')
   elif option =='add':
       new_cn = input('Please add a new country').lower()
       if new_cn in copu:
           print('This country already exists')
       else :
           cn_pop = int(input('plese enter the population'))
           copu[new_cn]=cn_pop
           for i,j in copu.items():
            print(f'{i.lower()}==>{j}')
   elif option =='remove':
       rm_cn = input('Please tell the country name').lower()
       if rm_cn in copu:
           del copu[rm_cn]
           for i,j in copu.items():
            print(f'{i.lower()}==>{j}')
       else:
          print('country does not exist')
   elif option =='query':
      cn_query = input('Enter a country name') 
      if cn_query in copu:
       print(f'The {cn_query} copulation is {copu[cn_query]}')
      else:
         print('country not there in dictionary')
   else:
      print('Please enter proper country name in database') 

user_input()


stock_prices={'info':[600,630,620],'ril':[1430,1490,1567],'mtl':[234,180,160]}
def operation(value='print'):
 if value == 'print':
  for i in stock_prices:
    val = (stock_prices[i])
    sum1 = 0
    for j in range(len(val)):
        sum1 = sum1 + val[j]
    avg1 = sum1/(len(val))
    print(f'{i}==>{stock_prices[i]}==>{avg1}')
 if value == 'add':
    stk_name =input('Enter a stock name').lower()
    stk_price = int(input('Enter the stock price'))
    if stk_name in stock_prices:
        cost_list = stock_prices[stk_name]
        cost_list.append(stk_price)
        print(cost_list)
        print(stock_prices)
    else: 
        stk_price = [stk_price]
        stock_prices[stk_name]=stk_price
        print(stock_prices)

import math
def circle_area(radius = 10):
    area = math.pi*(radius**2)
    print(f'The area of the circle is {area}')
    circumference = 2*math.pi*radius
    print(f'The circumference of the circle is {circumference}')
    diameter = 2*radius
    print(f'The diameter of the circle is {diameter}')

circle_area(8)



# Looping through keys seperately
# for country in copu:
#     print(f"Country: {country}")

# looping through items seperately
# for population in copu.values():
#     print(f"Population: {population}")

# copu = {'China': 143, 'India': 136, 'USA': 32, 'Pakistan': 21}

# # Looping through the dictionary
# for country, population in copu.items():
#     print(f"{country}: {population}")


