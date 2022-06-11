import csv
from pathlib import Path

_FOLDER_PATH = Path(__file__).parent.resolve()
_DATA_PATH = Path.joinpath(_FOLDER_PATH, "data")
_CSV1 = Path.joinpath(_DATA_PATH, "class1.csv")
_CSV2 = Path.joinpath(_DATA_PATH, "class2.csv")
_RESULT = Path.joinpath(_DATA_PATH, "all_classes.csv")


def merge_csv(csv_list, output_path):
    # build list with all fieldnames
    fieldnames = list()
    for file in csv_list:
        with open(file, "r") as input_csv:
            fn = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(x for x in fn if x not in fieldnames)

    # write data to output file based on field names
    with open(output_path, "w", newline="") as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, "r") as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)


if __name__ == "__main__":
    merge_csv([_CSV1, _CSV2], _RESULT)
