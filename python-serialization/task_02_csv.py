#!/usr/bin/python3

"""
This module converts data from current file type to next
"""
import csv
import json


def convert_csv_to_json(csv_filename):
  """Converts a CSV file to JSON format.

  Args:
      csv_filename: The name of the CSV file to convert.

  Returns:
      True if the conversion was successful, False otherwise.
  """
    try:
        json_data = json.dumps(csv_filename)

        with open("data.json", "w") as f:
            f.write(json_data)
        return True
    except FileNotFoundError:
        return False

