# Contact Management System
# Stores name and phone number using a dictionary

contacts = {}   # name : phone_number


# Function to add a new contact
def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")


# Function to search for a contact by name
def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print("Contact not found.")


# Function to display all contacts
def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")


# Main Program Loop
while True:
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        add_contact(name, phone)

    elif choice == "2":
        name = input("Enter Name to Search: ")
        search_contact(name)

    elif choice == "3":
        display_contacts()

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid Choice! Try again.")
