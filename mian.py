import time
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt

lines = []

with open("road_accident_dataset.csv") as f:
    lines = f.readlines()

# Sample data
tips = sns.load_dataset("tips")

# Create a boxplot
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Boxplot of Total Bill by Day")
plt.show()
print("lmao")
