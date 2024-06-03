#!/usr/bin/python3

"""
This module turns an object or data structure to a json file
"""
import json



def serialize_and_save_to_file(data, filename):
    """

    Serialize a Python dictionary to a JSON file.

    Perameters:
    data (dict): A python dictionary
    filename (str): A file that contains data in JSON format.
    """

    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    
    Load and deserialize data from JSON file to dictionary

    Parameters:
    filename (str): A json file to be deserialized
    
    Returns:
    dict: A python dictionary.
    """

    with open(filename,'r') as file:
        data = json.load(file)
    return data
