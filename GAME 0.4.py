from tkinter import *
import time
import threading
ventana= Tk()
ventana.geometry("1920x1080")
ventana.title("MARIO BROS")
dir1 = "Mario-Bros2.gif"
dir2= "MarioS1.png"
dir3= "MarioS4.png"
dir4= "MarioS2.png"
dir5= "MarioS5.png"
dir6= "MarioS6.png"
dir7= "MarioS3.png"
dir8= "koopa1.png"
dir9= "koopa2.png"
mapaimg= PhotoImage(file=dir1)
marioimg= PhotoImage(file=dir2)
marioimg2= PhotoImage(file=dir3)
marioimg3= PhotoImage(file=dir4)
marioimg4= PhotoImage(file=dir5)
marioimg5= PhotoImage(file=dir6)
marioimg6= PhotoImage(file=dir7)
eneimg= PhotoImage(file=dir8)
eneimg2= PhotoImage(file=dir9)
fondo= Label(ventana, image=mapaimg).place(x=0, y=0)
c= Canvas(ventana,width=1920, height=1080)
c.config(bg="black")
c.pack()
mapa= c.create_image(0, 0, image=mapaimg, anchor=NW)
mario= c.create_image(500, 665, image=marioimg, anchor=NW)
ene= c.create_image(1000, 105, image=eneimg, anchor=NW)

def enem():
##    c.move(ene,-3,0)
##    ventana.update()
##    ventana.after(50, enem)
##

    while True:
        c.move(ene,-3,0)
        ventana.after(50)
        ventana.update()


        

                    
         
    

c.place(x= 0,y=0)
estado=2
ya=False
q=False
p=False


#ventana.mainloop()
"""
nombre= Label(ventana,text="MARIO")
nombre.pack()
nombre.mainloop()
"""
                     
    

def movermario(event):
    global estado, mario, q, a, te, te1,p
    # mover izquierda
    if(event.keysym=="Left" and q==False):
       te=c.coords(mario)[0]
       te1=c.coords(mario)[1]
       c.delete(mario)
       mario= c.create_image(te, te1, image=marioimg2, anchor=NW)
       c.move(mario,-3,0)
       ventana.update()
       ventana.after(1)
       estado=1
       q=True
    elif(event.keysym=="Left" and q==True):
        if(p==False):
           te=c.coords(mario)[0]
           te1=c.coords(mario)[1]
           c.delete(mario)
           mario= c.create_image(te, te1, image=marioimg2, anchor=NW)
           c.move(mario,-9,0)
           ventana.update()
           ventana.after(1)
           estado=1
           p=True
        elif(p==True):
           te=c.coords(mario)[0]
           te1=c.coords(mario)[1]
           c.delete(mario)
           mario= c.create_image(te, te1, image=marioimg3, anchor=NW)
           c.move(mario,-9,0)
           ventana.update()
           ventana.after(1)
           estado=1
           p=False
            
 
    
      


       
    # mover derecha
    elif(event.keysym=='Right' and q==True):
       te=c.coords(mario)[0]
       te1=c.coords(mario)[1]
       c.delete(mario)
       mario= c.create_image(te, te1, image=marioimg, anchor=NW)
       c.move(mario,9,0)
       ventana.update()
       ventana.after(1)
       estado=3
       q=False
    elif(event.keysym=='Right' and q==False):
      if(p==False):
           te=c.coords(mario)[0]
           te1=c.coords(mario)[1]
           c.delete(mario)
           mario= c.create_image(te, te1, image=marioimg, anchor=NW)
           c.move(mario,9,0)
           ventana.update()
           ventana.after(1)
           estado=3
           p=True
      elif(p==True):
           te=c.coords(mario)[0]
           te1=c.coords(mario)[1]
           c.delete(mario)
           mario= c.create_image(te, te1, image=marioimg4, anchor=NW)
           c.move(mario,9,0)
           ventana.update()
           ventana.after(1)
           estado=3
           p=False
           
           


      
    elif(event.keysym=='Down'):
       c.move(mario,0,10)
       
def yatu():
    global mario
    en= c.coords(enem)[0]
    en1= c.coords(enem)[1]
    te=c.coords(mario)[0]
    te1=c.coords(mario)[1]
    c.delete(mario)
    mario= c.create_image(te, te1, image=marioimg2, anchor=NW)
    ventana.after(500,yatu)
    
