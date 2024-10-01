import pandas as pd
import json

# Load JSON data from file with UTF-8 encoding
with open("data.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

# Convert JSON data to DataFrame
df = pd.DataFrame(json_data)

# Save DataFrame to Excel file
df.to_excel("output.xlsx", index=False)

print("JSON data has been successfully written to output.xlsx")
