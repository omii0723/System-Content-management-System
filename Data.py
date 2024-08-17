import json
import os

# Define the file name where contacts will be stored
CONTACTS_FILE = "contacts.json"

# Load contacts from file if it exists, otherwise create an empty list
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")

# View all contacts
def view_contacts(contacts):
    if contacts:
        for index, contact in enumerate(contacts, start=1):
            print(f" Name: {contact['name']}")
            print(f" Phone: {contact['phone']}")
            print(f" Email: {contact['email']}")
    else:
        print("No contacts found.")

# Edit an existing contact
def edit_contact(contacts):
    view_contacts(contacts)
    if contacts:
        index = int(input("Enter the number of the contact you want to edit: ")) - 1
        if 0 <= index < len(contacts):
            print(f"Editing contact: {contacts[index]['name']}")
            contacts[index]['name'] = input("Enter new name: ")
            contacts[index]['phone'] = input("Enter new phone number: ")
            contacts[index]['email'] = input("Enter new email address: ")
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    if contacts:
        index = int(input("Enter the number of the contact you want to delete: ")) - 1
        if 0 <= index < len(contacts):
            removed_contact = contacts.pop(index)
            save_contacts(contacts)
            print(f"Contact {removed_contact['name']} deleted successfully!")
        else:
            print("Invalid contact number.")

# Main menu
def main_menu():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the program
if __name__ == "__main__":
    main_menu()

