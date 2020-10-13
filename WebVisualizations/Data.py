import pandas as pd

# Import cities.csv using Pandas to read 
# and then convert the file into HTML

#Returns "data.html" into the WebVisualizations folder


df = pd.read_csv('Resources/cities.csv')
df.to_html('data.html', index=False)
table = df.to_html()
print(table)