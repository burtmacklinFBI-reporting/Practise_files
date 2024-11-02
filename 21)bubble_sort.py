def bubblesort(element,key='name'):
  if key.lower() == 'name' or key.lower() == 'transaction_amount' or key.lower() == 'device' :
     sorting_list = []
     for k in element:
        sorting_list += [k[key]]
        length =len(sorting_list)
     for j in range(length-1):
         swapped = False
         for i in range(length- 1-j):
          if sorting_list[i] > sorting_list[i+1]:
            swap = sorting_list[i]
            sorting_list[i] = sorting_list[i+1]
            sorting_list[i+1]=swap
            swapped = True

         if not swapped:
          break
    
     new_sorted_list = []
     for i in sorting_list:
         for k in element:
            if k[key] == i:
               new_sorted_list.append(k)

     return new_sorted_list
  else:
     return 'entered key does not exist'

     
 
  # or this is a different apporach that you can try which is easy
#   def bubble_sort(elements, key=None):
#     size = len(elements)

#     for i in range(size-1):
#         swapped = False
#         for j in range(size-1-i):
#             a = elements[j][key]
#             b = elements[j+1][key]
#             if a > b:
#                 tmp = elements[j]
#                 elements[j] = elements[j+1]
#                 elements[j+1] = tmp
#                 swapped = True

#         if not swapped:
#             break
    
  
            
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

print(bubblesort(elements,'transaction_amount'))