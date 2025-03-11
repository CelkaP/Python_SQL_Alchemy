import csv


class CSVExporter:
    """Class to handle writing data from SQLAlchemy to a CSV file."""

    @staticmethod
    def write_to_csv(items, file_name):
        """
        Writes a list of dictionaries to a CSV file.
        :param items: A list of dictionaries containing data to write to CSV.
        :param file_name: Name of the CSV file to write data to.
        """
        if not items:
            print("Couldn't find any items to write to CSV.")
            return

        headers = items[0].keys()

        try:
            with open(file_name, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()
                writer.writerows(items)
            print(f"Data has been successfully written to {file_name}.")
        except Exception as e:
            print(f"Something went wrong while writing to a CSV file. \n{e}")
