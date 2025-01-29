import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
with open("road_accident_dataset.csv") as f:
    lines = f.readlines()

data = [line.strip().split(",") for line in lines]
  
if(False):
    countries = [row[0] for row in data[1:]]
    country_counts = Counter(countries)
    country_names = list(country_counts.keys())
    country_accidents = list(country_counts.values())

    #create a barplot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=country_names, y=country_accidents, palette="viridis")
    plt.title("Number of Accidents by Country")
    plt.xticks(rotation=90)
    plt.ylabel("Number of Accidents")
    plt.tight_layout()

    plt.show()
elif(True):
    gender = [row[12] for row in data[1:]]
    gender_counts = Counter(gender)
    genders = list(gender_counts.keys())
    gender_accidents = list(gender_counts.values())

    plt.figure(figsize=(10, 6))
    sns.barplot(x=genders, y=gender_accidents, palette="viridis")
    plt.title("Gender")
    plt.xticks(rotation=90)
    plt.ylabel("Number of Accidents")
    plt.tight_layout()

    plt.show()


