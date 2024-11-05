# Contact class to represent each contact
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"


# Function to display the menu
def show_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Function to add a new contact
def add_contact(contact_list):
    print("\n--- Add a New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    new_contact = Contact(name, phone, email, address)
    contact_list.append(new_contact)
    print(f"Contact {name} added successfully!")

# Function to view all contacts
def view_contacts(contact_list):
    if len(contact_list) == 0:
        print("\nNo contacts found.")
    else:
        print("\n--- Your Contact List ---")
        for idx, contact in enumerate(contact_list, start=1):
            print(f"{idx}. {contact}")

# Function to search contacts by name or phone
def search_contact(contact_list):
    search_term = input("\nEnter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contact_list if search_term in contact.name.lower() or search_term in contact.phone]

    if not found_contacts:
        print("\nNo matching contacts found.")
    else:
        print("\n--- Search Results ---")
        for contact in found_contacts:
            print(contact)

# Function to update a contact's details
def update_contact(contact_list):
    view_contacts(contact_list)
    try:
        index = int(input("\nEnter the number of the contact you want to update: ")) - 1
        if 0 <= index < len(contact_list):
            contact = contact_list[index]
            print(f"\nUpdating contact: {contact.name}")

            # Ask for new details
            contact.name = input(f"Enter new name (current: {contact.name}): ") or contact.name
            contact.phone = input(f"Enter new phone (current: {contact.phone}): ") or contact.phone
            contact.email = input(f"Enter new email (current: {contact.email}): ") or contact.email
            contact.address = input(f"Enter new address (current: {contact.address}): ") or contact.address

            print(f"\nContact {contact.name} updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to delete a contact
def delete_contact(contact_list):
    view_contacts(contact_list)
    try:
        index = int(input("\nEnter the number of the contact you want to delete: ")) - 1
        if 0 <= index < len(contact_list):
            deleted_contact = contact_list.pop(index)
            print(f"\nContact {deleted_contact.name} deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main function to run the contact management system
def run_contact_management_system():
    contact_list = []  # List to store all contacts
    while True:
        show_menu()
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            add_contact(contact_list)
        elif choice == '2':
            view_contacts(contact_list)
        elif choice == '3':
            search_contact(contact_list)
        elif choice == '4':
            update_contact(contact_list)
        elif choice == '5':
            delete_contact(contact_list)
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-6).")

# Run the program
if __name__ == "__main__":
    run_contact_management_system()
