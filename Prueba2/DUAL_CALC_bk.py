from tkinter import *

#from tkinter import ttk

#from PIL import Image,ImageTk

window = Tk()
window.title("ICC DUAL APP")
window.geometry("340x180")
window.resizable(0,0)
window.configure(bg = "white")

def calc():
    num = v.get()

    list_num = []
    
    for n in num:
        n = int(n) 

        list_num.append(n) 

    a =  list_num[9]
    b =  list_num[18]

    if a == 9:
        list_num[9] = 0
    else:
        list_num[9] = list_num[9] + 1
    if b == 0:
        list_num[18] = 8
    elif  b == 1:
        list_num[18] = 9
    else:
        list_num[18] = list_num[18] - 2

    dual = "".join(map(str, list_num)) 
 
    reply = d.set(format(dual)) 

    return reply

def clear():

    cls = v.set(format(""))
    era = d.set(format(""))
    return cls, era
              
     
lbl = Label(window, text="ICC REAL", font=("Arial Bold", 14),
             fg="blue", bg = "white").place(x=10, y=20)
v = StringVar()
icc = Entry(window,  relief=RIDGE, textvariable=v, font=("Arial Bold", 14),
            width=19, bg="powder blue", fg="darkblue").place(x=110, y=20)
lbl = Label(window, text="ICC DUAL", font=("Arial Bold", 14), fg="blue", 
            bg = "white").place(x=10, y=50)
btn = Button(window, text="Calcular", font=("Arial Bold", 14), bg="grey", 
             fg="white", command=calc).place(height=30, x=70, y=100)
d = StringVar()
icc_d= Entry(window, textvariable=d, font=("Arial Bold", 14),width=19, 
             fg="green", bd=0,bg = "white").place(x=110, y=50)
btn_c = Button(window, text=" Borrar ", font=("Arial Bold", 14), 
               bg="grey", fg="red",command=clear).place(height=30, x=180, y=100)
#imge= Image.open("C:/Users/JGT/OneDrive/Python/Movistar_min2.png")
#photo=ImageTk.PhotoImage(imge)
#logo=Label(image=photo).place(x=280, y=120)
        
window.mainloop()


	   



# ICCs DE PRUEBA

# 8934076690000134048

# 8934076699000134048

# 8934076699000134040

# 8934076699000134041

# 8934076690000134048















 
window.mainloop()
