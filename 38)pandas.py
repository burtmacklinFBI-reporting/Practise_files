import pandas as pd, numpy as np

df = pd.read_csv('movies.csv') # this is the module to read csv files, and the object that we have created is a dataframe. Pandas deal a lot about data frames.
print(df)

df.head(3) # this will give you the first top 3 rows 
df.tail(3) #this will give me the last 3 rows in the table
df.sample(6) #this will randomly get you the sample of the rows
df[2:6] #this will give you the rows from 2 to 5
df[['title','industry','imdb_rating']] #this will help us add filter what are the columns that we would be needing
df.shape #this will give you the shape of the table like (35,10) means 35 rows and 10 columns
df.columns #would let us know what are those columns



print(df['title']) #this is one way to access the titles of the table
print(df.title) #this is another way to print it as this treating the column like a property and this property is called as series.

dir(df.title) #this would give us all the properties that I can use on the column title

df.title.min(),df.title.max() #this is how you can do max and min

#doing filter operation based on a certain column, like using the where clause in SQL. we would be getting a new list so it is better to make a new dataframe

df_b = df[df.industry == 'Bollywood']
df.industry.unique() #this will give the unique values in the industry

df.industry.value_counts() #this is the way to know count of all the industries that are there. Just like count in sql.

df[df.release_year > 2000]
df[(df.release_year > 2000) & (df.release_year < 2010)] #this is a way where you can filter multiple rows

df.describe() #this will give you all the min, max, and some other mathemical operation for all the arthimetic groups that are present

df.info() #this will give info on all the columns

df[df.imdb_rating == df.imdb_rating.max()]
df[(df.imdb_rating == df.imdb_rating.max()) | (df.imdb_rating == df.imdb_rating.min())] #this is a way of using the OR function

df['age'] = df.release_year.apply(lambda x: 2023 - x)
#this is a way to derive a new column based on another column. We are creating a new column called age and then we ar appling the operation on release year. and the lamda x is kind of like a for loop where each release_year value would go into x and then it would work.


df['profit'] = df.apply(lambda x: x['revenue'] - x['budget'], axis = 1)
#this is a way of creating a new column based on multiple columns and axis =1 means that row.

df.index # whenever you create a dataframe you would automatically be having an index, but you can also make a column as your index so that it will be acting an primary key and you can know all its details easily using loc ( location of index)


df.set_index('title',inplace= True) #this will make the title as index and we use inplace = true because it will modify the existing df and not create a new df.

df.loc['Pather Panchali']
df.loc['Pather Panchali','Doctor Strange']

df.iloc[2:3] #even though you do not have a index based integer no more you can use like this and you can always reset in a way you want.

df.reset_index(inplace=True)

# READING AND MANIPULATING CSV FILES


df = pd.read_csv('stock_data.csv') #read_csv is not only used to read the csv, but there a lot of parameters that we can use to see. Like you can skip some number of rows, or make a particular rows your header and many more which you will be seeing below.
# print(df)

df = pd.read_csv('stock_data.csv',skiprows=1) 
# print(df) #see now this has skipped the first line making the second line the header which is important.

df = pd.read_csv('stock_data.csv',header=1) 
# print(df)
#this is an another way to write it, as in this you can select which row you want it to be the header. Remember that the row index starts from 0.

df = pd.read_csv('stock_data.csv',header=1,names= ['stock_symbol','eps','revenue','price','people']) 
# print(df)
#this method is used to rename the columns already present according to your views. But the thing is you need to enter all the columns that are present in the same particular order.

#now what if you want to see only 2 rows, like how you see in sql about FETCH FIRST 10 ROWS ONLY;
df = pd.read_csv('stock_data.csv',header=1,nrows= 4) 
# print(df)
#this will give us 4 rows apart from the header, but you can also filter after creating the dataframe using head, tail, sample but turns out this is a little more efficient that the other methods.


#you can convert values into NaN. You can either deal with column specific or you can deal with them all as a whole.

#column specific
df = pd.read_csv('stock_data.csv',header=1,na_values={ 'eps': ['not available'],'revenue':[-1],'people':['not available','n.a']})
#what this will do is it will go into that respective column and then it will go into that respective column and then modify those values in that respective columns to the value mentioned.


#entire table specific, you can give all the values an an entire list
df = pd.read_csv('stock_data.csv',header=1,na_values= ['not available',-1,'n.a'])

#derived columns
df['pe'] = df['price']/df['eps']
#this is an another way to get derived columns along with the df.apply method.

df.to_csv('pe.csv')
#this will create a new csv, and there are a lot of additions which we can do to this as well, like we can remove the index and we can also remove the header
df.to_csv('pe.csv',index=False,header= True)



#READING AND EDITING EXCEL FILES

df_movies = pd.read_excel('movies_db.xlsx','movies')
print(df)
# this is how you can read the excel file but the important thing is that you also need to mention the sheet that you are going to be using as it does not make sense if you do not mention the sheet.

#suppose there are some values that are present in a column which you want to change or convert then you can use converters function.


def standarize_currency(val):
    if val == '$$' or val =='Dollars':
        return 'USD'
    return val
df_finance = pd.read_excel('movies_db.xlsx','financials',converters= {'currenncy':standarize_currency})

