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

df = pd.read_csv('data.csv')
print(df.empty)

df = pd.DataFrame([[10, 12, 2], [3, 4, 7]])
print(df.eq(7))

data1 = {
  "firstname": ["Sally", "Mary", "John", "Mary"],
  "age": [50, 40, 30, 40]
}
df1 = pd.DataFrame(data1)
data2 = {
  "firstname": ["Sally", "Mary", "John", "Mary"],
  "age": [50, 40, 30, 40]
}
df2 = pd.DataFrame(data2)
print(df1.equals(df2))

data = {
  "Women": [125, 230, 412],
  "Men": [219, 185, 452]
}
df = pd.DataFrame(data)
print(df.eval("Women + Men"))

data = {
  "Brand": ["Ford", "Ford", "Ford"],
  "Model": ["Sierra", "F-150", "Mustang"],
  "Typ": ["2.0 GL", "Raptor", ["Mach-E", "Mach-1"]]
}
df = pd.DataFrame(data)
newdf = df.explode('Typ')
print(newdf)

df = pd.read_csv('data.csv')
newdf = df.ffill()
print(newdf)

df = pd.read_csv('data.csv')
newdf = df.fillna(222222)
print(newdf)

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
newdf = df.filter(items=["name", "age"])
print(newdf)

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.floordiv(10))

df = pd.DataFrame([[10, 12, 2], [3, 4, 7]])
print(df.ge(7))

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
print(df.get("firstname"))

data = {
  'co2': [95, 90, 99, 104, 105, 94, 99, 104],
  'car': ['Skoda', 'Skoda', 'Ford', 'Skoda', 'Ford', 'Ford', 'Skoda', 'Ford']
}
df = pd.DataFrame(data)
print(df.groupby(["car"]).mean())

df = pd.DataFrame([[10, 12, 2], [3, 4, 7]])
print(df.gt(7))

df = pd.read_csv('data.csv')
print(df.head())

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
print(df.iat[2, 1])

data = {
  "sales": [23, 34, 56],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
print(df.idxmax())

data = {
  "sales": [23, 34, 56],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
print(df.idxmin())

data = [[50, True], [40, False], [30, False]]
df = pd.DataFrame(data)
print(df.iloc[1, 0])

df = pd.read_csv('data.csv')
print(df.index)

data = {
  "age": ["fifty", 40, 30],
  "qualified": ["No", True, False]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("Original dtypes:")
print(df.dtypes)
df = df.iloc[1:]
print("New DataFrame:")
print(df)
newdf = df.infer_objects()
print("New dtypes:")
print(newdf.dtypes)

df = pd.read_csv('data.csv')
df.info()

data = {
  "firstname": ["Sally", "Mary", "John"],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
df.insert(1, "age", [50, 40, 30])
print(df)

df = pd.read_csv('data2.csv')
newdf = df.interpolate(method='linear')
print(newdf)

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
print(df.isin([50, 40]))

df = pd.read_csv('data2.csv')
newdf = df.isna()
print(newdf)

df = pd.read_csv('data2.csv')
newdf = df.isnull()
print(newdf)

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
for x, y in df.items():
  print(x)
  print(y)

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
for index, row in df.iterrows():
  print(row["firstname"])

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
for row in df.itertuples():
  print(row)

data1 = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
data2 = {
  "qualified": [True, False, False]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
newdf = df1.join(df2)
print(newdf)

df = pd.DataFrame([[10, 12, 2], [3, 4, 7]])
print(df.le(7))

data = [[50, True], [40, False], [30, False]]
label_rows = ["Sally", "Mary", "John"]
label_cols = ["age", "qualified"]
df = pd.DataFrame(data, label_rows, label_cols)
print(df.loc["Mary", "age"])

df = pd.DataFrame([[10, 12, 2], [3, 4, 7]])
print(df.lt(7))

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
print(df.keys())

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data)
newdf = df.mask(df["age"] > 30)
print(newdf)

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.max())

data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]
df = pd.DataFrame(data)
print(df.mean())

data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]
df = pd.DataFrame(data)
print(df.median())

df = pd.read_csv('data.csv')
newdf = df.melt()
print(newdf)

df = pd.read_csv('data.csv')
print(df.memory_usage())

data1 = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
data2 = {
  "firstname": ["Sally", "Peter", "Micky"],
  "age": [77, 44, 2]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
newdf = df1.merge(df2, how='right')
print(newdf)

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.min())

data = {
  "points": [5, 6, 4],
  "total": [50, 40, 20]
}
df = pd.DataFrame(data)
print(df.mod(3))

data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]
df = pd.DataFrame(data)
print(df.mode())

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.mul(10))

df = pd.read_csv('data.csv')
print(df.ndim)

df = pd.DataFrame([[10, 12, 2], [3, 4, 7]])
print(df.ne(7))

df = pd.read_csv('data.csv')
newdf = df.nlargest(10, "Calories")
print(newdf)

df = pd.read_csv('data.csv')
newdf = df.notna()
print(newdf)

df = pd.read_csv('data.csv')
newdf = df.notnull()
print(newdf)

df = pd.read_csv('data.csv')
newdf = df.nsmallest(10, "Calories")
print(newdf)

data = [[10, 20, 0], [10, 10, 10], [10, 20, 30]]
df = pd.DataFrame(data)
print(df.nunique())

