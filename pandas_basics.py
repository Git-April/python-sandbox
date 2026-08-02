import pandas as pd #Pandas HOME

#Pandas HOME
df = pd.read_csv('pandas_basics_data.csv')

print(df.to_string())

#Pandas Getting Started
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

print(pd.__version__)