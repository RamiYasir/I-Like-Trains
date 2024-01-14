def sanitise_data(file_path) -> None:
    with open ('resources/sanitised-data.csv', 'w') as sanitised_data:
        with open(file_path, 'r') as file:
            line = file.readline()
            while line != '':
                new_line = re.sub(",,+|\(|\)", "", line)
                sanitised_data.write(new_line)
                line = file.readline()