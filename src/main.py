class ContactBook:
    """A class to manage contacts with their name, phone, and email information."""

    def __init__(self):
        """Initialize an empty contact book."""
        self.contacts = {}

    def add_contact(self, name, phone=None, email=None):
        """
        Add a new contact to the contact book.

        Args:
            name (str): The name of the contact.
            phone (str, optional): The phone number of the contact.
            email (str, optional): The email address of the contact.

        Returns:
            None
        """
        if name in self.contacts:
            print("Contact already exists!")
            return
        self.contacts[name] = {'phone': phone, 'email': email}

    def view_contacts(self):
        """Display all contacts in the contact book."""
        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print('-' * 40)

    def delete_contact(self, name):
        """
        Delete a contact from the contact book.

        Args:
            name (str): The name of the contact to delete.

        Returns:
            None
        """
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted")
        else:
            print("Contact does not exist")

    def update_contact(self, name, phone=None, email=None):
        """
        Update an existing contact's information.

        Args:
            name (str): The name of the contact to update.
            phone (str, optional): The new phone number.
            email (str, optional): The new email address.

        Returns:
            None
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print("Update successful")
        else:
            print("Contact not found")


def main():
    """Main function to run the contact book program."""
    contact_book = ContactBook()
    while True:
        print("""
        1. Add contact
        2. View contacts
        3. Update contact
        4. Delete contact
        5. Quit
        """)
        user_input = input('Please choose an option: ')
        
        if user_input == '5':
            break
        elif user_input == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contact_book.add_contact(name, phone, email)
        elif user_input == '2':
            contact_book.view_contacts()
        elif user_input == '3':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contact_book.update_contact(name, phone, email)
        elif user_input == '4':
            name = input("Name: ")
            contact_book.delete_contact(name)


if __name__ == "__main__":
    main()