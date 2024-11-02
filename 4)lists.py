#A1) and all the five parts it does have

expense_list = [2200,2350,2600,2130,2190]

extra_doll = (expense_list[1] - expense_list[0] )
print('Extra dollars are',extra_doll)

first_qrt = 0
for i in range(3):
 first_qrt = first_qrt + expense_list[i]
print('Expenses in first quarter are',first_qrt)

for i in range(len(expense_list)):
  if expense_list[i] == 2000:
    print('You spend 2000 in',i+1,'this month')

expense_list.append(1980)
expense_list[3] = (expense_list[3] - 200)
print(expense_list)

#A2)

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.pop()
heros.insert(3,'black panther')
print(heros)
heros[1:3] = ['doctor strange']
print(heros)
heros.sort()

#remove(value): Removes the first occurrence of the specified value.
#pop(index): Removes and returns the element at the specified index (or the last one if no index is given).
#del: Deletes an element (or a slice) at a specific index. del my_list[1:3]
#clear(): Removes all elements from the list.