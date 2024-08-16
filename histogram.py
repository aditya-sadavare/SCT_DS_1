import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker

df = pd.read_csv('C:\\Users\\adity\\Downloads\\population_by_age_group.csv', usecols=['65+',
                                                                                      '25-64 years',
                                                                                      '15-24 years',
                                                                                      '5-14 years',
                                                                                      '0-4 years'])


df = df.apply(pd.to_numeric)
total_population_by_age_group = df.sum()

print(total_population_by_age_group.index)
print(total_population_by_age_group.values)

plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.bar(total_population_by_age_group.index, total_population_by_age_group.values, color='blue',edgecolor='black')
plt.xlabel('Age Groups') 
plt.ylabel('Total Population')
plt.title('Total Population Distribution by Age Group')

plt.tight_layout()
plt.show()
