import pandas as pd
import re

def sanitise_data(file_path):
    with open ('resources/sanitised-data.csv', 'w') as sanitised_data:
        with open(file_path, 'r') as file:
            line = file.readline()
            while line != '':
                new_line = re.sub(",,+|\(|\)", "", line)
                sanitised_data.write(new_line)
                line = file.readline()


df = pd.read_csv('resources/sanitised-data.csv')


def total_expenses() -> float:
    total_spend = 0
    for expense in df['Net Amount']:
        float_expense = float(re.sub(",", "", expense))
        total_spend += float_expense
        # print(f"current expense: ${float_expense}, running exense: ${total_spend}")

    return total_spend

def get_all_distinct_entries(column: str):
    distinct_entries = []
    for entry in df[column]:
        if entry in distinct_entries:
            continue
        distinct_entries.append(entry)
    return distinct_entries

# print(df.to_string())
print(f'total expense are ${total_expenses()} in these service areas: ${get_all_distinct_entries("Service Area")}, to these suppliers: ${get_all_distinct_entries("Supplier Name")}')
