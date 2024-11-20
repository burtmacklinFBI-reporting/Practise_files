from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df_sales = pd.read_excel('linechart.xlsx')
plt.figure(figsize=(12,4))
plt.plot(df_sales['Quarter'],df_sales['Fridge'],color = 'blue',label = 'ridge') #provide x axis and y axis
 #can increase the size of the graphAd
plt.plot(df_sales['Quarter'],df_sales['Dishwasher'],color = 'green',label = 'Dishwasher') 
plt.plot(df_sales['Quarter'],df_sales['Washing Machine'],color = 'orange',label = 'Washing Machine') 
plt.title('Product Sales') #add the title to the chart
plt.ylabel('Revenue (in $)')
plt.xlabel('Product Sales')
plt.legend() #this will show you the legend with all the colour coding
print(plt.show())

total_sales = df_sales[['Fridge','Dishwasher','Washing Machine']].sum()
plt.pie(total_sales,labels=total_sales.index,autopct='%1.1f%%') #there are two precision points.autopct means to keep the percentages on the pie and f means float and then if you keep 1.2f that means two precision points
print(plt.show())

#check other parameters in the pie chart.

plt.pie(total_sales,labels=total_sales.index,autopct='%1.1f%%',explode=(0.1,0.1,0),shadow=True)
print(plt.show())
#the explode needs a tuple parameter and then in that you will pass the number of parameters that are equal to the number of pies present in the chart and in the same particular order and that part is going to explode and then make yours come outside. Shadow will give you a shadow to the outline.


#PLOTTING A BAR CHART, you can easily do in the dataframe without using pyplopt

df_sales.plot(kind='bar',x='Quarter')
print(plt.show())

#practise more modules and each of them.