import pandas

data = {'one': pandas.Series([1,2,3],index = ['a','b','c']), 'two': pandas.Series([4,5,6,7],index = ['a','b','c','d'])}

table = pandas.DataFrame(data)
print(table)