# main.py
#
# This is a console application that cleans, transforms, and merges contact data

import os

from utilities import clear_console

DATA_FOLDER = "../data/"
METADATA_CATELOG = "metadata.csv"

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