import pandas as pd

data = {'Name': ['John', 'Cateline', 'Matt', 'Oliver'],
        'ID': [1, 22, 23, 36]}

df = pd.DataFrame(data)

#one hot encoding 
new_df = pd.get_dummies(df.Name)
print(new_df)