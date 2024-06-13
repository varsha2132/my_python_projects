import random
import string
import sqlite3
import re
from tkinter import *
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class PasswordGeneratorGUI():
    def __init__(self, master):
        self.master = master
        self.password_length = IntVar()
        self.generated_password = StringVar()

        self.master.title('Password Generator')
        self.master.geometry('300x200')

        self.label = Label(self.master, text="Enter Password Length:")
        self.label.pack()

        self.length_entry = Entry(self.master, textvariable=self.password_length)
        self.length_entry.pack()

        self.generate_button = Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.generated_label = Label(self.master, textvariable=self.generated_password)
        self.generated_label.pack()

        


    def generate_password(self):
        try:
            length = self.password_length.get()
            if length <= 0:
                messagebox.showerror("Error", "Please enter a positive integer for password length.")
                return

            password = generate_password(length)
            self.generated_password.set("Generated Password: " + password)

            # Save to SQLite
            with sqlite3.connect("generated_passwords.db") as db:
                cursor = db.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS passwords(GeneratedPassword TEXT NOT NULL);")
                cursor.execute("INSERT INTO passwords(GeneratedPassword) VALUES(?);", (password,))
                db.commit()

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer for password length.")


       

if __name__ == "__main__":
    root = Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
