# main.py
#
# This is a console application that cleans, transforms, and merges contact data

import os

from utilities import clear_console, get_data, save_data

METADATA_CATELOG = "metadata.csv"
MERGED_DATA = "clean_contacts.csv"
contact_db = dict()

def update_dictionary(contact):

    email = contact[0]
    if email in contact_db.keys():
        db_contact = contact_db[email]
        for i in range(1, 9):
            db_contact[i] = contact[i] if db_contact[i] is None else db_contact[i]
        contact_db[email] = db_contact
    else:
        contact_db[email] = contact

def map_contact(metadata_item, contact_item):

    new_contact = [ contact_item[int(metadata_item[i])] for i in [4, 2, 3, 5, 6, 7, 8, 9, 10] ]
    new_contact.append(metadata_item[0])
    update_dictionary(new_contact)
    return new_contact

def process_file(metadata_item):

    data = get_data(metadata_item[0])
    print("Number of records in {file} is {count}".format(file=metadata_item[0], count=len(data)))
    [map_contact(metadata_item, item) for item in data]
    return True

if __name__ == "__main__":

    clear_console()
    print('\n-----------------------------------------------------------------------')
    print('This is a one-off special data cleaning program.')
    print('Use this to transform and dedupe contact files in .csv format')
    print('This program will create a single contact file using email address as')
    print('the primary key. The following fields are mapped into the single contact file.')
    print('')
    print('- Email Address')
    print('- First Name')
    print('- Last Name')
    print('- Primary Phone')
    print('- Other Phone')
    print('- Street Address')
    print('- City')
    print('- State')
    print('- Zip Code')
    print('')
    print('copyright William McCann 2021')
    print('-----------------------------------------------------------------------')

    metadata = get_data(METADATA_CATELOG)
    [process_file(item) for item in metadata]

    contacts = [contact_db[item] for item in contact_db]
    save_data(contacts, MERGED_DATA)
