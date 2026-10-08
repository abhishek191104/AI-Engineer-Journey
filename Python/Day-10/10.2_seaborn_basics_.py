import seaborn as sns
import matplotlib.pyplot as plt

# 1. Scatter Plot
hours = [1, 2, 3, 4, 5, 6]
marks = [50, 55, 60, 68, 75, 85]

sns.scatterplot(x=hours, y=marks)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()


# 2. Histogram
marks = [
    45, 50, 55, 60, 62,
    65, 68, 70, 72, 75,
    78, 80, 82, 85, 90
]

sns.histplot(marks, bins=5)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.show()


# 3. Box Plot
sns.boxplot(x=marks)

plt.xlabel("Marks")
plt.title("Marks Distribution - Box Plot")
plt.show()


# 4. Study Hours vs Marks
sns.scatterplot(
    x=hours,
    y=marks[:6]
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()
