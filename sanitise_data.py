import re
from pathlib import Path

def sanitise_data(file_path) -> None:
    # reminder to refactor.
    path = Path(file_path)
    path_without_extension = path.with_suffix('')
    split_values = re.split("/", path_without_extension.as_posix())
    print(split_values)
    
    with open (f'resources/sanitised-data-{split_values[1]}.csv', 'w') as sanitised_data:
        with open(file_path, 'r', errors='replace') as file:
            line = file.readline()
            while line != '':
                new_line = re.sub(",,+|\(|\)", "", line)
                sanitised_data.write(new_line)
                line = file.readline()

# being lazy and just calling it on each file
sanitise_data("resources/2223Qtr4Payments.csv")