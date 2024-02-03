import sqlite3

class ContactManager:
    def __init__(self):
        self.conn = sqlite3.connect("contacts.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            phone TEXT,
                            email TEXT,
                            address TEXT)''')
        self.conn.commit()

    def add_contact(self, name, phone, email, address):
        self.cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                            (name, phone, email, address))
        self.conn.commit()

    def view_contacts(self):
        self.cursor.execute("SELECT id, name, phone FROM contacts")
        contacts = self.cursor.fetchall()
        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Phone: {contact[2]}")
        print()

    def search_contact(self, search_term):
        self.cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?",
                            (f"%{search_term}%", f"%{search_term}%"))
        result = self.cursor.fetchall()
        return result

    def update_contact(self, contact_id, name, phone, email, address):
        self.cursor.execute("UPDATE contacts SET name=?, phone=?, email=?, address=? WHERE id=?",
                            (name, phone, email, address, contact_id))
        self.conn.commit()

    def delete_contact(self, contact_id):
        self.cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


def main():
    contact_manager = ContactManager()

    while True:
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)

        elif choice == "2":
            print("Contact List:")
            contact_manager.view_contacts()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            result = contact_manager.search_contact(search_term)
            if result:
                for contact in result:
                    print(contact)
            else:
                print("No matching contacts found.")

        elif choice == "4":
            contact_manager.view_contacts()
            contact_id = input("Enter the ID of the contact you want to update: ")
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_manager.update_contact(contact_id, name, phone, email, address)

        elif choice == "5":
            contact_manager.view_contacts()
            contact_id = input("Enter the ID of the contact you want to delete: ")
            contact_manager.delete_contact(contact_id)

        elif choice == "6":
            contact_manager.close_connection()
            print("Exiting the Contact Manager.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
