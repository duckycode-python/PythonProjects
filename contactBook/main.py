import os
import json
contacts = []
def start():
    os.system('cls')
    print ("""
  ___  _____  _  _  ____   __    ___  ____    ____  _____  _____  _  _ 
 / __)(  _  )( \( )(_  _) /__\  / __)(_  _)  (  _ \(  _  )(  _  )( )/ )
( (__  )(_)(  )  (   )(  /(__)\( (__   )(     ) _ < )(_)(  )(_)(  )  ( 
 \___)(_____)(_)\_) (__)(__)(__)\___) (__)   (____/(_____)(_____)(_)\_)
""")
    global contacts
    contacts = [x for x in contacts if x]
    print ("""
    1. Contact list.
    2. Add new contact.
    3. Delete contact.
    4. Export contact list from file.
    5. Import contact list from file.
    """)
    task = input("(1/2/3/4/5) ")
    if task == "1":
        os.system('cls')
        contactlist()
    if task == "2":
        os.system('cls')
        addnew()
    if task == "3":
        os.system('cls')
        deletenumber()
    if task == "4":
        os.system('cls')
        exportlist()
    if task == "5":
        os.system('cls')
        importlist()
    else:
        print ("Error!")
        back()
def back():
    print("\nClick Enter to back")
    input()
    os.system('cls')
    start()
def contactlist():
    if len(contacts) == 0:
        print ("You don't have any contacts. Add some first.")
        back()
    else:
        for x in contacts:
            print("Name: ",x[0], " Number: ", x[1])
    back()    
def addnew():
    name = input("Name: ")
    number = input("Number(without spaces): ")
    if isinstance(number, int) and len(number) == 9:
        pass
    else:
        print("Number must be nine numeric and only numbers!")
        back()
    contacts.append([name, number])
    print("Contact succesfully created.")
    back()
def deletenumber():
    print("Who you want to delete?")
    nametodelete = input("Name: ")
    for x in contacts:
        if x[0] == nametodelete:
            x.clear()
    back()
def exportlist():
    print("What type of file you want to export?")
    print ("""
    1. txt
    2. json""")
    type = input("(1/2) ")
    print("What name for file?")
    filename = input("(without .json or .txt) ")
    if filename.isalpha():
        pass
    else:
        print("File name can contain only letters!")
        back()
    if type == "1":
        f = open(f"{filename}.txt", "w")
        for x in contacts:
            name = x[0]
            number = x[1]
            line = str(name + " " + number)
            f.write(line + "\n")
        f.close
        print("Succesfully exported contact list to numbers.txt.")
        back()
    elif type == "2":
        f = open(f"{filename}.json", "w")
        json.dump(contacts, f)
        f.close
        print("Succesfully exported contact list to numbers.json.")
        back()
    else:
        print ("Error!")
        back()
def importlist():
    global contacts
    if lose():
        os.system('cls')
        pass
    else:
        os.system('cls')
        start()
    print("What type of file you want to import?")
    print ("""
    1. txt
    2. json""")
    pick = input("(1/2) ")
    if pick == "1":
        contacts.clear()
        unorganised = []
        f = open("numbers.txt", "r")
        unorganised = f.readlines()
        unorganised = [x[:-1] for x in unorganised]
        for x in unorganised:
            name = x.split()[0]
            number = x.split()[1]
            if isinstance(number, int):
                pass
            else:
                print("Something went wrong! Did you edit file?")
                back()
            contacts.append([name, number])
        f.close
        back()
    elif pick == "2":
        contacts.clear()
        f = open("numbers.json", "r")
        contacts = json.load(f)
        print(contacts)
        f.close
        back()
    else:
        print ("Error!")
        back()
def lose():
    print("""If you import contacts from file you will lose previous! Even if import will go wrong!
    1. Agree 
    2. Disagree""")
    statement = input("(1/2) ")
    if statement == "1":
        return True
    elif statement == "2":
        os.system('cls')
        start()
    else:
        print ("Error!")
        back()
start()