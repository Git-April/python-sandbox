import pandas as pd

data = [[-50, 40, 30], [-1, 2, -2]]
df = pd.DataFrame(data)
print(df.abs())

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.add(15))

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data)
newdf = df.add_prefix("preson_")
print(newdf)

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data)
newdf = df.add_suffix("_after")
print(newdf)

data = {
  "x": [50, 40, 30],
  "y": [300, 1112, 42]
}
df = pd.DataFrame(data)
x = df.agg(["sum"])
print(x)
y = df.aggregate(["sum"])
print(y)

data = [[True, False, True], [True, True, True]]
df = pd.DataFrame(data)
print(df.all())

data = [[True, False, True], [True, False, False]]
df = pd.DataFrame(data)
print(df.any())

def calc_sum(x):
  return x.sum()

data = {
  "x": [50, 40, 30],
  "y": [300, 1112, 42]
}
df = pd.DataFrame(data)
x = df.apply(calc_sum)
print(x)

data = {
  "age": [16, 14, 10],
  "qualified": [True, True, True]
}
df = pd.DataFrame(data)
newdf = df.assign(name = ["Emil", "Tobias", "Linus"])
print(newdf)

data = {
  "Duration": [50, 40, 45],
  "Pulse": [109, 117, 110],
  "Calories": [409.1, 479.5, 340.8]
}
df = pd.DataFrame(data)
newdf = df.astype('int64')
print(newdf)

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
print(df.at[1, "firstname"])

df = pd.read_csv('data.csv')
print(df.axes)

df = pd.read_csv('data.csv')
newdf = df.bfill()
print(newdf)

df = pd.read_csv('data.csv')
print(df.columns)

df1 = pd.DataFrame([[1, 2], [3, 4]])
df2 = pd.DataFrame([[5, 6], [7, 8]])
def myfunc(a, b):
  if (a.sum() > b.sum()):
    return a
  else:
    return b
print(df1.combine(df2, myfunc))

df1 = pd.DataFrame([[1, 2], [None, 4]])
df2 = pd.DataFrame([[5, 6], [7, 8]])
print(df1.combine_first(df2))

data = {
  "name": ["Sally", "Mary", pd.NA],
  "qualified": [True, False, pd.NA]
}
df = pd.DataFrame(data)
print("Original dtypes:")
print(df.dtypes)
newdf = df.convert_dtypes()
print("New dtypes:")
print(newdf.dtypes)

data = {
  "Duration": [50, 40, 45],
  "Pulse": [109, 117, 110],
  "Calories": [409.1, 479.5, 340.8]
}
df = pd.DataFrame(data)
print(df.corr())

data = {
  "Duration": [50, 40, None, None, 90, 20],
  "Pulse": [109, 140, 110, 125, 138, 170]
}
df = pd.DataFrame(data)
print(df.count())

data = [[5, 6, 7], [2, 6, 9]]
df = pd.DataFrame(data)
print(df.cov())

data = {
  "firstname": ["Sally", "Mary", "John"],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
newdf = df.copy()
print(newdf)

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.cummax())

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.cummin())

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.cumprod())

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.cumsum())

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.describe())

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.diff())

data = {
  "points": [100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.div(10))

df1 = pd.DataFrame([[1, 2], [3, 4]])
df2 = pd.DataFrame([[5, 6], [7, 8]])
print(df1.dot(df2))

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
newdf = df.drop("age", axis='columns')
print(newdf)

data = {
  "firstname": ["Sally", "Mary", "John", "Mary"],
  "age": [50, 40, 30, 40],
  "qualified": [True, False, False, False]
}
df = pd.DataFrame(data)
newdf = df.drop_duplicates()
print(newdf)

data = {
  "name": ["Bill", "Bob", "Betty"],
  "age": [50, 50, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data).set_index(["name", "age"])
newdf = df.droplevel(0)
print(df)
print(newdf)

df = pd.read_csv('data.csv')
newdf = df.dropna()
print(newdf)

df = pd.read_csv('data.csv')
print(df.dtypes)

data = {
  "firstname": ["John", "Mary", "John", "Sally", "Mary"],
  "age": [40, 30, 40, 50, 30],
  "city": ["Bergen", "Oslo", "Stavanger", "Oslo", "Oslo"]
}
df = pd.DataFrame(data)
s = df.duplicated()
print(s)