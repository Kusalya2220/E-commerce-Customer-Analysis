import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = Path("data/ecommerce_customers.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

print("E-COMMERCE CUSTOMER ANALYSIS")
print("\nDataset preview:")
print(df.head())

print("\nCustomer status counts:")
print(df["customer_status"].value_counts())

print("\nAverage order value by customer status:")
print(df.groupby("customer_status")["average_order_value"].mean().round(2))

print("\nTotal revenue by region:")
print(df.groupby("region")["total_spend"].sum().sort_values(ascending=False).round(2))

status_counts = df["customer_status"].value_counts()
status_counts.plot(kind="bar", title="Customers by Status", xlabel="Status", ylabel="Number of Customers")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "customers_by_status.png")
print("\nChart saved to outputs/customers_by_status.png")

region_revenue = df.groupby("region")["total_spend"].sum().sort_values(ascending=False)
region_revenue.plot(kind="bar", title="Total Spend by Region", xlabel="Region", ylabel="Total Spend")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "spend_by_region.png")
print("Chart saved to outputs/spend_by_region.png")
