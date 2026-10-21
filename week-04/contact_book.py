contacts = {}

#Adding a new contact to the contact book - Dictionary
def add_contact():
    name = input ("Enter contact name: ").strip()
    phone = input ("Enter contact phone number: ").strip()
    email = input ("Enter contact email address: ").strip()

    if not name:
        print("Contact name cannot be empty.")
        return

    if name in contacts:
        print(f"Contact {name} already exists.")
        return

    contacts[name] = {
        "phone": phone, 
     "email": email
     }
    
    print(f"Contact {name} added with phone number {phone} and email {email}.") 


#Viewing the contacts in the contact book  - Dictionary
def view_contacts():
    print("\n--- All Contacts ---")

    if not contacts:
        print("No contacts found.")
        return

    #convert dictionary keys to a list and sort them
    sorted_names = sorted(contacts.keys())
    
    for name in sorted_names:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")


# Searching for a contact in the contact book - Dictionary
def search_contact():
    print("\n--- Search Contact ---")

    name = input("Enter contact name to search: ").strip()

    if not name:
        print("Contact name cannot be empty.")
        return

    if name not in contacts:
        print(f"Contact {name} not found.")
        return

    print(f"Contact found: {name}")
    print(f"Phone: {contacts[name]['phone']}")
    print(f"Email: {contacts[name]['email']}")




# Updating an existing contact in the contact book - Dictionary
def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter contact name to update: ").strip()

    if not name:
        print("Contact name cannot be empty.")
        return

    if name not in contacts:
        print(f"Contact {name} not found.")
        return

    if name in contacts:
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email address (leave blank to keep current): ").strip()

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email

        print(f"Contact {name} updated.")
    
    else:
        print(f"Contact {name} not found.")

# Deleting a contact from the contact book - Dictionary
def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter contact name to delete: ").strip()

    if not name:
        print("Contact name cannot be empty.")
        return

    if name not in contacts:
        print(f"Contact {name} not found.")
        return

    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print(f"Contact {name} not found.")

#Display Contact Summary - Tuple
def display_contact_summary():
    print("\n--- Contact Summary ---")

    name = input("Enter contact name to view summary: ").strip()

    if name not in contacts:
        print(f"Contact {name} not found.")
        return

    contact_summary = (
        name,
        contacts[name]["phone"],
        contacts[name]["email"]
    )

    print(f"Contact Summary for {contact_summary[0]}:")
    print(f"Contact Name: {contact_summary[0]}")
    print(f"Phone: {contact_summary[1]}")
    print(f"Email: {contact_summary[2]}")


# Displaying unique email addresses from the contact book - Set
def display_unique_emails():
    print("\n--- Unique Email Addresses ---")

    if not contacts:
        print("No contacts found.")
        return

    unique_emails = set(contact["email"] for contact in contacts.values())
    
    for email in unique_emails:
        print(email)

# Main menu for the contact book application
def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Display Contact Summary")
        print("7. Display Unique Emails")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            display_contact_summary()
        elif choice == "7":
            display_unique_emails()
        elif choice == "8":
            print("Exiting the contact book application.")
            break
        else:
            print("Invalid choice. Please try again. Enter a number between 1 and 8.")


if __name__ == "__main__":
            main()