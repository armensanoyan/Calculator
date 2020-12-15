# !/usr/bin/python3  
import tkinter as tk
from functools import partial
import operator

operations_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
entry_number = ''
operations = ['+','-','*','/','=']
list_of_buttons = list(range(10)) + ['0'] + operations
current_value =''
current_operation =''
first_value = ''

def main():

    window = tk.Tk()
    window.geometry("300x350")  
    window.title("Calculator")
    input_area = tk.Frame(window)
    input_area.pack()

    entry = tk.Entry(input_area, fg="yellow", bg="Gray")
    entry.bind('<KeyRelease>', get_keyboard_input)
    entry.pack()

    main_frame = tk.Frame(input_area, width=150, height=50)
    main_frame.pack()

    number = 1
    for i in range(5):
        for j in range(3):
            frame = tk.Frame(main_frame, relief=tk.RAISED, borderwidth=1,)
            frame.grid(row=i, column=j)
            label = tk.Button(frame, text= list_of_buttons[number], relief=tk.RAISED, fg='Gray', bg='DimGray', width=10, height=3)
            label.bind('<Button-1>',get_pushed_button)
            number += 1

            label.pack(fill='both')

    window.mainloop()


def get_pushed_button(event):
    current_value = event.widget['text']
    entry = event.widget.master.master.master.children['!entry']

    if type(current_value) == int or current_value.isdigit():
        entry.insert(len(entry.get()), str(list_of_buttons[current_value]))
    elif current_value in operations:
        global first_value
        global current_operation
        if first_value != '':
            current_value = operations_dict[current_operation](int(first_value), int(entry.get()))
            first_value = current_value
            entry.delete(0,len(entry.get()))
            entry.insert(0, current_value)
        else:
            current_operation = current_value
            first_value = entry.get()
            entry.delete(0,len(entry.get()))
    print(current_value)


def get_keyboard_input(event):
    entry = event.widget
    entry_number = entry.get()
    current_value = event.keysym

    if not current_value.isdigit() and not current_value in operations:
        entry.delete(len(entry_number)-1,len(entry_number))
    print(entry.get())


main()