from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = 3.14 * a * a * b
    
    mezo3.delete(0, END)
    mezo3.insert(0, str(c)+" cm3")
    v = c / 0.07874
    mezo4.delete(0, END)
    mezo4.insert(0, str(v)+" g")
    f = c / 0.68
    mezo5.delete(0, END)
    mezo5.insert(0, str(f)+" g")

foablak=Tk()
cimke=Label(foablak, text="SZIA URAM!", fg="black")
cimke.pack()
cimke=Label(foablak, text="", fg="black")
cimke.pack()
cimke=Label(foablak, text="Sugár (cm):", fg="black")
cimke.pack()
mezo1=Entry(foablak)
mezo1.pack()
cimke=Label(foablak, text="Magasság (cm):", fg="black")
cimke.pack()
mezo2=Entry(foablak)
mezo2.pack()
gomb4=Button(foablak, text="Kiszámít", command=osszeg,)
gomb4.pack()
cimke=Label(foablak, text="Térfogat:", fg="black")
cimke.pack()
mezo3=Entry(foablak)
mezo3.pack()
cimke=Label(foablak, text="Vashenger:", fg="black")
cimke.pack()
mezo4=Entry(foablak)
mezo4.pack()
cimke=Label(foablak, text="Fahenger:", fg="black")
cimke.pack()
mezo5=Entry(foablak)
mezo5.pack()

can1 = Canvas(foablak, width = 460, height = 460, bg = "white")
photo = PhotoImage(file = 'D:\IKT python projects\IKT-python\sus.png')
item = can1.create_image(40,40, image = photo)
can1.pack()

foablak.mainloop()