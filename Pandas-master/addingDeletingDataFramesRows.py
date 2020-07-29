import pandas

table = pandas.DataFrame({
    'one': pandas.Series([1,2,3],index = ['a','b','c']),
    'two': pandas.Series([4,5,6,7],index = ['a','b','c','d'])
    })

print(table.loc['a'])

table = table.append(pandas.DataFrame([[30,60]],columns = ['one','two']))
print(table)

table = table.drop('a')
print(table)