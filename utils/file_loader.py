import csv

def load_csv_test_cases(path_to_file: str):
    reader = csv.reader(open(path_to_file), delimiter=",", quotechar='"')
    data_read = [row for row in reader]
    return data_read
