
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Create a PDF to save the visualizations
pdf = PdfPages("HR_Employee_Attrition_EDA.pdf")

# 1. Summary Statistics
summary = df.describe(include='all')
print(summary)

# 2. Attrition count plot
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Attrition', palette='Set2')
plt.title("Attrition Count")
pdf.savefig(); plt.close()

# 3. Lineplot: Age vs MonthlyIncome
df_sorted = df.sort_values(by="Age")
plt.figure(figsize=(10,6))
sns.lineplot(data=df_sorted, x='Age', y='MonthlyIncome', ci=None)
plt.title("Age vs Monthly Income")
pdf.savefig(); plt.close()

# 4. Lineplot: TotalWorkingYears vs MonthlyIncome
df_sorted2 = df.sort_values(by="TotalWorkingYears")
plt.figure(figsize=(10,6))
sns.lineplot(data=df_sorted2, x='TotalWorkingYears', y='MonthlyIncome', ci=None)
plt.title("Total Working Years vs Monthly Income")
pdf.savefig(); plt.close()

# 5. Correlation heatmap
plt.figure(figsize=(14,10))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt='.1f', cmap='coolwarm')
plt.title("Correlation Heatmap")
pdf.savefig(); plt.close()

# 6. Boxplot: MonthlyIncome by JobLevel
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='JobLevel', y='MonthlyIncome', palette='Set3')
plt.title("Monthly Income by Job Level")
pdf.savefig(); plt.close()

# Close the PDF
pdf.close()
