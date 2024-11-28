#!/usr/bin/env python3
"""
This class contains the class for accessing the json file
"""
import json
from os import path
from uuid import uuid4


class JSONDB:
    """
    JSON Database Class
    """
    def __init__(self):
        pass

    def read_json(self, json_file):
        """
        Read data from the JSON file.
        """
        try:
            with open(json_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"Error": "File not found!"}
        except json.JSONDecodeError:
            return {"Error": "JSONDecodeError"}

    def write_json(self, data, json_file):
        """
        Write data to the JSON file as an array of dictionaries.
        """
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        # Check if file exists and load existing data if present, else create an empty list
        if path.exists(json_file):
            with open(json_file, 'r') as file:
                try:
                    file_data = json.load(file)
                    if not isinstance(file_data, list):
                        file_data = []
                except json.JSONDecodeError:
                    file_data = []
        else:
            file_data = []

        # Append the new dictionary data
        data['id'] = str(uuid4())
        file_data.append(data)

        # Write the updated list back to the file
        with open(json_file, 'w') as file:
            json.dump(file_data, file, indent=4)

jsondb = JSONDB()