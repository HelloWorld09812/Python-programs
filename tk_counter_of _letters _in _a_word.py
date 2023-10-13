from tkinter import *
from tkinter import messagebox

def btn_click():
    text_input = text.get()
    counter = len(text_input)
    info = f'В слове: {text_input} | {counter} символов'
    messagebox.showinfo(title='Название', message=info)

window = Tk()
window.geometry('600x400')
window.title('Счетчик букв в слове')

text = Entry(window)
text.pack()

btn = Button(text='Выполнить', command=btn_click)
btn.pack()

window.mainloop()
