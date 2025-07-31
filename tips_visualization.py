import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

sns.barplot(x="day", y="tip", data=df)
plt.title("Bar plot – Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Tip")
plt.tight_layout()
plt.show()

sns.lineplot(x="total_bill", y="tip", data=df)
plt.title("Line plot – Tip vs. Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.tight_layout()
plt.show()

df["sex"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90)
plt.title("Pie chart – Gender Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Heatmap – Correlation Heatmap")
plt.tight_layout()
plt.show()

sns.boxplot(x="sex", y="tip", data=df)
plt.title("Box plot – Tip Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Tip")
plt.tight_layout()
plt.show()
