#!/usr/bin/python3

""" This module uses pickle to serialize data """

import pickle



class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the CustomObject in the specified format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of CustomObject and save it to the specified filename.

        Parameters:
        filename (str): The name of the file to which the object will be serialized.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from the specified filename.

        Parameters:
        filename (str): The name of the file from which the object will be deserialized.

        Returns:
        CustomObject: The deserialized instance of CustomObject, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None

