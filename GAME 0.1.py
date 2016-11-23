from tkinter import *
import time
ventana= Tk()
ventana.geometry("1920x1080")
ventana.title("MARIO BROS")
dir1 = "Mario-Bros2.gif"
dir2= "MA2.png"
mapaimg= PhotoImage(file=dir1)
marioimg= PhotoImage(file=dir2)
fondo= Label(ventana, image=mapaimg).place(x=0, y=0)
c= Canvas(ventana,width=1920, height=1080)
c.config(bg="black")
c.pack()
mapa= c.create_image(0, 0, image=mapaimg, anchor=NW)
mario= c.create_image(735, 648, image=marioimg, anchor=NW)
c.place(x= 0,y=0)
estado=2
ya=False
#ventana.mainloop()
"""
nombre= Label(ventana,text="MARIO")
nombre.pack()
nombre.mainloop()
"""
def movermario(event):
    global estado
    if(event.keysym=="Left"):
       c.move(mario,-8,0)
       estado=1
    
    elif(event.keysym=='Right'):
       c.move(mario,8,0)
       estado=3
      

def salto(event):
    global estado,ya
    if(event.keysym=='Up'and ya == False):
        ya=True
        if(estado==2):
            ya = False
            for i in range(21):
                c.move(mario,0,-10)
                ventana.update()
                time.sleep(0.01)
                ya= False
            for i in range(21):
                c.move(mario,0,10)
                ventana.update()
                time.sleep(0.01)
                   
               #estado=2
                ya=False
        elif(estado == 3):
            for i in range(21): 
               c.move(mario,2,-10)
               ventana.update()
               time.sleep(0.01)
               ya = False
            for i in range(21):
               c.move(mario,2,10)
               ventana.update()
               time.sleep(0.01)
               
           #estado=2
               ya = False
        elif(estado == 1):
            for i in range(21): 
               c.move(mario,-2,-10)
               ventana.update()
               time.sleep(0.01)
               ya = False
            for i in range(21):
               c.move(mario,-2,10)
               ventana.update()
               time.sleep(0.01)
           
           #estado=2
               ya = False
        
def para():
    global estado
    estado=2
    ventana.after(500,para)
def gravedad():
    c.move(mario,0,20)
  
    
para()
c.bind_all("<KeyPress-Left>", movermario)
c.bind_all("<KeyPress-Right>", movermario)
c.bind_all("<KeyPress-Up>", salto)
#c.bind_all("<KeyPress-Down>", salto)



