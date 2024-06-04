#!/usr/bin/python3

""" This module converts XML to JSON """
import xml.estree.ElementTree as ET



def serialize_to_xml(dictionary, filename):
    """
    This Method converts JSON to XML format

    """

    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    This method converts xml to JSON
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    deserialized_dict = {}

    for child in root:
        deserialized_dict[child.tag] = child.text

    return deserialized_dict

