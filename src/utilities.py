# utilities.py
#
# Miscellaneous functions used by the application.
from os import system, name

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
