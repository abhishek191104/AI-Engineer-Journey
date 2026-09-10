contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"Contact '{name}' added successfully!")

    elif choice == "2":
        name = input("Enter contact name to search: ")
        if name in contacts:
            print(f"Name: {name} | Phone: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "4":
        if contacts:
            print("\n--- All Contacts ---")
            for name, phone in contacts.items():
                print(f"Name: {name} | Phone: {phone}")
        else:
            print("No contacts available.")

    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")