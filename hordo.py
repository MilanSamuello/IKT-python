from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = int(mezo3.get())

    d = 3.14 * b * b * c 
    mezo4.delete(0, END)
    mezo4.insert(0, str(d)+" l")

    s = d / a
    mezo5.delete(0, END)
    mezo5.insert(0, str(s)+" bor")

foablak=Tk()
cimke=Label(foablak, text="SZIA URAM!", fg="black")
cimke.pack()
cimke=Label(foablak, text="", fg="black")
cimke.pack()
cimke=Label(foablak, text="bor mennyisége (liter):", fg="black")
cimke.pack()
mezo1=Entry(foablak)
mezo1.pack()

cimke=Label(foablak, text="Hordó magassága (dm):", fg="black")
cimke.pack()
mezo2=Entry(foablak)
mezo2.pack()
cimke=Label(foablak, text="Hordó szélessége (dm):")
cimke.pack()
mezo3=Entry(foablak)
mezo3.pack()
gomb4=Button(foablak, text="Kiszámítás", command=osszeg,)
gomb4.pack()
cimke=Label(foablak, text="Hordó literje:", fg="black")
cimke.pack()
mezo4=Entry(foablak)
mezo4.pack()
cimke=Label(foablak, text="Ennyi bor fér bele:", fg="black")
cimke.pack()
mezo5=Entry(foablak)
mezo5.pack()
can1 = Canvas(foablak, width = 460, height = 460, bg = "black")
photo = PhotoImage(file = 'D:\IKT python projects\IKT-python\sus.png')
item = can1.create_image(50,50, image = photo)
can1.pack()

foablak.mainloop()