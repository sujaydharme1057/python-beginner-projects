FILE_NAME = "contacts.txt"


# ---------------- LOAD CONTACTS ----------------

def load_contacts():
    contacts = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    name, number = line.split(",")
                    contacts[name] = number

    except FileNotFoundError:
        pass

    return contacts


# ---------------- SAVE CONTACTS ----------------

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, number in contacts.items():
            file.write(name + "," + number + "\n")


# ---------------- ADD CONTACT ----------------

def add_contact(contacts):
    name = input("Enter name: ").strip()
    number = input("Enter phone number: ").strip()

    if name in contacts:
        print("❌ Contact already exists!")
    else:
        contacts[name] = number
        save_contacts(contacts)
        print("✅ Contact added successfully!")


# ---------------- VIEW CONTACTS ----------------

def view_contacts(contacts):

    if not contacts:
        print("📭 No contacts found.")
        return

    print("\n----- CONTACTS -----")

    for i, (name, number) in enumerate(contacts.items(), start=1):
        print(f"{i}. {name} : {number}")


# ---------------- SEARCH CONTACT ----------------

def search_contact(contacts):

    name = input("Enter name to search: ").strip()

    if name in contacts:
        print(f"📞 {name} : {contacts[name]}")
    else:
        print("❌ Contact not found.")


# ---------------- DELETE CONTACT ----------------

def delete_contact(contacts):

    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("🗑️ Contact deleted successfully!")
    else:
        print("❌ Contact not found.")


# ---------------- MAIN PROGRAM ----------------

contacts = load_contacts()

while True:

    print("\n==========================")
    print("       CONTACT BOOK")
    print("==========================")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        view_contacts(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        delete_contact(contacts)

    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")