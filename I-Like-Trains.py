import pandas as pd
import re

def sanitise_data(file_path):
    with open ('resources/sanitised-data.csv', 'w') as sanitised_data:
        with open(file_path, 'r') as file:
            line = file.readline()
            while line != '':
                new_line = re.sub(",,+", "", line)
                sanitised_data.write(new_line)
                line = file.readline()

sanitise_data('resources/2324Qtr1Payments.csv')

df = pd.read_csv('resources/sanitised-data.csv')
print(df.to_string())
