import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("covid_data.csv")
#print(df)

has_null = df.isnull().any()
print(has_null)
#columns present
print(df[["Country_Region", "Confirmed","Deaths", "Recovered"]])


x = df[["Country_Region", "Confirmed", "Recovered"]].sort_values(by = "Confirmed", ascending = False)
print(x.head(10))


#bar plot

# plt.bar(["Confirmed", ""], [90, 95])
# plt.show()


x.plot(kind='bar', x='Country_Region', y='Confirmed', color='lightblue', title='Top 10 Countries with Highest Confirmed COVID-19 Cases', legend=False,  width=2)
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.show()
