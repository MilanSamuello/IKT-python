from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: "+str(c))



foablak=Tk()
cimke=Label(foablak, text="Első mező:", fg="black")
cimke.pack()
mezo1=Entry(foablak)
mezo1.pack()
cimke=Label(foablak, text="Második:", fg="black")
cimke.pack()
mezo2=Entry(foablak)
mezo2.pack()
cimke=Label(foablak, text="Harmadik:", fg="black")
cimke.pack()
mezo3=Entry(foablak)
mezo3.pack()



foablak.mainloop()