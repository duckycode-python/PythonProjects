import json
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pathlib
from tkinter import filedialog as fd

from numpy import integer, isin
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
    buttonExport = Button(root, text="Export Contacts", padx=30, pady=25, command=lambda: exportContact())
    buttonExport.grid(column=1, row=3, columnspan=1)
    buttonImport = Button(root, text="Import Contacts", padx=30, pady=25, command=lambda: importContact())
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
    number = int(numberEntry.get())
    if isinstance(number, int) and len(str(number)) == 9:
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
    Label(root, text=wiadomosc).pack()
    back()

def deleteLoop():
    global wiadomosc
    global contacts
    instance = False
    nametodelete = nametodeleteEntry.get()
    contacts = [x for x in contacts if x]
    for x in contacts:
        if x[0] == nametodelete:
            response = messagebox.askyesno("Warning!", f"Are you sure u wanna delete contact named: {x[0]} with number {x[1]} ?")
            if response == 1:
                x.clear()
                wiadomosc = "Succesfully removed contact!"
                deleteContact()
            else:
                mainScreen()
        else:
            pass
    for x in contacts:
        if x[0] == nametodelete:
            deleteLoop()
        else:
            instance = False
    if instance == False:
        wiadomosc = "Unable to find contact"
        deleteContact()
    else:
        wiadomosc = "Error"
        deleteContact()
def exportContact():
    global pathtosave
    global v
    v = IntVar()
    destroyall()
    Label(root, text="Click button below to choose folder").pack(anchor=CENTER)
    Button(root, text="click", command=lambda: selectFolderExport()).pack(anchor=CENTER)
    back()
    Label(root, text=f"Path to selected folder:\n{pathtosave}").pack()
    Label(root, text="\n What file type?").pack()
    Radiobutton(root, text=".json", value=1, variable=v).pack()
    Radiobutton(root, text=".txt", value=2,variable=v).pack()
    Button(root, text="Export", command=lambda: exportFileSave()).pack()

def selectFolderExport():
    global pathtosave
    pathtosave = filedialog.askdirectory()
    exportContact()

def exportFileSave():
    global v
    global contacts
    global pathtosave
    if v.get() == 2:
        f = open(f"{pathtosave}/contacts.txt", "w")
        for x in contacts:
            name = x[0]
            number = x[1]
            line = (str(name) + " " + str(number))
            f.write(line + "\n")
        f.close
        messagebox.showinfo(title="Succesfully", message=f"Succesfully exported contact list to contacts.txt.")
        back()
    elif v.get() == 1:
        f = open(f"{pathtosave}/contacts.json", "w")
        json.dump(contacts, f)
        f.close
        messagebox.showinfo(title="Succesfully", message=f"Succesfully exported contact list to contacts.json.")
        back()
def importContact():
        destroyall()
        global filename
        global contacts
        Label(root, text="Click button belove to select file.").pack()
        Button(root, text="click", command=lambda: pathtosaveImport()).pack(anchor=CENTER)
        back()
        filetype = pathlib.Path(f"{filename}").suffix
        if filetype == ".txt":
            contacts.clear()
            unorganised = []
            f = open(f"{filename}", "r")
            unorganised = f.readlines()
            unorganised = [x[:-1] for x in unorganised]
            for x in unorganised:
                name = x.split()[0]
                number = x.split()[1]
                if isinstance(number, integer):
                    contacts.append([name, number])
                else:
                    Label(root, text="Something went wrong! Did you edit file?").pack()
                    importContact()
            Label(root, text="Succesfully imported contacts!").pack()
            f.close
        elif filetype == ".json":
            contacts.clear()
            f = open(f"{filename}", "r")
            contacts = json.load(f)
            print(contacts)
            f.close
            back()
        else:
            Label(root, text="Error! Wrong file type.").pack()
def pathtosaveImport():
    global filename
    response = messagebox.askyesno("Warning!", "You will lose your curent contact list. Even if import will be unsuccesfully")
    if response == 1:
        filename = fd.askopenfilename()
    else:
        mainScreen()
    importContact()
mainScreen()
root.mainloop()