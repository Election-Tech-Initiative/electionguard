import json


def read_json_file(file_name: str) -> dict:
    """ opens a json file, return its content save in a dictionary
    try to open a given file name, raises no file found exception if not found
    :param file_name: file name
    :return a dictionary of json file content
    """
    try:
        file = open(file_name, 'r')
        values = json.load(file)
        file.close()
        return values
    except FileNotFoundError:
        print("file not found")
