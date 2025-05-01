from tkinter import *

def convert():
    a=float(input.get())
    km= round(a * 1.60934)
    label_3.config(text=f"{km}")


window= Tk()
window.title("Mile To Km Converter")

window.config(padx=20,pady=20)

#labels
label_1=Label(text="Miles")
label_1.grid(column=2,row=0)

label_2=Label(text="is equal to")
label_2.grid(column=0,row=1)

label_3=Label(text="0")
label_3.grid(column=1,row=1)

label_4=Label(text="Km")
label_4.grid(column=2,row=1)

#buttom
button=Button(text="Calculate",command=convert)
button.grid(column=1,row=2)

#entry
input=Entry(width=10)
input.grid(column=1,row=0)
window.mainloop()