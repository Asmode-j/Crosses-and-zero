import tkinter as tk
from tkinter import messagebox
import random

num_button = list(range(1, 10))
counter=0
win = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
igra=[]
win_kerstik=[]
win_nolik=[]

def otmetka0():
    global counter, igra
    if '1' not in igra:
        Igrok()
        btn0.configure(text='X') if counter % 2 == 0 else btn0.configure(text='O')
        win_kerstik.append(1) if counter % 2 == 0 else win_nolik.append(1)
        check_win()           
        counter+=1
        igra.append('1')
    else:
        pass
def otmetka1():
    global counter, igra
    if '2' not in igra:
        Igrok()
        btn1.configure(text='X') if counter % 2 == 0 else btn1.configure(text='O')
        win_kerstik.append(2) if counter % 2 == 0 else win_nolik.append(2)
        check_win()
        counter+=1
        igra.append('2')
    else:
        pass
def otmetka2():
    global counter, igra
    if '3' not in igra:
        Igrok()
        btn2.configure(text='X') if counter % 2 == 0 else btn2.configure(text='O')
        win_kerstik.append(3) if counter % 2 == 0 else win_nolik.append(3)
        check_win()
        counter+=1
        igra.append('3')
    else:
        pass
def otmetka3():
    global counter, igra
    if '4' not in igra:
        Igrok()
        btn3.configure(text='X') if counter % 2 == 0 else btn3.configure(text='O')
        win_kerstik.append(4) if counter % 2 == 0 else win_nolik.append(4)
        check_win()
        counter+=1
        igra.append('4')
    else:
        pass
def otmetka4():
    global counter, igra
    if '5' not in igra:
        Igrok()
        btn4.configure(text='X') if counter % 2 == 0 else btn4.configure(text='O')
        win_kerstik.append(5) if counter % 2 == 0 else win_nolik.append(5)
        check_win()
        counter+=1
        igra.append('5')
    else:
        pass
def otmetka5():
    global counter, igra
    if '6' not in igra:
        Igrok()
        btn5.configure(text='X') if counter % 2 == 0 else btn5.configure(text='O')
        win_kerstik.append(6) if counter % 2 == 0 else win_nolik.append(6)
        check_win()
        counter+=1
        igra.append('6')
    else:
        pass
def otmetka6():
    global counter, igra
    if '7' not in igra:
        Igrok()
        btn6.configure(text='X') if counter % 2 == 0 else btn6.configure(text='O')
        win_kerstik.append(7) if counter % 2 == 0 else win_nolik.append(7)
        check_win()
        counter+=1
        igra.append('7')
    else:
        pass
def otmetka7():
    global counter, igra
    if '8' not in igra:
        Igrok()
        btn7.configure(text='X') if counter % 2 == 0 else btn7.configure(text='O')
        win_kerstik.append(8) if counter % 2 == 0 else win_nolik.append(8)
        check_win()
        counter+=1
        igra.append('8')
    else:
        pass
def otmetka8():
    global counter, igra
    if '9' not in igra:
        Igrok()
        btn8.configure(text='X') if counter % 2 == 0 else btn8.configure(text='O')
        win_kerstik.append(9) if counter % 2 == 0 else win_nolik.append(9)
        check_win()
        counter+=1
        igra.append('9')
    else:
        pass

def Igrok():
    global counter
    if counter % 2 == 0:
        igrok = 'Нолик'
        lbl.configure(text=f'Ход: {igrok}')
    else:
        igrok = 'Крестик'
        lbl.configure(text=f'Ход: {igrok}')

def check_win():
    win_kerstik.sort()
    win_nolik.sort()
    for i_win in win:
        if counter % 2 == 0:
            for i1 in win_kerstik:
                    for i2 in win_kerstik:
                            for i3 in win_kerstik:
                                if [i1,i2,i3] in win:
                                    lbl.configure(text='Победил Крестик')
                                    messagebox.showinfo('Оповещение', 'Победил Крестик')
                                    window.destroy()                
        elif counter % 2 ==1:
            for i1 in win_nolik:
                    for i2 in win_nolik:
                            for i3 in win_nolik:
                                if [i1,i2,i3] in win:
                                    lbl.configure(text='Победил Нолик')
                                    messagebox.showinfo('Оповещение', 'Победил Нолик')
                                    window.destroy()
    if len(igra)>=8:
        lbl.configure(text='Ничья')
        messagebox.showinfo('Оповещение', 'Ничья')          

window = tk.Tk()
window.title("Крестики нолики")  
window.geometry('750x550')

index=0
for row in range(3):
    for column in range(3):
        exec (f'btn{index} = tk.Button(text = "   ", command=otmetka{index}, font=("Arial Bold", 26))')
        exec (f'btn{index}.grid(column={column}, row={row})')
        index+=1

lbl = tk.Label(window, text=f'Ход: Крестик', font=("Arial Bold", 16))
lbl.grid(sticky=tk.N,column=3, row=0)

window.mainloop()
