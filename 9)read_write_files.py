with open('/Users/jyotiradityagullinkala/Desktop/DS:AI/road.txt','r') as f:
 passage = f.read()
 words = passage.split()
 cnt_words = {}
 for i in words:
  if i in cnt_words:
   cnt_words[i] += 1
  else:
   cnt_words[i] = 1
max_value = max(cnt_words.values())
max_key=[]
for key,value in cnt_words.items():
 if value == max_value:
  max_key.append(key)
print(max_key)

# max_value = [key for key, value in cnt_words.items() if value == max_value] The above for loop and the list creation can also be replaced by this method, this is called the list compresion method.Notice how the whole process is covered in square brackets which indicates that the items will go into a list.if there is a for condition and a if then definitely we can use this method to create a new list.


with open('/Users/jyotiradityagullinkala/Desktop/DS:AI/stocks.csv','r') as f, open('/Users/jyotiradityagullinkala/Desktop/DS:AI/output.csv','w') as out:
 out.write("Company Name,PE Ratio,PB Ratio")
 next(f)# if you want to skip the first line of the loop
 for line in f:
  tokens = line.split(",")
  tokens = line.split(",")
  stock = tokens[0]
  price = float(tokens[1])
  eps = float(tokens[2])
  book = float(tokens[3])
  pe = round(price / eps, 2)
  pb = round(price / book, 2)
  out.write(f"{stock},{pe},{pb}\n")






