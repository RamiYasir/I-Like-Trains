import pandas as pd
import re

df = pd.read_csv('resources/sanitised-data.csv')
df.reset_index()

def total_expenses() -> float:
    total_spend = 0
    for expense in df['Net Amount']:
        float_expense = float(re.sub(",", "", expense))
        total_spend += float_expense

    return total_spend


def get_all_distinct_entries(column: str) -> list:
    distinct_entries = []
    for entry in df[column]:
        if entry in distinct_entries:
            continue
        distinct_entries.append(entry)
    return distinct_entries



def sort_suppliers_by_service_area() -> dict:
    service_to_supplier = {service: [] for service in get_all_distinct_entries("Service Area")}
    for supplier in get_all_distinct_entries("Supplier Name"):
        row = df.loc[df["Supplier Name"] == supplier].iloc[0]
        service_value = row["Service Area"]
        supplier_value = row["Supplier Name"]

        if supplier_value in service_to_supplier[service_value]:
            continue
        service_to_supplier[service_value].append(supplier_value)

    return service_to_supplier
            

nice_dictionary = sort_suppliers_by_service_area()
print(f"${nice_dictionary.popitem()} \n\n\n") 
print(nice_dictionary.popitem())