OUTPUT:

![Figure_1](https://github.com/user-attachments/assets/c1f77b95-aedb-4218-8e4d-5ae055043b55)

Import Libraries:
The code imports necessary libraries: matplotlib.pyplot for plotting, pandas for data manipulation, and matplotlib.ticker for formatting tick labels.

Read CSV File:
The pd.read_csv() function reads a CSV file containing population data by age group into a Pandas DataFrame. The usecols parameter specifies the columns to read, which correspond to different age groups.

Convert Data to Numeric:
df.apply(pd.to_numeric) ensures that all values in the DataFrame are converted to numeric types, which is important for accurate calculations and plotting.

Calculate Total Population:
df.sum() computes the total population for each age group by summing the values across all rows of the DataFrame.

Print Data:
The print() statements display the age groups and their corresponding total population values for verification purposes.

Plot Data:
The plt.bar() function creates a bar chart with age groups on the x-axis and total population values on the y-axis. The bars are colored blue with black edges.
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}')) formats the y-axis labels to use commas as thousands separators and no decimal places.
Labels and title are added to the chart using plt.xlabel(), plt.ylabel(), and plt.title().

Display Plot:
plt.tight_layout() adjusts the layout to fit all elements within the plot area, ensuring labels and titles are properly positioned.
plt.show() displays the final plot.


