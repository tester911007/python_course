import pandas as pd

link = "https://stepik.org/media/attachments/lesson/245267/salaries.xlsx"
file = pd.read_excel(link, index_col=0)

print(file.median(axis=1).sort_values())
print(file.mean(axis=0).sort_values())
