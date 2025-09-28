# STEP 1: Set up the contact dictionary
# Create an empty dictionary to store contacts
# Key = name, Value = phone number
contacts = {}

# STEP 2: Show menu in a loop
# Keep showing the menu until the user chooses to Exit
while True:
    # Print the main menu
    print("\n Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    # Take user input (menu choice)
    choice = input("Enter your choice (1–5): ")

    # ------------------------------
    # OPTION 1 → Add Contact
    # Add a new contact into the dictionary
    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        # Validate phone number (digits only)
        if not phone.isdigit():
            print("Phone number must contain only digits.")
        else:
            # Store contact with lowercase name as key
            contacts[name.lower()] = phone
            print("Contact added.")

    # ------------------------------
    # OPTION 2 → View All Contacts
    # Display all saved contacts
    elif choice == "2":
        print("\n All Contacts:")
        if not contacts:
            print("No contacts found.")  # If dictionary is empty
        else:
            # Loop through dictionary and print all contacts
            for name, phone in contacts.items():
                print(name.title(), "→", phone)

    # ------------------------------
    # OPTION 3 → Search Contact
    # Search for a specific contact by name
    elif choice == "3":
        search_name = input("Enter name to search: ").strip().lower()
        if search_name in contacts:
            print( search_name.title(), "→", contacts[search_name])
        else:
            print("Contact not found.")

    # ------------------------------
    # OPTION 4 → Delete Contact
    # Remove a contact from the dictionary
    elif choice == "4":
        del_name = input("Enter name to delete: ").strip().lower()
        if del_name in contacts:
            del contacts[del_name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    # ------------------------------
    # OPTION 5 → Exit Program
    # Break the loop and stop the program
    elif choice == "5":
        print("Exiting... Bye!")
        break

    # ------------------------------
    # Invalid Input Handling
    # If the user enters anything other than 1–5
    else:
        print("Invalid choice. Try again.")