data = [[10, 18, 11], [20, 15, 8], [30, 20, 3]]
df = pd.DataFrame(data)
print(df.pct_change())

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
df.pop("age")
print(df)

data = {
  "points": [4, 5, 6],
  "total": [10, 12, 15]
}
df = pd.DataFrame(data)
print(df.pow(5))

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.prod())

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.product())

data = [[1, 1, 2], [6, 4, 2], [4, 2, 1], [4, 2, 3]]
df = pd.DataFrame(data)
print(df.quantile(0.2))

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
print(df.query('age > 35'))

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.radd(15))

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.rdiv(10))

data = {
  "age": [50, 40, 30, 40],
  "qualified": [True, False, False, False]
}
idx = ["Sally", "Mary", "John", "Monica"]
df = pd.DataFrame(data, index=idx)
newidx = ["Robert", "Cindy", "Chloe", "Pete"]
newdf = df.reindex(newidx)
print(newdf)


data = {
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
idx = ["Sally", "Mary", "John"]
df = pd.DataFrame(data, index=idx)
newdf = df.rename({"Sally": "Pete", "Mary": "Patrick", "John": "Paula"})
print(newdf)

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
newdf = df.rename_axis("members")
print(newdf)

data = {
  "name": ["Bill", "Bob", "Betty"],
  "age": [50, 50, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
newdf = df.replace(50, 60)
print(newdf)

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
idx = ["X", "Y", "Z"]
df = pd.DataFrame(data, index=idx)
newdf = df.reset_index()
print(newdf)

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.rfloordiv(10))

data = {
  "points": [5, 6, 4],
  "total": [50, 40, 20]
}
df = pd.DataFrame(data)
print(df.rmod(3))

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.rmul(10))

data = [[1.1235, 1.9654, 2.6874], [6.5124, 4.2210, 2.2899]]
df = pd.DataFrame(data)
print(df.round(1))

data = {
  "points": [5, 6, 4],
  "total": [10, 12, 15]
}
df = pd.DataFrame(data)
print(df.rpow(5))

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.rsub(15))

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.rtruediv(10))

df = pd.read_csv('data.csv')
print(df.sample())

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.sem())

df = pd.read_csv('data.csv')
newdf = df.select_dtypes(include='int64')
print(newdf)

df = pd.read_csv('data.csv')
print(df.shape)

data = {
  "age": [50, 40, 30],
  "qualified": [True, False, False]
}
df = pd.DataFrame(data)
newdf = df.set_axis(["John", "Peter", "Alex"])
print(newdf)

data = {
  "name": ["Sally", "Mary", "John", "Monica"],
  "age": [50, 40, 30, 40],
  "qualified": [True, False, False, False]
}
df = pd.DataFrame(data)
newdf = df.set_index('name')
print(newdf)

df = pd.read_csv('data.csv')
print(df.size)

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.skew())

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
idx = ["Mary", "Sally", "Emil", "Tobias", "Linus", "John", "Peter"]
df = pd.DataFrame(data, index=idx)
newdf = df.sort_index()
print(newdf)

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data, index=idx)
newdf = df.sort_values(by='age')
print(newdf)

data = {
  "age": [50, 40, 30, 40, 20, 10, 30]
}
df = pd.DataFrame(data)
s = df.squeeze()
print(s)

df = pd.read_csv('data.csv')
newdf = df.stack()
print(newdf)

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.std())

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.sum())

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.sub(15))

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data)
newdf = df.T
print(newdf)

df = pd.read_csv('data.csv')
print(df.tail())

df = pd.read_csv('data.csv')
print(df.take([5, 10]))

def eur_to_nok(x):
  return x * 10
data = {
  "for1": [2, 6, 3],
  "for2": [8, 20, 12]
}
df = pd.DataFrame(data)
newdf = df.transform(eur_to_nok)
print(newdf)

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data)
newdf = df.transpose()
print(newdf)

data = {
  "points":[100, 120, 114],
  "total": [350, 340, 402]
}
df = pd.DataFrame(data)
print(df.truediv(10))

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data)
newdf = df.truncate(before=3, after=5)
print(newdf)

df1 = pd.DataFrame([["Emil", "Tobias", "Linus"], [16, 14, 10]])
df2 = pd.DataFrame([["Emil"], [17]])
df1.update(df2)
print(df1)

df = pd.read_csv('data.csv')
print(df.values)

data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]
df = pd.DataFrame(data)
print(df.var())

data = {
  "age": [50, 40, 30, 40, 20, 10, 30],
  "qualified": [True, False, False, False, False, True, True]
}
df = pd.DataFrame(data)
newdf = df.where(df["age"] > 30)
print(newdf)

data = {
  'weight': [929, 1109, 1112, 1119, 1328, 1584, 1415, 1235],
  'co2': [95, 90, 99, 104, 105, 94, 99, 104],
  'model': ['Citigo', 'Fabia', 'Fiesta', 'Rapid', 'Focus', 'Mondeo', 'Octavia', 'B-Max'],
  'car': ['Skoda', 'Skoda', 'Ford', 'Skoda', 'Ford', 'Ford', 'Skoda', 'Ford']
}
df = pd.DataFrame(data)
df = df.set_index(['car', 'model'])
print(df.xs('Ford'))

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}
df = pd.DataFrame(data)
for x in df.__iter__():
  print(x)