# !/usr/bin/python3  
import tkinter as tk
from functools import partial

entry_number = ''
operations = ['0','+','-','*','/','=']
list_of_buttons = list(range(10)) + operations

def main():

    window = tk.Tk()
    window.geometry("300x350")  
    window.title("Calculator")
    input_area = tk.Frame(window)
    input_area.pack()
    entry = tk.Entry(input_area, fg="yellow", bg="Gray")
    entry.pack()
    entry.bind('<KeyRelease>', hello)
    main_frame = tk.Frame(input_area, width=150, height=50)
    main_frame.pack()

    number = 1
    for i in range(5):
        for j in range(3):
            frame = tk.Frame(main_frame, relief=tk.RAISED, borderwidth=1,)
            frame.grid(row=i, column=j)
            label = tk.Button(frame, text= list_of_buttons[number], relief=tk.RAISED, fg='Gray', bg='DimGray', width=10, height=3,command = partial(pushed, number, entry))
            number += 1

            label.pack(fill='both')

    window.mainloop()

def hello(event):
    entry_number = event.widget.get()
    current_value = event.keysym
    try:
        int(current_value)
    except ValueError:
        event.widget.delete(len(entry_number)-1,len(entry_number))
        print('not number') 
    print(event.widget.get())

def pushed(arg, entry):
    def get_button(arg):
        entry.insert(0,entry_number + str(list_of_buttons[arg]))
        print('pushed: ', list_of_buttons[arg])
    return get_button(arg)

main()