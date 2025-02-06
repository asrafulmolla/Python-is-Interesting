import seaborn as sns
import matplotlib.pyplot as plt

# Load the "tips" dataset
data = sns.load_dataset("tips")

# Set figure size
plt.figure(figsize=(10, 4))

# Create a violin plot for the "total_bill" column
sns.violinplot(x=data["total_bill"])

# Show the plot
plt.show()
