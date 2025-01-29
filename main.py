import matplotlib.pyplot as plt
import seaborn as sns
with open("road_accident_dataset.csv") as f:
    lines = f.readlines()

data = [line.strip().split(",") for line in lines]

print(data[0][0][0])