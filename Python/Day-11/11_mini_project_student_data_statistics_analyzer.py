import pandas as pd
import statistics

#1.Read the CSV using Pandas.
df = pd.read_csv("Day-11/11_student_marks.csv")
print(df)
marks = df["marks"]

#2. Calculate the mean, median, and mode of the marks column using the statistics module.
print("\nMean of the Marks:", statistics.mean(marks))
print("Median of Marks:", statistics.median(marks))
print("Mode of Marks:", statistics.mode(marks))

#3.Calculate population variance and standard deviation.
print("\nPopulation Variance of Marks:", statistics.pvariance(marks))
print("Population Standard Deviation of Marks:", statistics.pstdev(marks))

#4.Find the minimum and maximum marks.
print("\nMinimum Marks:", marks.min())
print("Maximum Marks:", marks.max())

#5.Calculate the 25th, 50th and 75th percentiles.
print("\n25th Percentile:", marks.quantile(0.25)) 
print("50th Percentile:", marks.quantile(0.50))
print("75th Percentile:", marks.quantile(0.75))

#6.Identify students scoring above the mean.
mean = statistics.mean(marks)
above_mean = df[df["marks"] > mean]

print("\nStudents scoring above the mean:")
print(above_mean)

#7.Exploratory correlation with row order
df["student_order"] = range(1, len(df) + 1)

print(
    "\nCorrelation with student order:",
      df["student_order"].corr(df["marks"]))