from csv import DictReader

from configs.settings import data_settings as ds


class CsvReader:

    def __init__(self, path: str, storage_name: str):
        self.path = path
        self.storage_name = storage_name

    def csv_reader(self) -> list[str]:
        with open(f"{self.path}/{self.storage_name}", "r") as file:
            reader = DictReader(file)
            column_name = reader.fieldnames[1]

            return [row[column_name] for row in reader]


if __name__ == "__main__":
    reader = CsvReader(path=ds.data_directory, storage_name=ds.csv_storage)
    print(reader.csv_reader())
