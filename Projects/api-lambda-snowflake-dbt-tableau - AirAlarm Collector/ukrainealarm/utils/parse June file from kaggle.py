import json
import pandas as pd
with open('airalert_20240601_20240630.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)
#df['where'] = df['text'][0][0]['text'] #where the air alarm
for e in range(len(df)):
    #print(e)
    #print(df['text'][e][0]['text'])
    df['where'] = df['text'][e][0]['text'] #where the air alarm
    print(df['where'])
#print(df)
# 
# 
#print(df['text'][4873])