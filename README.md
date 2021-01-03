## clean-susans-contacts
A set of Python scripts to clean Sue's contact data

January 3, 2020

Bill McCann

### Summary
The follow tasks will complete this project

__Manual Steps__

1. Copy data to this project's /data folder. Sue has duplicate files, so only copy the originals.
2. Manually convert Excel workbooks to comma separated values, then remove the workbooks.
3. Create a metadata catelog. The metadata will be a table that contains a row for each file. The columns will be the file name followed by indices to map columns for First Name, Last Name, email address and phone number.

__Coding Steps__

4. Create a virtual environment
5. Create script to read metadata catelog into a simple list
7. Create a function to process all records in the list
6. Create a function to read data file
7. Create a function to map a row to new object
8. Create a function to update a dictionary
9. Create a function to write the dictionary to an output file

### Project Notes

The file personal_contacts-a5c6e0cf-7063-463d-a69a-3e373715d925-v1.csv has two rows for the column headings. I delete the first row.

The Garden State export has separate columns for street number and street name. Since there is no data in these columns I am not
going to bother writing code to deal with that.

The file personal_contacts-a5c6e0cf-7063-463d-a69a-3e373715d925-v1.csv has several phone numbers across multiple columns. For this data cleaning, I am only using two phone numbers. A quick scan shows that column L and O are the most frequently populated. I will use those.

#### Virtual Environment

__Create Virtual Environment__

The virtual environment was created using the following commands.

```bash
sudo apt-get update
sudo apt-get install python3-venv
python3 -m venv venv
```

### Running the Application

First start the Python virtual environment

```bash
source ./venv/bin/activate
```

