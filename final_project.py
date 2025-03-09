import sys
sys.stdout.reconfigure(encoding='utf-8')

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Step 1: Read the CSV file
df = pd.read_csv("data1.csv")

# Step 2: Data Analysis
average_age = df["Age"].mean()
average_salary = df["Salary"].mean()

# Step 3: Bar Chart - Salary Distribution
plt.figure(figsize=(10,5))
plt.bar(df["Name"], df["Salary"], color='skyblue')
plt.xlabel("Names")
plt.ylabel("Salary")
plt.title("Salary Distribution")
plt.xticks(rotation=90)
plt.savefig("salary_chart.png")
plt.close()

# Step 4: Pie Chart - Age Distribution
plt.figure(figsize=(7,7))
plt.pie(df["Age"], labels=df["Name"], autopct="%1.1f%%", startangle=140)
plt.title("Age Distribution")
plt.savefig("age_pie_chart.png")
plt.close()

# Step 5: Generate PDF Report
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "Data Analysis Report", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.cell(200, 10, f"Average Age: {average_age:.2f}", ln=True)
pdf.cell(200, 10, f"Average Salary: {average_salary:.2f}", ln=True)
pdf.ln(10)

# Add Bar Chart to PDF
pdf.image("salary_chart.png", x=10, w=180)
pdf.ln(10)

# Add Pie Chart to PDF
pdf.image("age_pie_chart.png", x=35, w=140)

# Save PDF Report
pdf.output("report.pdf")


print("✅ Report generated: report.pdf".encode("utf-8").decode("utf-8"))
