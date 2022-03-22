from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = 3.14 * a * a * b
    mezo3.delete(0, END)
    mezo3.insert(0, str(c)+" cm3")


foablak=Tk()
cimke=Label(foablak, text="Szia uram!", fg="black")
cimke.pack()
cimke=Label(foablak, text="Sugár (cm):", fg="black")
cimke.pack()
mezo1=Entry(foablak)
mezo1.pack()
cimke=Label(foablak, text="Magasság (cm):", fg="black")
cimke.pack()
mezo2=Entry(foablak)
mezo2.pack()
gomb4=Button(foablak, text="Kiszámít", command=osszeg)
gomb4.pack()
cimke=Label(foablak, text="Térfogat:", fg="black")
cimke.pack()
mezo3=Entry(foablak)
mezo3.pack()

foablak.mainloop()