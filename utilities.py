import pandas as pd
import matplotlib as mpl
import re
from collections import Counter, defaultdict

def total_expenses(df: pd.DataFrame) -> float:
    total_spend = 0
    for expense in df['Net Amount']:
        float_expense = float(re.sub(",", "", expense))
        total_spend += float_expense

    return total_spend

 
def get_all_distinct_entries(df: pd.DataFrame, column: str) -> list:
    distinct_entries = []
    for entry in df[column]:
        if entry in distinct_entries:
            continue
        distinct_entries.append(entry)
    return distinct_entries


def sort_suppliers_by_service_area(df: pd.DataFrame) -> dict:
    service_to_supplier = {service: [] for service in get_all_distinct_entries(df, "Service Area")}
    for supplier in get_all_distinct_entries(df, "Supplier Name"):
        row = df.loc[df["Supplier Name"] == supplier].iloc[0]
        service_value = row["Service Area"]
        supplier_value = row["Supplier Name"]

        if supplier_value in service_to_supplier[service_value]:
            continue
        service_to_supplier[service_value].append(supplier_value)

    return service_to_supplier


def total_expenses_per_supplier(df: pd.DataFrame, supplier: str):
    results = df.loc[df["Supplier Name"] == supplier]
    total_expense = total_expenses(results)

    return total_expense
