'''

Created on 24 mar. 2020

**** LOGIN WINDOW ****

'''
# -*- coding: utf-8 -*-


import tkinter as tk

win = tk.Tk()

win.title("LOGIN")
win.geometry("320x240+650+200")
win.resizable(0,0)
win.configure(bg = "#e3e3e3", relief = "groove", bd = 6, cursor="hand2")

in_user = tk.StringVar()
in_pass = tk.StringVar()

title = tk.Label(win, text = "LOGIN WINDOW", padx = 5, font=("Arial Bold", 14),  
                  fg="#636363", bg = "#e3e3e3")
title.place(width = 200, height = 30, x = 80, y = 20)

lbl1 = tk.Label(win, text = "User", padx = 5,  font=("Arial Bold", 16),  
                  fg="#636363", bg = "#e3e3e3")
lbl1.place(width = 60, height = 30, x = 10, y = 70)

user = tk.Entry(win, textvariable = in_user,  font=("Arial Bold", 12),  
                  fg="#636363", bg = "white")
user.place(width = 200, height = 30, x = 80, y = 70)

lbl2 = tk.Label(win, text = "Pass", font=("Arial Bold", 14),  
                  fg="#636363", bg = "#e3e3e3")
lbl2.place(width = 60, height = 30, x = 10, y = 110)

passw = tk.Entry(win, textvariable = in_pass,  font=("Arial Bold", 12),  
                  fg="#636363", bg = "white")
passw.place(width = 200, height = 30, x = 80, y = 110)










win.mainloop()