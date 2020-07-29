import pandas

table = pandas.read_csv('panda.csv')
print(table)
table1 = pandas.DataFrame([[1,2,3],[4,5,6]])

table1.to_csv('panda2.csv')
print(table1)