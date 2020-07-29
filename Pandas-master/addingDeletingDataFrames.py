import pandas

table = pandas.DataFrame({
    'one': pandas.Series([1,2,3],index = ['a','b','c']),
    'two': pandas.Series([4,5,6,7],index = ['a','b','c','d'])
    })
print(table)
table['New'] = pandas.Series([8,9,10], index = ['b','c','d'])
print(table)
print(table.pop('one'))
print(table)
del(table['two'])
print(table)