def salto(event):
    global estado, mario, q, a, te, te1,p, ya
    if(event.keysym=='Up'and ya == False):
        ya= True
        if(estado==2):
            contador=0
            contador2=0
            while(contador<20):
                te=c.coords(mario)[0]
                te1=c.coords(mario)[1]
                c.coords(mario, te, te1+1)
                contador+=1
##        ya=True
##        # salto arriba
##        if(estado==2):
##            contador=0
##            contador2=0
##            while(contador<20):
##                te=c.coords(mario)[0]
##                te1=c.coords(mario)[1]
##                c.delete(mario)
##                mario= c.create_image(te, te1, image=marioimg5, anchor=NW)
##                c.move(mario,0,-12)
##                ventana.update()
##                ventana.after(5)
##                contador+=1
##            while(contador2<23):
##                c.move(mario,0,12)
##                ventana.update()
##                ventana.after(5)
##                contador2+=1
##            te=c.coords(mario)[0]
##            te1=c.coords(mario)[1]
##            c.delete(mario)
##            mario= c.create_image(te, te1, image=marioimg, anchor=NW)
##            estado=2
##            ya=False
##        # salto derecha
##        elif(estado == 3):
##                contador=0
##                contador2=0
##                while(contador<20):
##                    te=c.coords(mario)[0]
##                    te1=c.coords(mario)[1]
##                    c.delete(mario)
##                    mario= c.create_image(te, te1, image=marioimg5, anchor=NW)
##                    c.move(mario,4,-12)
##                    ventana.after(5)
##                    ventana.update()
##                    contador+=1
##                while(contador2<20):
##                    if((c.coords(mario)[0]>912 and c.coords(mario)[1]<=472)):
##                        te=c.coords(mario)[0]
##                        c.move(mario,4,12)
##                        ventana.update()
##                        time.sleep(0.01)
##                        c.move(mario,4,12)
##                        ventana.update()
##                        time.sleep(0.01)
##                        c.move(mario,4,12)
##                        ventana.update()
##                        time.sleep(0.01)
##                        c.move(mario,4,12)
##                        ventana.update()
##                        time.sleep(0.01)
##                        c.move(mario,4,12)
##                        ventana.update()
##                        time.sleep(0.01)
##                        c.move(mario,4,12)
##                        ventana.update()
##                        time.sleep(0.01)
##                        c.move(mario,4,12)
##                        ventana.update()
##                        time.sleep(0.01)
##                        break
##                    c.move(mario,4,12)
##                    ventana.update()
##                    ventana.after(5)
##                    contador2+=1
##                te=c.coords(mario)[0]
##                te1=c.coords(mario)[1]
##                c.delete(mario)
##                mario= c.create_image(te, te1, image=marioimg, anchor=NW)
##                estado=2
##                ya = False
##        # saltar izquierda
##        elif(estado == 1): 
##            contador4=0
##            contador5=0
##            while(contador4<23):
##                te=c.coords(mario)[0]
##                te1=c.coords(mario)[1]
##                c.delete(mario)
##                mario= c.create_image(te, te1, image=marioimg6, anchor=NW)
##                c.move(mario,-4,-12)
##                ventana.update()
##                time.sleep(0.01)
##                contador4+=1
##            while(contador5<23):
##                if(c.coords(mario)[0]<588 and c.coords(mario)[1]<=472):
##                    te=c.coords(mario)[0]
##                    c.move(mario,-4,12)
##                    ventana.update()
##                    time.sleep(0.01)
##                    c.move(mario,-4,12)
##                    ventana.update()
##                    time.sleep(0.01)
##                    c.move(mario,-4,12)
##                    ventana.update()
##                    time.sleep(0.01)
##                    c.move(mario,-4,12)
##                    ventana.update()
##                    time.sleep(0.01)
##                    c.move(mario,-4,12)
##                    ventana.update()
##                    time.sleep(0.01)
##                    c.move(mario,-4,12)
##                    ventana.update()
##                    time.sleep(0.01)
##                    c.move(mario,-4,12)
##                    ventana.update()
##                    time.sleep(0.01)
##                    break
##                c.move(mario,-4,12)
##                ventana.update()
##                time.sleep(0.01)
##                contador5+=1
##            te=c.coords(mario)[0]
##            te1=c.coords(mario)[1]
##            c.delete(mario)
##            mario= c.create_image(te, te1, image=marioimg2, anchor=NW)
##            estado=2
##            ya = False
        
