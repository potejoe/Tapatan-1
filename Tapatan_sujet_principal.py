#########################################
#informations liées au groupe
# groupe Miashs Td1 groupe 5
# Gouyer Roxane
# Alioune Ndiaye
# Momar SAMBE
# Maxime Jouan
# Pote die
########################
# import des librairies
import tkinter as tk
from random import randint

########################
# Constantes
Hauteur = 400
Largeur =300
######################
# Variables globales



########################
# fonctions


def test_clic(event):
    i, j = coord(event.x, event.y)
    if i > 40 and i < 60 and j > 90 and j <110:
        if tour[0] == 1 or tour[0] == 3 or tour[0] ==5 and piontableau[0] == 1:
            cadre.create_oval(40,90,60,110,width=0,fill='red')
            if tour[0] == 1:
               cadre.create_oval(45,45,55,55,width=0,fill='white')
            elif tour[0] == 3:
                cadre.create_oval(145,45,155,55,width=0,fill='white')
            elif tour[0] == 5:
                cadre.create_oval(245,45,255,55,width=0,fill='white')
            piontableau[0]=2
        elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6 and piontableau[0] == 1:
            cadre.create_oval(40,90,60,110,width=0,fill='blue')
            if tour[0] == 2:
                cadre.create_oval(45,345,55,355,width=0,fill='white')
            elif tour[0] == 4:
                cadre.create_oval(145,345,155,355,width=0,fill='white')
            elif tour[0] == 6:
                cadre.create_oval(245,345,255,355,width=0,fill='white')
            piontableau[0]=3
        tour[0] += 1
        

    if i > 140 and i < 160 and j > 90 and j <110:
        if tour[0] == 1 or tour[0] == 3 or tour[0] == 5 and piontableau[1] == 1:
           cadre.create_oval(140,90,160,110,width=0,fill='red')
           if tour[0] == 1:
               cadre.create_oval(45,45,55,55,width=0,fill='white')
           elif tour[0] == 3:
               cadre.create_oval(145,45,155,55,width=0,fill='white')
           elif tour[0] == 5:
               cadre.create_oval(245,45,255,55,width=0,fill='white')
           piontableau[1]= 2
        elif tour[0] == 2 or tour[0] == 4 or tour[0] ==6 and piontableau[1] == 1:
            cadre.create_oval(140,90,160,110,width=0,fill='blue')
            if tour[0] == 2:
                cadre.create_oval(45,345,55,355,width=0,fill='white')
            elif tour[0] == 4:
                cadre.create_oval(145,345,155,355,width=0,fill='white')
            elif tour[0] == 6:
                cadre.create_oval(245,345,255,355,width=0,fill='white')
            piontableau[1] = 3
        tour[0] += 1
    
    if i > 240 and i < 260 and j > 90 and j <110:
        if tour[0] == 1 or tour[0] == 3 or  tour[0] == 5 and piontableau[2] == 1:
            cadre.create_oval(240,90,260,110,width=0,fill='red')
            if tour[0] == 1:
                cadre.create_oval(45,45,55,55,width=0,fill='white')
            elif tour[0] == 3:
                cadre.create_oval(145,45,155,55,width=0,fill='white')
            elif tour[0] == 5:
                cadre.create_oval(245,45,255,55,width=0,fill='white')
            piontableau[2] = 2
        elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6 and piontableau[2] == 1:
            cadre.create_oval(240,90,260,110,width=0,fill='blue')
            if tour[0] == 2:
                cadre.create_oval(45,345,55,355,width=0,fill='white')
            elif tour[0] == 4:
                cadre.create_oval(145,345,155,355,width=0,fill='white')
            elif tour[0] == 6:
                cadre.create_oval(245,345,255,355,width=0,fill='white')
            piontableau[2] = 3
        tour[0] += 1

    if i > 40 and i < 60 and j > 175 and j <210:
        if tour[0] == 1 or tour[0] == 3 or tour[0] == 5 and piontableau[3] == 1:
           cadre.create_oval(40,190,60,210,width=0,fill='red')
           if tour[0]==1:
               cadre.create_oval(45,45,55,55,width=0,fill='white')
           elif tour[0] == 3:
               cadre.create_oval(145,45,155,55,width=0,fill='white')
           elif tour[0] == 5:
               cadre.create_oval(245,45,255,55,width=0,fill='white')
           piontableau[3] = 2
        elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6 and piontableau[3] == 1:
            cadre.create_oval(40,190,60,210,width=0,fill='blue')
            if tour[0]==2:
                cadre.create_oval(45,345,55,355,width=0,fill='white')
            elif tour[0] == 4:
                cadre.create_oval(145,345,155,355,width=0,fill='white')
            elif tour[0] == 6 :
                cadre.create_oval(245,345,255,355,width=0,fill='white')
            piontableau[3] = 3
        tour[0] += 1

    if i > 140 and i < 160 and j > 190 and j <210:
        if tour[0] == 1 or tour[0] == 3 or tour[0] == 5 and piontableau[4] == 1:
           cadre.create_oval(140,190,160,210,width=0,fill='red')
           if tour[0]==1:
               cadre.create_oval(45,45,55,55,width=0,fill='white')
           elif tour[0] == 3:
               cadre.create_oval(145,45,155,55,width=0,fill='white')
           elif tour[0] == 5:
               cadre.create_oval(245,45,255,55,width=0,fill='white')
           piontableau[4] = 2  
        elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6 and piontableau[4] == 1:
            cadre.create_oval(140,190,160,210,width=0,fill='blue')
            if tour[0] == 2:
                cadre.create_oval(45,345,55,355,width=0,fill='white')
            elif tour[0] == 4:
                cadre.create_oval(145,345,155,355,width=0,fill='white')
            elif tour[0] == 6:
                cadre.create_oval(245,345,255,355,width=0,fill='white')
            piontableau[4] = 3
        tour[0] += 1


    if i > 240 and i < 260 and j > 190 and j <210:
        if tour[0] == 1 or tour[0] == 3  or tour[0] == 5 and piontableau[5] == 1:
           cadre.create_oval(240,190,260,210,width=0,fill='red')
           if tour[0] == 1:
               cadre.create_oval(45,45,55,55,width=0,fill='white')
           elif tour[0] == 3:
               cadre.create_oval(145,45,155,55,width=0,fill='white')
           elif tour[0] == 5:
               cadre.create_oval(245,45,255,55,width=0,fill='white')
           piontableau[5] = 2
        elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6 and piontableau[5] == 1:
            cadre.create_oval(240,190,260,210,width=0,fill='blue')
            if tour[0] == 2:
                cadre.create_oval(45,345,55,355,width=0,fill='white')
            elif tour[0] == 4:
                cadre.create_oval(145,345,155,355,width=0,fill='white')
            elif tour[0] == 6:
                cadre.create_oval(245,345,255,355,width=0,fill='white')
            piontableau[5] = 3
        tour[0] += 1
    
    if i > 40 and i < 60 and j > 290 and j <310:
        if tour[0] == 1 or tour[0] == 3 or tour[0] == 5 and piontableau[6] == 1:
           cadre.create_oval(40,290,60,310,width=0,fill='red')
           if tour[0] == 1:
               cadre.create_oval(45,45,55,55,width=0,fill='white')
           elif tour[0] == 3:
               cadre.create_oval(145,45,155,55,width=0,fill='white')
           elif tour[0] == 5:
                cadre.create_oval(245,45,255,55,width=0,fill='white')
           piontableau[6] = 2
        elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6 and piontableau[6] == 1:
            cadre.create_oval(40,290,60,310,width=0,fill='blue')
            if tour[0] ==0:
                cadre.create_oval(45,345,55,355,width=0,fill='white')
            elif tour[0] == 4:
                cadre.create_oval(145,345,155,355,width=0,fill='white')
            elif tour[0] == 6:
                cadre.create_oval(245,345,255,355,width=0,fill='white')
            piontableau[6] = 3
        tour[0] += 1
    
    if i > 140 and i < 160 and j > 290 and j <310:
        if tour[0] == 1 or tour[0] == 3 or tour[0] == 5 and piontableau[7] == 1:
           cadre.create_oval(140,290,160,310,width=0,fill='red')
           if tour[0] ==1:
               cadre.create_oval(45,45,55,55,width=0,fill='white')
           elif tour[0] == 3:
               cadre.create_oval(145,45,155,55,width=0,fill='white')
           elif tour[0] == 5:
               cadre.create_oval(245,45,255,55,width=0,fill='white')
           piontableau[7] = 2
        elif tour[0] == 2 or tour[0] == 4 or tour[0] == 6 and piontableau[7] == 1:
            cadre.create_oval(140,290,160,310,width=0,fill='blue')
            if tour[0] == 2:
                cadre.create_oval(45,345,55,355,width=0,fill='white')
            elif tour[0] == 4:
                cadre.create_oval(145,345,155,355,width=0,fill='white')
            elif tour[0] == 6:
                cadre.create_oval(245,345,255,355,width=0,fill='white')
            piontableau[7] = 3
        tour[0] += 1

    if i > 240 and i < 260 and j > 290 and j <310:
        if tour[0] == 1 or tour[0] == 3 or tour[0] == 5 and piontableau[8] == 1:
            cadre.create_oval(240,290,260,310,width=0,fill='red')
            if tour[0] == 1:
                cadre.create_oval(45,45,55,55,width=0,fill='white')
            elif tour[0] == 3:
                cadre.create_oval(145,45,155,55,width=0,fill='white')
            elif tour[0] == 5:
                cadre.create_oval(245,45,255,55,width=0,fill='white')
            piontableau[8] = 2
        elif tour[0] == 4 or tour[0] == 2 or tour[0] == 6 and piontableau[8] == 1:
            cadre.create_oval(240,290,260,310,width=0,fill='blue')
            if tour[0] == 4:
                cadre.create_oval(145,345,155,355,width=0,fill='white')
            elif tour[0] == 2:
                cadre.create_oval(45,345,55,355,width=0,fill='white')
            elif tour[0] == 6:
                cadre.create_oval(245,345,255,355,width=0,fill='white')
            piontableau[8] = 3
        tour[0] += 1




