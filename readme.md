# Contact Book Application

## Description
This Contact Book application is a simple command-line program written in Python. It allows users to manage their contacts by adding, viewing, updating, and deleting contact information.

## Features
- Add new contacts with name, phone number, and email address
- View all stored contacts
- Update existing contact information
- Delete contacts
- Simple command-line interface

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Download the `contact_book.py` file.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing `contact_book.py`.
3. Run the script using Python:
   ```
   python contact_book.py
   ```
4. Follow the on-screen prompts to manage your contacts.

## Menu Options
1. Add contact: Add a new contact to the book.
2. View contacts: Display all stored contacts.
3. Update contact: Modify information for an existing contact.
4. Delete contact: Remove a contact from the book.
5. Quit: Exit the application.

## Data Structure
Contacts are stored in memory as a dictionary. Each contact is represented by a nested dictionary containing 'phone' and 'email' keys.

## Limitations
- Data is not persistent and will be lost when the program is closed.
- No data validation is performed on user inputs.

## Future Improvements
- Implement data persistence (e.g., saving to a file or database)
- Add input validation for phone numbers and email addresses
- Implement a search function
- Add support for additional contact fields (e.g., address, birthday)

