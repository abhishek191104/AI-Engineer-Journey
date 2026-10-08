import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#1.Read Dataset
df = pd.read_csv("Day-10/10.4_student_data.csv")
print(df)

#2.First Five Rows
print(df.head(5))

#3.Dataset Shape
print(df.shape)

#4.Information
print(df.info())

#5.Statistical Summary
print(df.describe())

#6.Check Missing Values
print(df.isnull().sum())

#7.Average Marks
print(df["Marks"].mean())

#8.Highest Marks
print(df["Marks"].max())

#9.Lowest Marks
print(df["Marks"].min())

#10.Find Student with Highest Marks
print(df[df["Marks"] == df["Marks"].max()])

#11.Marks Distribution
sns.histplot(df["Marks"], bins = 5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()

#12.Study Hours vs Marks
sns.scatterplot(
  data = df,
  x = "Hours_Studied",
  y = "Marks"
)
plt.title("Study Hours vs Marks")

plt.show()

#13.Attendance vs Marks
sns.scatterplot(
  data = df,
  x = "Attendance",
  y = "Marks"
)
plt.title("Attendance vs Marks")
plt.show()

#14.Marks by Gender
sns.boxplot(
  data = df,
  x = "Gender",
  y = "Marks"
)

plt.title("Marks by Gender")
plt.show()

#15.Marks by Study Hours
sns.barplot(
  data = df,
  x = "Hours_Studied",
  y = "Marks"
)
plt.title("Marks by Study Hours")
plt.show()