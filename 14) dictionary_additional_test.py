data = {}
first_week_data = {}
max_temp_list = {}
with open('/Users/jyotiradityagullinkala/Desktop/DS:AI/nyc_weather.csv','r') as f:
    for line in f:
        i = line.split(',')
        date = i[0]
        temp = i[1]
        data[date] = temp
max_temp=0     
for k,v in data.items():
    day =k.split(' ')
    if len(day) > 1 and int(day[1]) <= 7:
      first_week_data[k] = v
    if len(day) > 1 and int(day[1]) <= 10:
      if int(v)>=max_temp:
         max_temp=int(v)
 
    
for k,v in data.items():
       day =k.split(' ')
       if len(day) > 1 and int(day[1]) <= 10 and int(v) == max_temp:
        max_temp_list[k] = v

print('max_temp_list',max_temp_list)
print('entire_data',data)