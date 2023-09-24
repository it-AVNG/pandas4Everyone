'''
creating data structure 
'''
import pandas as pd

# creating a series
s = pd.Series(['banana',42])
print()
print(s)

# manually assign index value
s = pd.Series(
    data = [['banana','apple'],['pork','chicken']],
    index = ['fruit','protein'],
)
print()
print(s)

s = pd.Series({'key':'get ready'})
print()
print(s)

# creating DataFrame
scientist = pd.DataFrame(
{
    "Name": ["Rosaline Franklin", "William Gosset"],
    "Occupation": ["Chemist", "Statistician"],
    "Born": ["1920-07-25", "1876-06-13"],
    "Died": ["1958-04-16", "1937-10-16"],
    "Age": [37, 61],
},
# index = ["Rosaline Franklin", "William Gosset"],
columns=['Name','Age','Born','Died','Occupation']
)
print()
print(scientist)

