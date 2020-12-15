# !/usr/bin/python3  
import tkinter as tk
from functools import partial


window = tk.Tk()
window.geometry("300x350")  
window.title("Calculator")
input_area = tk.Frame(window)
input_area.pack()

def hello(event):
    value = entry.get()
    current_value = event.keysym
    print(current_value)
    try:
        int(current_value)
    except ValueError:
        entry.delete(len(value)-1,len(value))
        print('not number') 
    print(entry.get())

entry = tk.Entry(input_area, fg="yellow", bg="Gray")
entry.pack()
entry.bind('<KeyRelease>', hello)
input_text = entry.get()
print('input_text:', input_text)

main_frame = tk.Frame(input_area, width=150, height=50)
main_frame.pack()

arr = list(range(10)) + ['0','+','-','*','/','%']

def pushed(arg):
    def get_button(arg):
        print('pushed: ', arr[arg])
    return get_button(arg)

number = 1
for i in range(5):
    for j in range(3):
        frame = tk.Frame(main_frame, relief=tk.RAISED, borderwidth=1,)
        frame.grid(row=i, column=j)
        label = tk.Button(frame, text= arr[number], relief=tk.RAISED, fg='Gray', bg='DimGray', width=10, height=3,command = partial(pushed, number))
        number += 1

        label.pack(fill='both')

window.mainloop()