# utilities.py
#
# Miscellaneous functions used by the application.
import csv

from os import system, name, path

DATA_FOLDER = "./data/"

def clear_console():
    """ clear the screen

    This function clears the terminal screen.

    There is no unittest coverage for this funciton.

    Args:
        None

    Returns:
        None
    """ 

	# for windows 
    if name == 'nt': 
        _ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def get_data(file_name):
    """ Load the data into a list

    Args:
        file_name    The name of the file containing the data (the ranked list)

    Returns:
        data         A list of items in ranked order
    """

    if not path.isfile(DATA_FOLDER + file_name): return []

    with open(DATA_FOLDER + file_name, mode = "r") as file:

        data = []
        first = True
        csvFile = csv.reader(file)
        for item in csvFile:
            if first:
                first = False
            else:
                data.append(item)

    return data

def save_data(data, file_name):
    """ Save the data into a csv file

    Args:
        data         A list containing the items to save
        file_name    The name of the file to contain the data
    Returns:
        Nothing
    """

    fields = [
        "email",
        "first-name",
        "last-name",
        "primary-phone",
        "other-phone",
        "street-address",
        "city",
        "state",
        "zip-code",
        "source-file"
    ]

    with open(DATA_FOLDER + file_name, "w") as file:
        write = csv.writer(file)
        write.writerow(fields)
        for item in data:
            write.writerow(item)
