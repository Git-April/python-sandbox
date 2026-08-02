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

#Pandas Series
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

print(myvar[0])

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

print(myvar["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

#Pandas DataFrames
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)

print(df.loc[0])

print(df.loc[[0, 1]])

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)

print(df.loc["day2"])

df = pd.read_csv('pandas_basics_data.csv')
print(df)

#Pandas Read CSV
df = pd.read_csv('data.csv')
print(df.to_string())

df = pd.read_csv('data.csv')
print(df)

print(pd.options.display.max_rows)

pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)

#Pandas Read JSON
df = pd.read_json('data.json')
print(df.to_string())

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
print(df)

#Pandas Analyzing Data
df = pd.read_csv('data.csv')
print(df.head(10))

df = pd.read_csv('data.csv')
print(df.head())

print(df.tail())

print(df.info())

#Cleaning Empty Cells
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())

df = pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df.to_string())

df = pd.read_csv('data.csv')
df.fillna({"Calories": 130}, inplace=True)

df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)

df = pd.read_csv('data.csv')
x = df["Calories"].median()
df.fillna({"Calories": x}, inplace=True)

df = pd.read_csv('data.csv')
x = df["Calories"].mode()
df.fillna({"Calories": x}, inplace=True)

#Cleaning Wrong Format
df = pd.read_csv('data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df.to_string())

df.dropna(subset=['Date'], inplace=True)

#Cleaning Wrong Data
df.loc[7, 'Duration'] = 45

#Removing Duplicates
df = pd.read_csv('data.csv')
print(df.duplicated())

df.drop_duplicates(inplace=True)