def cree_pion():
    for i in range(3):
        xt,yt=i%3*100+50,i//3*100
        if i<3:yt+=50
        cadre.create_oval(xt-3,yt-3,xt+3,yt+3,width=0,fill='red')
    for i in range(12,15):
        xt,yt=i%3*100+50,i//3*100
        if i>11:yt-=50
        cadre.create_oval(xt-3,yt-3,xt+3,yt+3,width=0,fill='blue')

def tracePlateau():
    cadre.create_rectangle(50,100,250,300,width=5)
    cadre.create_line(50,100,250,300,width=5,fill='black')
    cadre.create_line(50,300,250,100,width=5,fill='black')
    cadre.create_line(50,200,250,200,width=5,fill='black')
    cadre.create_line(150,100,150,300,width=5,fill='black')
    for i in range(15):
        xt,yt=i%3*100+50,i//3*100
        if i<3:yt+=50
        if i>11:yt-=50
        cadre.create_oval(xt-7,yt-7,xt+7,yt+7,width=5,fill='black')
        cadre.create_oval(xt-3,yt-3,xt+3,yt+3,width=0,fill='light yellow')

    
def coord(x, y):
    return x , y

def tour_joueur():
    global tour
    tour = [1]

def pion_existant():
    global piontableau
    piontableau = [1,1,1,1,1,1,1,1,1]



########################
# programme principal
fen = tk.Tk()
fen.title('Tapatan')
cadre= tk.Canvas(fen, bg='white', width=Largeur, height=Hauteur)
cadre.grid(row=1,column=1,columnspan=3)
tracePlateau()
cree_pion()
tour_joueur()
pion_existant()
cadre.bind("<Button-1>",test_clic)
fen.mainloop()