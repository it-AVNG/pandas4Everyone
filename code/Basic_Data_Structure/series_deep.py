import pandas as pd

scientist = pd.DataFrame(
    {
        'Name': ["Rosaline Franklin", "William Gosset"],
        'Occupation': ["Chemist", "Statistician"],
        'Born': ["1920-07-25", "1876-06-13"],
        'Died': ["1958-04-16", "1937-10-16"],
        'Age': [37, 61],
    },
    index = ["Rosaline Franklin", "William Gosset"],
    columns= ['Name','Age','Occupation','Born','Died']
)
print(scientist)

# Select a scientist using index label
print()
person = scientist.loc['William Gosset']
print(person.values)
print(type(person.values))