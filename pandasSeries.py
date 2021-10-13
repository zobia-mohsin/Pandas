import pandas as pd

grades = pd. Series([87, 100, 94])

# print(grades)

# Series is case sensitive, when printed tells us data type
grades2 = pd.Series(98.6, range(3))

# print(grades2)

# print(grades[0])

# print(grades.describe())

# onr way to do it:
grades = pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])
# another way, custom indexes
grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})

print(grades)

# accesing index
print(grades['Eva'])

# because index is atribute
print(grades.Wally)

print(grades.dtype)
# int64

print(grades.values)
# prints [87,1oo,94]

hardware = pd.Series(['Hammar', 'Saw', 'Wrench'])

print(hardware)

# calling string methods apply to each element
# true true false because wrech does not have an a
print(hardware.str.contains('a'))

print(hardware.str.upper())
