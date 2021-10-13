import pandas as pd

# data frame is two dimensional whereas series is only one dimensional
# each column in a data fram is a column, each column returned as a series in data frame.
grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}

grades = pd.DataFrame(grades_dict)  # makes the dictionary a dataframe

grades.index = ['Test1', 'Test2', 'Test3']

print(grades)


# return rows of eva's grade as SERIRES, GRABS COLUMN OF EVA UP AND DOWN
print(grades['Eva'])

print(grades.Sam)  # column headers become attributes of our data frame

# same thing as Eva, to get all of test1 grades
print(grades.loc['Test1'])

print(grades.iloc[1])
# Row and column and use brackets to spearete [] row and columns

# but with loc upperbound is included
print(grades.loc['Test1':'Test3'])

# with iloc method, upper method not included,
print(grades.iloc[0:2])

#print(grades.loc[['Test1', 'Test3']])

# gives outcome as rows and columns if we add another set of []
#print(grades.iloc[0, 2])
# if consecutive we can use colons and if not then use commas and []
#print(grades.loc['Test1':'Test2', ['Eva', 'Katie']])

# print(grades.iloc[0:2, [1, 3]])  # UPPERBOUND NOT INCLUDED AND ONLY USE INDEXES
# You can use either methods

# BOOLEAN INDEXES, checks every value in your data DataFrame

grades90 = grades[grades >= 90]

# print(grades90)  # RESULTS shows once that pass the test, other ones NaN meaning fail

gradesB = grades[(grades >= 80) & (grades < 90)]

# print(gradesB)

gradesAorB = grades[(grades > 90) | (grades >= 80)]  # line is OR |

# print(gradesAorB)

print(grades.at['Test2', 'Eva'])

# if we wanted to update a grade

#grades.at['Test2', 'Eva'] = 100

print(grades)

print(grades.iat[1, 1])

print(grades.describe())
# gives alot of information for each student, information by student, can change decimal points

# changes all information from describe to 2 decimal places based on student
pd.set_option('precision', 2)

print(grades.describe())

# lets say we want describe information sorted by test name, describe only does it by column so transpose
print(grades.T.describe())

# sorting by name of index from increasing to decr4easing
# print(grades.T.sort_index(ascending=False))

# print(grades.sort_index(axis=1))  # sorting by row instread of column axis = 0

# sorts row one of Test1 for all students, have to specify row you want to assort by
print(grades.sort_values(by='Test1', axis=1, ascending=False))

print(grades.T.sort_values(by='Test1', ascending=False))

print(grades.loc['Test1'].sort_values(ascending=False))  # only shows test 1
