import tkinter as tk
from tkinter import messagebox

class ContactsSetup:
    def __init__(self):
        self.frame = None
        self.contacts = []

    def run(self, root, go_back_callback=None):
        self.clear_frame()
        self.frame = tk.Frame(root, bg="#f0f4f7")
        self.frame.pack(fill="both", expand=True)

        if go_back_callback:
            back_button = tk.Button(
                self.frame,
                text="\u2b05 Back",
                font=("Arial", 12),
                bg="#f0f4f7",
                fg="black",
                relief="flat",
                command=go_back_callback
            )
            back_button.pack(anchor="nw", padx=10, pady=10)

        self._add_label("Name")
        self.name_entry = self._add_entry()

        self._add_label("Email")
        self.email_entry = self._add_entry()

        self._add_label("Phone")
        self.phone_entry = self._add_entry()

        tk.Button(self.frame, text="Add Contact", command=self.add_contact, bg="#4caf50", fg="white").pack(pady=5)
        tk.Button(self.frame, text="Delete Selected", command=self.delete_contact, bg="#f44336", fg="white").pack(pady=5)

        self.contacts_listbox = tk.Listbox(self.frame, width=50, bg="white")
        self.contacts_listbox.pack(pady=10)

    def _add_label(self, text):
        label = tk.Label(self.frame, text=text, bg="#0a273d", font=("Arial", 10, "bold"))
        label.pack()

    def _add_entry(self):
        entry = tk.Entry(self.frame)
        entry.pack()
        return entry

    def add_contact(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name or not email or not phone:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        contact_str = f"{name} | {email} | {phone}"
        self.contacts.append(contact_str)
        self.contacts_listbox.insert(tk.END, contact_str)
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def delete_contact(self):
        selected = self.contacts_listbox.curselection()
        if not selected:
            messagebox.showinfo("Delete Contact", "Please select a contact to delete.")
            return

        index = selected[0]
        self.contacts_listbox.delete(index)
        del self.contacts[index]

    def clear_frame(self):
        if self.frame is not None:
            self.frame.destroy()