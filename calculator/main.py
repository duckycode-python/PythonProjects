from tkinter import *
root = Tk()

e = Entry(root, width=50)
e.grid(row=0, column=0, columnspan=3)

def buttonclick(number):
    e.insert(0, str(number))

def buttonPlus():
    global math
    global firstnumber
    firstnumber = e.get()
    e.delete(0, END)
    math = "+"
def buttonEqual():
    secondnumber = e.get()
    e.delete(0, END)
    if math == "+":
        answer = int(firstnumber) + int(secondnumber)
        e.delete(0, END)
        e.insert(0, str(answer))
    

button1 = Button(root, text=1, padx=45, pady=30, command=lambda: buttonclick(1))
button2 = Button(root, text=2, padx=45, pady=30, command=lambda: buttonclick(2))
button3 = Button(root, text=3, padx=45, pady=30, command=lambda: buttonclick(3))
button4 = Button(root, text=4, padx=45, pady=30, command=lambda: buttonclick(4))
button5 = Button(root, text=5, padx=45, pady=30, command=lambda: buttonclick(5))
button6 = Button(root, text=6, padx=45, pady=30, command=lambda: buttonclick(6))
button7 = Button(root, text=7, padx=45, pady=30, command=lambda: buttonclick(7))
button8 = Button(root, text=8, padx=45, pady=30, command=lambda: buttonclick(8))
button9 = Button(root, text=9, padx=45, pady=30, command=lambda: buttonclick(9))
buttonPlus = Button(root, text="+", padx=45, pady=30, command=buttonPlus)
buttonEqual = Button(root, text="=", padx=90,pady=30, command=buttonEqual)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)
button7.grid(row=5, column=0)
button8.grid(row=5, column=1)
button9.grid(row=5, column=2)
buttonPlus.grid(row=6, column=0)
buttonEqual.grid(row=6,column=1, columnspan=2)

root.mainloop()