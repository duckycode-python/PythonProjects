from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Contact Book")
root.geometry("300x405")
contacts=[]
def destroyall():
    for widget in root.winfo_children():
       widget.destroy()
def back():
    global wiadomosc
    backButton = Button(root, text="Back", command=lambda: mainScreen())
    backButton.pack(anchor=CENTER)
    wiadomosc = ""

def mainScreen():
    destroyall()
    global contacts
    contacts = [x for x in contacts if x]
    buttonContactList = Button(root, text="Contact List", padx=30, pady=25, command=lambda: contactList())
    buttonContactList.grid(column=1, row=0, columnspan=1)
    buttonAddContact = Button(root, text="Add Contact", padx=30, pady=25, command=lambda: addContact())
    buttonAddContact.grid(column=1, row=1, columnspan=1)
    buttonDeleteContact = Button(root, text="Delete Contact", padx=30, pady=25, command=lambda: deleteContact())
    buttonDeleteContact.grid(column=1, row=2, columnspan=1)
    buttonExport = Button(root, text="Export Contacts", padx=30, pady=25)
    buttonExport.grid(column=1, row=3, columnspan=1)
    buttonImport = Button(root, text="Import Contacts", padx=30, pady=25)
    buttonImport.grid(column=1, row=4, columnspan=1)

def addContact():
    global wiadomosc
    global check
    global nameEntry
    global numberEntry
    destroyall()
    nameEntry = Entry(root)
    nameEntry.insert(0, "Write name here")
    nameEntry.pack(anchor=CENTER)

    numberEntry = Entry(root)
    numberEntry.insert(0, "Write number here")
    numberEntry.pack(anchor=CENTER)

    addContact = Button(root, text="Add contact", command=lambda: check())
    addContact.pack(anchor=CENTER)
    addContactLabel = Label(root, text=wiadomosc)
    addContactLabel.pack(anchor=CENTER)
    back()
    
def check():
    global wiadomosc
    name = nameEntry.get()
    number = numberEntry.get()
    if isinstance(number, int) and len(number) == 9:
        if len(name) <= 9:
            wiadomosc = ("Contact succesfully created.")
            contacts.append([name, number])
            addContact()
        else:
            wiadomosc = ("Too long name!")         
            addContact()
    else:
        wiadomosc = ("Number must be nine numeric and only numbers!")         
        addContact()
def contactList():
    global wiadomosc
    destroyall()
    if len(contacts) == 0:
        wiadomosc = ("You don't have any contacts. Add some first.")
        label = Label(root, text=wiadomosc)
        label.pack(anchor=CENTER)
        back()
    else:
        random = 1
        for x in contacts:
            contact = f"Name: {x[0]} | Number: {x[1]}"
            bgcolor = 0
            textcolor = 0
            if random % 2 == 0:
                bgcolor = "white"
                textcolor = "black"
            else:
                bgcolor = "black"
                textcolor = "white"
            label = Label(root, text=contact, bg=bgcolor, fg=textcolor)
            label.pack(anchor=CENTER)
            random += 1
            back()
def deleteContact():
    global wiadomosc
    destroyall()
    global nametodeleteEntry
    nametodeleteEntry = Entry(root)
    nametodeleteEntry.insert(0, "Contact name you want to delete")
    nametodeleteEntry.pack()
    Button(root, text="Delete", command=lambda: deleteLoop()).pack(anchor=CENTER)
    label = Label(root, text=wiadomosc)
    label.pack(anchor=CENTER)
    back()

def deleteLoop():
    global wiadomosc
    nametodelete = nametodeleteEntry.get()
    for x in contacts:
        if x[0] == nametodelete:
            response = messagebox.askyesno("Warning!", f"Are you sure u wanna delete contact named: {x[0]} with number {x[1]} ?")
            if response == 1:
                x.clear()
                wiadomosc = "Succesfully removed contact!"
                deleteContact()
        else:
            wiadomosc = "Unable to find contact!"
            deleteContact()
mainScreen()
root.mainloop()