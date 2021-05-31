import pandas as pd


df = pd.read_csv (r'C:\Users\usach\Desktop\Python Problem Statements\Indian_cities.csv')
print (df)
df.shape
df.head(5)
df.columns
#1
#a
df1=df.nlargest(10,'sex_ratio')
df1[['state_name']]
#b
df2=df.nlargest(10,'total_graduates')
df2[['name_of_city']]
#c
df3=df.nlargest(10,'effective_literacy_rate_total')
df3[['name_of_city','location']]

#2
#a
df.columns
df=df[['literates_total']]
df.head(5)
df.hist()
#b
x=df[['male_graduates']]
y= df[['female_graduates']]
plt.plot(x,y,color='red')
plt.title("graduation between male and female")
plt.xlabel("male_graduates")
plt.ylabel("female_graduates")
plt.show()

#3
#a
df.columns
df['effective_literacy_rate_total'].plot(kind='box',title='total effective literacy rate',figsize=(10,8))
#b
df.isnull()
df.dropna(axis=1,inplace=True)
df.head(5)
df.shape




