#!/usr/bin/python3

"""
This module converts data from current file type to next
"""
import csv
import json



def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON format.
    Args:
      csv_filename: The name of the CSV file to convert.

    Returns:
        True if the conversion was successful, False otherwise
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        return False

