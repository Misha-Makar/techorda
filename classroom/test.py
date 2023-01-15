import pandas as pd

df = pd.read_excel(r'mid.xlsx')
df = pd.DataFrame(df, columns=['city'])
print(df)
lst = []
for col in df['city']:
    lst.append(col)

from collections import Counter
print(len(Counter(lst)))




