from tkinter import*
from Traitement import*
from Hole import*
from Type import*

myWindow = Tk()
myWindow.geometry("1000x800+300+200")
myWindow.title("National Road")

road = Road(1,'',1,2,'linestring(0 0,0 0)',1)
holehafa = Hole(0,2,4,'linestring(0 0)',5,1)
hole = road.getAllHole()
nom = road.getRoadName()
tar = Type(1, "tar", 1000, 2)

for i in range (len(hole)):
    qty = hole[i].quantite()
    prix = tar.getPrix(qty)
    calDuree = tar.calcDuree(qty)
    id = Label(myWindow, text = 'id : '+str(hole[i].id))
    id.pack()
    q = Label(myWindow, text = 'q : '+str(qty))
    q.pack()
    qtt = Label(myWindow, text = 'duree : '+str(calDuree))
    qtt.pack()
    vidiny = Label(myWindow, text = 'Prix : '+str(prix)+'\n')
    vidiny.pack()


myWindow.mainloop()