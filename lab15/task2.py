import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("comptagevelo20152.csv", parse_dates=["Date"], dayfirst=True)
df['month'] = df['Date'].dt.month
monthly_totals = df.groupby("month").sum(numeric_only=True)

monthly_totals['Total'] = monthly_totals.sum(axis=1)
most_popular_month = monthly_totals['Total'].idxmax()
print(monthly_totals)
print(f"Найбільш популярний місяць у велосипедистів: {most_popular_month}")
monthly_totals = monthly_totals.drop(columns=['Total'])

monthly_totals.plot(xlabel="Місяць", ylabel="Відвідування", grid=True)
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.title("Використання велодоріжок за 2015 рік")
plt.show()