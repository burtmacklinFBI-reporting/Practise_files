result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
j=0
for i in range(len(result)):
    if result[i] == "heads":
        j = j + 1
print(f'You have got heads {j} times')

for i in range(1,11):
    if i%2 == 1:
        print(f'The square for {i} is',i**2)

expense_list = [2340, 2500, 2100, 3100, 2980]
exp =float(input('Please enter an amount'))
if exp in expense_list:
        i = expense_list.index(exp)
        print(f'You have made {exp} expense in {i+1} month')
else:
        print(f'You have not made this specific {exp} in any month')

for i in range(1,6):
    response =input('are you tired?').lower()
    if response == 'yes':
        print("you didn't finish the race")
        break
    elif response == 'no':
        if i==5: 
         print('Congratulations on completeing the race')
         break
    
for i in range(1,6):
    print('*'*i)
    
for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)
 



