from tkinter import *
root = Tk()
root.title("Contact Book")
root.geometry("300x405")


def mainScreen():
    buttonContactList = Button(root, text="Contact List", padx=30, pady=25)
    buttonContactList.grid(column=1, row=0, columnspan=1)
    buttonAddContact = Button(root, text="Add Contact", padx=30, pady=25, command=lambda: addContact())
    buttonAddContact.grid(column=1, row=1, columnspan=1)
    buttonDeleteContact = Button(root, text="Delete Contact", padx=30, pady=25)
    buttonDeleteContact.grid(column=1, row=2, columnspan=1)
    buttonExport = Button(root, text="Export Contacts", padx=30, pady=25)
    buttonExport.grid(column=1, row=3, columnspan=1)
    buttonImport = Button(root, text="Import Contacts", padx=30, pady=25)
    buttonImport.grid(column=1, row=4, columnspan=1)











mainScreen()
root.mainloop()