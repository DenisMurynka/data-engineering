import json
import pandas as pd

# Load the JSON data
with open('airalert_20240601_20240630.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the required fields
extracted_data = []
for item in data:
    date = item.get('date')
    text_entries = item.get('text', [])
    first_text_subobject = None

    # Extract the first sub-object with type 'bold' from the 'text' list
    for sub_item in text_entries:
        if isinstance(sub_item, dict) and sub_item.get('type') == 'bold':
            first_text_subobject = sub_item.get('text')
            break

    extracted_data.append({
        'date': date,
        'first_text_subobject': first_text_subobject
    })

# Create DataFrame
df = pd.DataFrame(extracted_data)

# Add a new column to store the end action date
df['end_action_date'] = None

# Iterate through the DataFrame to find the corresponding end action date for each start action
for i in range(len(df)):
    start_action = df.loc[i, 'first_text_subobject']
    if start_action and "Повітряна тривога в" in start_action:
        region = start_action.split(" в ")[-1]
        for j in range(i + 1, len(df)):
            end_action = df.loc[j, 'first_text_subobject']
            if end_action and f"Відбій тривоги в {region}" in end_action:
                df.loc[i, 'end_action_date'] = df.loc[j, 'date']
                break

# Display the DataFrame
print(df)

df.to_csv('op.csv', sep='\t', encoding='utf-8')