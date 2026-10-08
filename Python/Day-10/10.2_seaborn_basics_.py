import seaborn as sns
import matplotlib.pyplot as plt

#1. Scatter Plot
tips = sns.load_dataset("tips")

sns.scatterplot(
  data = tips,
  x = "total_bill",
  y = "tip"
)

plt.show()

#2. Histogram
sns.histplot(
    data=tips,
    x="total_bill"
)

plt.show()

#3.Box Plot
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill"
)

plt.show()