import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Study_Hours": [2, 3, 4, 5, 6],
    "Marks": [45, 55, 65, 75, 90]
}

df = pd.DataFrame(data)

sns.scatterplot(
    x="Study_Hours",
    y="Marks",
    data=df
)

plt.title("Study Hours vs Marks")

plt.show()