def para():
    global estado
    estado=2
    ventana.after(200,para)
    
    
def conti():
    global estado
    ventana.after(8,conti)
    # mapa continuo
    if(c.coords(mario)[0]>1287):
        te=c.coords(mario)[1]
        c.coords(mario, 215,te)
    if(c.coords(mario)[0]<212):
        te=c.coords(mario)[1]
        c.coords(mario, 1290,te)
    # suelo
    if(c.coords(mario)[1]>665):
        te=c.coords(mario)[0]
        c.coords(mario,te,665)
    # plataforma 1
    elif(c.coords(mario)[1]<583 and c.coords(mario)[1]>552 and c.coords(mario)[0]>912):
        te=c.coords(mario)[0]
        c.coords(mario,te,583)
    elif(c.coords(mario)[0]>912 and c.coords(mario)[1]>472 and c.coords(mario)[1]<583):
        te=c.coords(mario)[0]
        c.coords(mario,te,472)
    # caida 1
    elif(c.coords(mario)[0]<912 and c.coords(mario)[0]>588 and c.coords(mario)[1]==472):
        te=c.coords(mario)[0]
        contador7=0
        while(contador7<40):
            c.move(mario,0,10)
            ventana.update()
            time.sleep(0.01)
            contador7+=1
    # plataforma 2
    elif(c.coords(mario)[1]<583 and c.coords(mario)[1]>565 and c.coords(mario)[0]<588):
        te=c.coords(mario)[0]
        c.coords(mario,te,583)
    elif(c.coords(mario)[0]<588 and c.coords(mario)[1]>472 and c.coords(mario)[1]<583):
        te=c.coords(mario)[0]
        c.coords(mario,te,472)
    # plataforma 3
    elif(c.coords(mario)[1]<390 and c.coords(mario)[1]>358 and c.coords(mario)[0]<347):
        te=c.coords(mario)[0]
        c.coords(mario,te,390)
    elif(c.coords(mario)[1]<390 and c.coords(mario)[1]>278 and c.coords(mario)[0]<347):
        te=c.coords(mario)[0]
        c.coords(mario,te,278)
    # caida 2
    elif(c.coords(mario)[0]>347 and c.coords(mario)[0]<466 and c.coords(mario)[1]==278):
        te=c.coords(mario)[0]
        contador7=0
        while(contador7<25):
            c.move(mario,0,10)
            ventana.update()
            time.sleep(0.01)
            contador7+=1
    # plataforma 4
    elif(c.coords(mario)[1]<390 and c.coords(mario)[1]>358 and c.coords(mario)[0]<1037 and c.coords(mario)[0]>466):
        te=c.coords(mario)[0]
        c.coords(mario,te,390)
    elif(c.coords(mario)[1]<390 and c.coords(mario)[1]>278 and c.coords(mario)[0]>466 and c.coords(mario)[0]<1037):
        te=c.coords(mario)[0]
        c.coords(mario,te,278)
    # caida 3
    elif(c.coords(mario)[0]>1037 and c.coords(mario)[0]<1154 and c.coords(mario)[1]==278):
        te=c.coords(mario)[0]
        contador8=0
        while(contador8<25):
            c.move(mario,0,10)
            ventana.update()
            time.sleep(0.01)
            contador8+=1
    # plataforma 5 
    elif(c.coords(mario)[1]<390 and c.coords(mario)[1]>358 and c.coords(mario)[0]>1154):
        te=c.coords(mario)[0]
        c.coords(mario,te,390)
    elif(c.coords(mario)[1]<390 and c.coords(mario)[1]>278 and c.coords(mario)[0]>1154):
        te=c.coords(mario)[0]
        c.coords(mario,te,278)
    # plataforma 6
    elif(c.coords(mario)[1]<198 and c.coords(mario)[1]>164 and c.coords(mario)[0]<692):
        te=c.coords(mario)[0]
        c.coords(mario,te,198)
    elif(c.coords(mario)[1]<198 and c.coords(mario)[1]>83 and c.coords(mario)[0]<692):
        te=c.coords(mario)[0]
        c.coords(mario,te,85)
    # caida 4
    elif(c.coords(mario)[0]>692 and c.coords(mario)[0]<810 and c.coords(mario)[1]==85):
        te=c.coords(mario)[0]
        contador9=0
        while(contador9<25):
            c.move(mario,0,10)
            ventana.update()
            time.sleep(0.01)
            contador9+=1
    # plataforma 7
    elif(c.coords(mario)[1]<198 and c.coords(mario)[1]>164 and c.coords(mario)[0]>810):
        te=c.coords(mario)[0]
        c.coords(mario,te,198)
    elif(c.coords(mario)[1]<198 and c.coords(mario)[1]>85 and c.coords(mario)[0]>810):
        te=c.coords(mario)[0]
        c.coords(mario,te,85)

    # mapa continuo tortuga
    if(c.coords(ene)[0]>1287):
        te=c.coords(ene)[1]
        c.coords(ene, 215,te)
    if(c.coords(ene)[0]<212):
        te=c.coords(ene)[1]
        c.coords(ene, 1290,te)
    # suelo tortuga
    if(c.coords(ene)[1]>685):
        te=c.coords(ene)[0]
        c.coords(ene,te,685)
    # plataforma 1 tortuga
    elif(c.coords(ene)[0]>912 and c.coords(ene)[1]>492 and c.coords(ene)[1]<603):
        te=c.coords(ene)[0]
        c.coords(ene,te,492)
    # caida 1 tortuga
    elif(c.coords(ene)[0]<912 and c.coords(ene)[0]>588 and c.coords(ene)[1]==492):
        te=c.coords(ene)[0]
        contador7=0
        while(contador7<40):
            c.move(ene,0,10)
            ventana.update()
            time.sleep(0.01)
            contador7+=1
    # plataforma 2 tortuga
    elif(c.coords(ene)[0]<588 and c.coords(ene)[1]>492 and c.coords(ene)[1]<603):
        te=c.coords(ene)[0]
        c.coords(ene,te,492)
    # plataforma 3 tortuga
    elif(c.coords(ene)[1]<410 and c.coords(ene)[1]>298 and c.coords(ene)[0]<347):
        te=c.coords(ene)[0]
        c.coords(ene,te,298)
    # caida 2 tortuga
    elif(c.coords(ene)[0]>347 and c.coords(ene)[0]<466 and c.coords(ene)[1]==298):
        te=c.coords(ene)[0]
        contador7=0
        while(contador7<25):
            c.move(ene,0,10)
            ventana.update()
            time.sleep(0.01)
            contador7+=1
    # plataforma 4 tortuga
    elif(c.coords(ene)[1]<410 and c.coords(ene)[1]>298 and c.coords(ene)[0]>466 and c.coords(ene)[0]<1037):
        te=c.coords(ene)[0]
        c.coords(ene,te,298)
    # caida 3 tortuga
    elif(c.coords(ene)[0]>1037 and c.coords(ene)[0]<1154 and c.coords(ene)[1]==298):
        te=c.coords(ene)[0]
        contador8=0
        while(contador8<25):
            c.move(ene,0,10)
            ventana.update()
            time.sleep(0.01)
            contador8+=1
    # plataforma 5 tortuga
    elif(c.coords(ene)[1]<410 and c.coords(ene)[1]>298 and c.coords(ene)[0]>1154):
        te=c.coords(ene)[0]
        c.coords(ene,te,298)
    # plataforma 6 tortuga
    elif(c.coords(ene)[1]<218 and c.coords(ene)[1]>103 and c.coords(ene)[0]<692):
        te=c.coords(ene)[0]
        c.coords(ene,te,105)
    # caida 4 tortuga
    elif(c.coords(ene)[0]>692 and c.coords(ene)[0]<810 and c.coords(ene)[1]==105):
        te=c.coords(ene)[0]
        contador9=0
        while(contador9<25):
            c.move(ene,0,10)
            ventana.update()
            time.sleep(0.01)
            contador9+=1
    # plataforma 7 tortuga
    elif(c.coords(ene)[1]<218 and c.coords(ene)[1]>105 and c.coords(ene)[0]>810):
        te=c.coords(ene)[0]
        c.coords(ene,te,105)





    
    
    
    
    
          
    
        
    
    
    
