# CALCULATOR WITH TKINTER GUI

import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

# Create the window
w = tk.Tk()
w.title('Calculator')

# Create the frame
frame = tk.Frame(w, padx=10, bg='black')
frame.pack()

# Create an entry
entry = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=3, ipadx=3)


def det_click(num):
    entry.insert(tk.END, num)


def equal():  # if user press = button
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo('Error', 'Invalid Input')


def clear():  # if user press clear button
    entry.delete(0, tk.END)


# CREATE BUTTON

num_1 = tk.Button(frame, text='1', padx=15, pady=5, width=3, command=lambda: det_click(1))
num_1.grid(row=1, column=0, pady=2)

num_2 = tk.Button(frame, text='2', padx=15, pady=5, width=3, command=lambda: det_click(2))
num_2.grid(row=1, column=1, pady=2)

num_3 = tk.Button(frame, text='3', padx=15, pady=5, width=3, command=lambda: det_click(3))
num_3.grid(row=1, column=2, pady=2)

mul_button = tk.Button(frame, text='X', padx=15, pady=5, width=3, command=lambda: det_click('*'))
mul_button.grid(row=1, column=3, pady=2)

num_4 = tk.Button(frame, text='4', padx=15, pady=5, width=3, command=lambda: det_click(4))
num_4.grid(row=2, column=0, pady=2)

num_5 = tk.Button(frame, text='5', padx=15, pady=5, width=3, command=lambda: det_click(5))
num_5.grid(row=2, column=1, pady=2)

num_6 = tk.Button(frame, text='6', padx=15, pady=5, width=3, command=lambda: det_click(6))
num_6.grid(row=2, column=2, pady=2)

div_button = tk.Button(frame, text=':', padx=15, pady=5, width=3, command=lambda: det_click('/'))
div_button.grid(row=2, column=3, pady=2)

num_7 = tk.Button(frame, text='7', padx=15, pady=5, width=3, command=lambda: det_click(7))
num_7.grid(row=3, column=0, pady=2)

num_8 = tk.Button(frame, text='8', padx=15, pady=5, width=3, command=lambda: det_click(8))
num_8.grid(row=3, column=1, pady=2)

num_9 = tk.Button(frame, text='9', padx=15, pady=5, width=3, command=lambda: det_click(9))
num_9.grid(row=3, column=2, pady=2)

pow_button = tk.Button(frame, text='^', padx=15, pady=5, width=3, command=lambda: det_click('**'))
pow_button.grid(row=3, column=3, pady=2)

add_button = tk.Button(frame, text='+', padx=15, pady=5, width=3, command=lambda: det_click('+'))
add_button.grid(row=4, column=0, pady=2)

num_0 = tk.Button(frame, text='0', padx=15, pady=5, width=3, command=lambda: det_click(0))
num_0.grid(row=4, column=1, pady=2)

sub_button = tk.Button(frame, text='-', padx=15, pady=5, width=3, command=lambda: det_click('-'))
sub_button.grid(row=4, column=2, pady=2)

eq_button = tk.Button(frame, text='=', padx=15, pady=5, width=3, command=lambda: equal())
eq_button.grid(row=4, column=3, pady=2)

c_button = tk.Button(frame, text='clear', padx=15, pady=5, width=3, command=lambda: clear())
c_button.grid(row=5, column=1, columnspan=2, pady=2)

w.mainloop()
