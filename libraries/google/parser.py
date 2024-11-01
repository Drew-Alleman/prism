from libraries.google.google_classes import EmailLogEntry

import csv

class GoogleLogParser:
    def __init__(self):
        self.log_entries = []

    def read_export(self, filename: str) -> list:
        """
        Reads the CSV file and populates log entries with EmailLogEntry instances.
        :param filename: The Gmail Log search file to read
        """
        with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row.get("Message ID"):
                    entry = EmailLogEntry(row)
                    self.log_entries.append(entry)

        return self.log_entries
    
    def get_entries(self) -> list[EmailLogEntry]:
        """ 
        returns log entires loaded from GoogleLogParser.read_export()

        :return: a list of EmailLogEntry's
        """
        return self.log_entries
