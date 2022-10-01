from lib2to3.pgen2.literals import simple_escapes
import random
from tkinter import *
import string
import pyperclip

def generator():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special = string.punctuation
    pass_length = int(length_spin.get())
    simple = lowercase + numbers
    hard = lowercase + uppercase + numbers + special
    if choice.get() == 1:
        passEntry.delete(0, END)
        passEntry.insert(0, random.sample(simple, pass_length))
    if choice.get() == 2:
        passEntry.delete(0, END)
        passEntry.insert(0, random.sample(hard, pass_length))

def copy():
    pyperclip.copy(passEntry.get())

root = Tk()
root.title('Генератор пароля')
choice = IntVar()
mainColor = '#4a5a6c';
secondColor = '#df9a78';
Font = ('Arial', 22, 'bold')
Font2 = ('Arial', 18, 'bold')

root.config(bg=mainColor)

Label(root, text='Сложность пароля', font=Font, bg=mainColor, fg=secondColor).grid()

Radiobutton(root, text='Легкий', value=1, command=generator, variable=choice, font=Font2, bg=mainColor, fg=secondColor, activebackground=mainColor).grid(pady=5)
Radiobutton(root, text='Сложный', value=2, command=generator, variable=choice, font=Font2, bg=mainColor, fg=secondColor, activebackground=mainColor).grid(pady=5)

Label(root, text='Длина пароля', font=Font, bg=mainColor, fg=secondColor).grid()

length_spin = Spinbox(root, from_=6, to_=24, command=generator, width=5, font=Font, bg=mainColor, fg=secondColor)
length_spin.grid()

passEntry = Entry(root, width = 42, bd=2, font=Font, bg=mainColor, fg=secondColor, justify='center')
passEntry.grid(pady=5, padx=10)

copyButton = Button(root, command=copy, text='Копировать', font=Font2, bg=mainColor, fg=secondColor, activebackground=mainColor).grid(pady=5)

root.mainloop()