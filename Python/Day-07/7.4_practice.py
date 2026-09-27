'''import numpy as np

numbers = np.array([5, 10, 15, 20, 25])

print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))'''

import pandas as pd

Students = {
  "Name": ["Arun", "Ravi", "Priya", "Sneha"],
  "Age": [21, 22, 20, 23],
  "Marks": [80, 75, 92, 88]
}

df = pd.DataFrame(Students)
print(df["Marks"])
print(df[df["Marks"] > 80])
print("Mean:",df["Marks"].mean())