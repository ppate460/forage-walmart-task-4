import csv


def read_csv_file(file_path):

    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row_num, row in enumerate(csv_reader, start=1):
            print(f"Row {row_num}: {row}")


if __name__ == "__main__":
    # Change the name of the file to "shipping_data_0.csv" or 1 or 2, to view the data
    file_path = 'shipping_data_0.csv'
    read_csv_file(file_path)

