from db.scripts.dql_scripts import DQL
from src.csv import CSVExporter

def main():
    rows = DQL.retrieve_all_items_as_dict()
    CSVExporter.write_to_csv(rows, "db_output.csv")


if __name__ == "__main__":
    main()