# now in this we have converted the currency column nased on the standarize column specifically. 

# you can also two data frames based on a column, just like you are using joins in sql

df_merged = pd.merge(df_movies,df_finance,on = 'movies_id')
df_merged.to_excel('movies_merged.xlsx',sheet_name='merged',index = False)

#you can also create a dataframe from not only excel and csv but you can also use an dictionary with the keys being the column name and the values being the values. This is how you can create a dataframe

df_weather = pd.DataFrame({'day':[],'price':[],'vile':[]})

#you can also send two dataframes into one excel.

with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_finance.to_excel(writer,sheet_name= 'stocks')
    df_weather.to_excel(writer,sheet_name='weather')


#handling missing data

# when you are thinking about handling data first check if each column or atleast the column that you want to handle are in the data type that you want.

df_w = pd.read_csv('weather_data.csv',parse_dates=['day'])
print(df_w)
df_w.set_index('day',inplace=True)
print(df_w)


# Suppose you want to fill all the N/A values to 0 then you can use fillna function. The inplace argunment is very necessary as otherwise it will return you a new dataframe which you do not want.

df_w.fillna(0,inplace=True)

#or you can also replace a certain values in a column with the values that you want.

df_w.fillna({'temperature':df_w.temperature.mean(),'windspeed':df_w.windspeed.mean()})

#method = 'ffill' which means that forward fill, which means that it will fill the NA value with the previous value. But the limitation is if there 10 NA then it will fill each and every other value but we can also set a limit.

df_w.fillna(method = 'ffill') 
df_w.fillna(method = 'ffill',limit= 1)
#this way you can set a limit and know that only one NA value is going to filled 

#method ='bfill' which means you are viewing them by columns and then you would be filling the column 2 NA value with column 3 value.
df_w.fillna(method = 'bfill',axis='columns') 


#interpolate function, this function fill the NA value between two values and then tries to interpolate, or more like follow a linear graph. like 32, NA, 28 then when you interpolate on numeric columns then this is how it works.

df_w.interpolate()

#dropna. It will just drop the rows which even has a single NA value.

df_w.dropna()
df_w.dropna(how='all') #this means it will only drop if all the elements of the row do contain NA.
df_w.dropna(thresh=2) #drop any row which will have atleast two min values.

# you can also replace values a value with a certain value. Also you can use numpy to edit the values and then replace them with Nan values.

df_w.replace(-9999,0)
df_w.replace(-9999,np.nan)
df_w.replace(to_replace=[-9999,-8888],value=np.nan) #this is how you can replace multiple values

df_w.replace({'temperature':-9999,'windspeed':[-9999,-8888],'event':'no event'},np.nan)

df_w.replace({-9999:np.nan,-8888:np.nan,'no event':'Sunday'})

# GROUPING DATA
# It will create data frames which are based on the column that you pass. You can also iterate on them.

df_wc = pd.read_csv('weather_by_cities.csv',parse_dates=['day'])
# df_wc.set_index('day',inplace=True)
print(df_wc)

g = df_wc.groupby('city')
#this will create new groups for each city and then we can access them or we can also iterate over them just like we do over a dictionary

for city, data in g:
    print('city',city)
    print('data',data)
print(g.get_group('paris'))

print(g.max()) #it will do through each individual data group and then it will give you the max of each possible data group. This is the process for the numeric functions, like avg or mean. It will work individually for each group.

def grouper(df,idx,col):
    if 80<= df.at[idx, col] <=90:
        return '80-90'
    elif 50 <= df.at[idx, col] <=60:
        return '50-60'
    else:
        return 'others'
    
g1 = df_wc.groupby(lambda idx: grouper(df_wc,idx,'temperature'))

for key,d in g1:
    print('Key',key)
    print('data',d)

#you can now also group by like this where you can also create your own function and then also group by.

#DATA CONCATENATION AND MERGE OPERATIONS

india_weather = pd.DataFrame({'city':['mumbai','delhi','bangalore'],'temperature':[32,45,30],'humidity':[80,60,78]})

print(india_weather)

usa_weather = pd.DataFrame({'city':['new york','chicago','orlando'],'temperature':[21,14,35],'humidity':[68,65,75]})

print(usa_weather)

print(pd.concat([india_weather,usa_weather])) #in this the index is same and not in a sequence, as it is using the index from the old dataframe

print(pd.concat([india_weather,usa_weather],ignore_index=True))
#so now you get a continous index over here

#you can also specify keys for each dataframe, and this concept can be used to easily data for each index.

kl=pd.concat([india_weather,usa_weather],keys=['india','usa'])
print(kl.loc['india']) #this is a way you can filter out and see what is really happening.

# column wise concentation. you need to change the axis = 1 for column wise concatenation, but you need to have index same for each individual element, so while declaring the data frame itself, there is a seperate parameter present where you can give it a index like the way you want it.

df1 = pd.DataFrame({'city':['new york','chicago','orlando'],'temperature':[21,14,35]})

df2 = pd.DataFrame({'city':['new york','orlando','chicago'],'humidity':[65,68,75]})

print(pd.merge(df1,df2,on='city')) #it is just like join in sql, only cities which are common. It is default a inner join and you can change the join

print(pd.merge(df1,df2,on='city',how='left')) #this is how you can specify the join conditions.