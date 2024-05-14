import pandas as pd
import os
import glob



def read_all_files()-> pd.DataFrame:
   
    # read all files from "./pandas etls/Sales_Data/" directory
    # with .csv extention
    all_files = glob.glob(os.path.join("./pandas etls/Sales_Data/", "*.csv"))

    # concatenate all files into one 
    df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

    return df

df_with_nans = read_all_files()

# #create a mask to idintify NaNs
# df = df_with_nans[df_with_nans.isna().any(axis=1)]
# #show rows with NaNs
# print(df.head(100))


#remove NaNs
df = df_with_nans.dropna(how="all")

#remove redundant headers from file`s content (not the table header)
df = df[df['Order Date'].str[0:2] != 'Or']

# add Month coulmn and convert Month 05 to Month  5
df['Month'] = df['Order Date'].str[0:2]
df['Month'] = df['Month'].astype('int32') 


# add Sales column
df['Quantity Ordered'] = df['Quantity Ordered'].astype('int64') 
df['Price Each'] = df['Price Each'].astype('float') 
df['Sales'] = df['Quantity Ordered'] * df['Price Each']


#print(df.dtypes)
print(df.head())