def gravedad():
    c.move(mario,0,20)

para()
#yatu()
conti()
c.bind_all("<KeyPress-Left>", movermario)
c.bind_all("<KeyPress-Right>", movermario)
c.bind_all("<KeyPress-Up>", salto)
enem()

##c.bind_all("<KeyPress-Down>", movermario)
"""
 c.move(mario,0,-12)
            ventana.update()
            time.sleep(0.01)
            c.move(mario,4,0)
            ventana.update()
            time.sleep(0.01)
            c.move(mario,0,-12)


c.move(mario,4,-12)
            ventana.update()
            time.sleep(0.01)
            c.move(mario,4,-12)
            ventana.update()
            time.sleep(0.01)
            c.move(mario,4,-12)


        
            c.move(mario,4,12)
            ventana.update()
            time.sleep(0.01)
            c.move(mario,4,12)
            ventana.update()
            time.sleep(0.01)
            c.move(mario,0,12)
            ventana.update()
            time.sleep(0.01)

"""
#http://www.mariouniverse.com/sprites/snes/smb3


## # mapa continuo
##    if(c.coords(ene)[0]>1287):
##        te=c.coords(ene)[1]
##        c.coords(ene, 215,te)
##    if(c.coords(ene)[0]<212):
##        te=c.coords(ene)[1]
##        c.coords(ene, 1290,te)
##    # suelo
##    if(c.coords(ene)[1]>685):
##        te=c.coords(ene)[0]
##        c.coords(ene,te,685)
##    # plataforma 1
##    elif(c.coords(ene)[0]>912 and c.coords(ene)[1]>492 and c.coords(ene)[1]<603):
##        te=c.coords(ene)[0]
##        c.coords(ene,te,492)
##    # caida 1
##    elif(c.coords(ene)[0]<912 and c.coords(ene)[0]>588 and c.coords(ene)[1]==492):
##        te=c.coords(ene)[0]
##        contador7=0
##        while(contador7<40):
##            c.move(ene,0,10)
##            ventana.update()
##            time.sleep(0.01)
##            contador7+=1
##    # plataforma 2
##    elif(c.coords(ene)[0]<588 and c.coords(ene)[1]>492 and c.coords(ene)[1]<603):
##        te=c.coords(ene)[0]
##        c.coords(ene,te,492)
##    # plataforma 3
##    elif(c.coords(ene)[1]<410 and c.coords(ene)[1]>298 and c.coords(ene)[0]<347):
##        te=c.coords(ene)[0]
##        c.coords(ene,te,298)
##    # caida 2
##    elif(c.coords(ene)[0]>347 and c.coords(ene)[0]<466 and c.coords(ene)[1]==298):
##        te=c.coords(ene)[0]
##        contador7=0
##        while(contador7<25):
##            c.move(ene,0,10)
##            ventana.update()
##            time.sleep(0.01)
##            contador7+=1
##    # plataforma 4
##    elif(c.coords(ene)[1]<410 and c.coords(ene)[1]>298 and c.coords(ene)[0]>466 and c.coords(ene)[0]<1037):
##        te=c.coords(ene)[0]
##        c.coords(ene,te,298)
##    # caida 3
##    elif(c.coords(ene)[0]>1037 and c.coords(ene)[0]<1154 and c.coords(ene)[1]==298):
##        te=c.coords(ene)[0]
##        contador8=0
##        while(contador8<25):
##            c.move(ene,0,10)
##            ventana.update()
##            time.sleep(0.01)
##            contador8+=1
##    # plataforma 5 
##    elif(c.coords(ene)[1]<410 and c.coords(ene)[1]>298 and c.coords(ene)[0]>1154):
##        te=c.coords(ene)[0]
##        c.coords(ene,te,298)
##    # plataforma 6
##    elif(c.coords(ene)[1]<218 and c.coords(ene)[1]>103 and c.coords(ene)[0]<692):
##        te=c.coords(ene)[0]
##        c.coords(ene,te,105)
##    # caida 4
##    elif(c.coords(ene)[0]>692 and c.coords(ene)[0]<810 and c.coords(ene)[1]==105):
##        te=c.coords(ene)[0]
##        contador9=0
##        while(contador9<25):
##            c.move(ene,0,10)
##            ventana.update()
##            time.sleep(0.01)
##            contador9+=1
##    # plataforma 7
##    elif(c.coords(ene)[1]<218 and c.coords(ene)[1]>105 and c.coords(ene)[0]>810):
##        te=c.coords(ene)[0]
##        c.coords(ene,te,105)
##
##
##
##
##
