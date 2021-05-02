# Import everything from tkinter
from tkinter import *

# Import messagebox
from tkinter import messagebox

# display in window
root = Tk()

root.iconbitmap("calculator.ico")

# Set Title of the display window
root.title("CALCULATOR")


# Makes the display unresizable
root.resizable(0, 0)
root.configure(bg="gray")


equation = StringVar()

# Create text entry box for displaying the value
e = Entry(root, width=26, borderwidth=6, justify=RIGHT, textvariable=equation, font=('arial', 20, 'bold'), bg="gray")
# make entry using grid system
e.grid(row=0, column=0, columnspan=5)

current = ""


# Function to display number in text entry box
def button_click(number):
    global current
    current = current + str(number)
    equation.set(current)


# Function to clear the text of entry box
def button_clear():
    global current
    current = ""
    equation.set(current)


#
def button_del():
    global current


# Function to find final answer
def button_equal():
    # Try and except is used for error handling
    # like zero division and other
    try:
        global current
        # eval function evaluate the entry and str function changes the result to string
        total = str(eval(current))
        equation.set(total)
        current = total
    # If error occurs a popup is displayed
    except:
        messagebox.showinfo("MATH ERROR", "ERROR")

    # Create a Buttons and place it at a particular location
    # When user press the button, the command affiliated to that button is executed


button_1 = Button(root, text="1", padx=40, pady=21, command=lambda: button_click(1),font=('arial', 12),
                  bg="#364547")
button_2 = Button(root, text="2", padx=42, pady=21, command=lambda: button_click(2),font=('arial', 12),
                  bg="#364547")
button_3 = Button(root, text="3", padx=42, pady=21, command=lambda: button_click(3),font=('arial', 12),
                  bg="#364547")
button_4 = Button(root, text="4", padx=40, pady=21, command=lambda: button_click(4),font=('arial', 12),
                  bg="#364547")
button_5 = Button(root, text="5", padx=42, pady=21, command=lambda: button_click(5),font=('arial', 12),
                  bg="#364547")
button_6 = Button(root, text="6", padx=42, pady=21, command=lambda: button_click(6),font=('arial', 12),
                  bg="#364547")
button_7 = Button(root, text="7", padx=40, pady=21, command=lambda: button_click(7),font=('arial', 12),
                  bg="#364547")
button_8 = Button(root, text="8", padx=42, pady=21, command=lambda: button_click(8),font=('arial', 12),
                  bg="#364547")
button_9 = Button(root, text="9", padx=42, pady=21, command=lambda: button_click(9),font=('arial', 12),
                  bg="#364547")
button_0 = Button(root, text="0", padx=92, pady=20, command=lambda: button_click(0),font=('arial', 12),
                  bg="#364547")
button_dot = Button(root, text=".", padx=43, pady=20, command=lambda: button_click("."),font=('arial', 12, 'bold'),
                    bg="#364547")
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: button_click("+"),font=('arial', 12, 'bold'),
                    bg="#687980")
button_sub = Button(root, text="-", padx=42, pady=20, command=lambda: button_click("-"),font=('arial', 12, 'bold'),
                    bg="#687980")
button_div = Button(root, text="/", padx=42, pady=20, command=lambda: button_click("/"),font=('arial', 12, 'bold'),
                    bg="#687980")
button_mul = Button(root, text="x", padx=40, pady=20, command=lambda: button_click("*"),font=('arial', 12, 'bold'),
                    bg="#687980")
button_clear = Button(root, text="AC", padx=136, pady=20, command=button_clear,font=('arial', 12, 'bold'),
                      bg="#766161")
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal,font=('arial', 12, 'bold'),
                      bg="#393e46")

# Put the button on the screen
button_0.grid(row=5, column=0, columnspan=2)
button_dot.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_clear.grid(row=1, column=0, columnspan=3)
button_div.grid(row=1, column=3)

# Starts the loop
root.mainloop()
