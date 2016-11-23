from tkinter import *
import time
import random

#============ TK =============#
ventana= Tk()
ventana.geometry("1920x1080")
ventana.title("MARIO BROS")

#=========== Direcciones de imagen ============#
dir1 = "MAPA.gif"
dir2= "MarioS1.png"
dir3= "MarioS4.png"
dir4= "MarioS2.png"
dir5= "MarioS5.png"
dir6= "MarioS6.png"
dir7= "MarioS3.png"
dir8= "koopa1.png"
dir9= "koopa3.png"
dir10= "koopa001.png"
dir11= "koopa2.png"
dir12= "koopa4.png"
dir13= "koopa6.png"
dir14= "koopa7.png"
dir15= "BOM.png"
dir16= "BOM2.png"
dir17= "MENU6.png"
dir18= "M1.png"
dir19= "M2.png"
dir20= "M4.png"
dir21= "1.png"
dir22= "2.png"
dir23= "3.png"
dir24= "4.png"
dir25= "5.png"
dir26= "koopa8.png"
dir27= "koopa9.png"
dir28= "BOM3.png"
dir29= "MARIOS.png"
dir30= "LIVE.png"
dir31= "LUIGI.png"
dir32= "LU.png"
dir33= "LU2.png"
dir34= "LU3.png"
dir35= "LU7.png"
dir36= "LU6.png"
dir37= "LU8.png"
dir38= "POW.png"
dir39= "POW2.png"
dir40= "POW3.png"
dir41= "STAR.png"
dir42= "mush.png"
dir43= "OP.png"
dir44= "opb.png"
#========== Asignacion de imagenes ==========#
# Mapa
mapaimg= PhotoImage(file=dir1)
# Mario
marioimg= PhotoImage(file=dir2)
marioimg2= PhotoImage(file=dir3)
marioimg3= PhotoImage(file=dir4)
marioimg4= PhotoImage(file=dir5)
marioimg5= PhotoImage(file=dir6)
marioimg6= PhotoImage(file=dir7)
# Enemigos
eneimg= PhotoImage(file=dir8)
eneimg2= PhotoImage(file=dir9)
eneimg1= PhotoImage(file=dir10)
eneimg3= PhotoImage(file=dir11)
eneimg4= PhotoImage(file=dir12)
eneimg5= PhotoImage(file=dir13)
eneimg6= PhotoImage(file=dir14)
eneimg7= PhotoImage(file=dir15)
eneimg8= PhotoImage(file=dir16)
eneimg9= PhotoImage(file=dir26)
eneimg10= PhotoImage(file=dir27)
eneimg11= PhotoImage(file=dir28)
# Menu
menuimg= PhotoImage(file=dir17)
mimg= PhotoImage(file= dir18)
mimg2= PhotoImage(file= dir19)
mimg3= PhotoImage(file= dir20)
nimg1= PhotoImage(file= dir21)
nimg2= PhotoImage(file= dir22)
nimg3= PhotoImage(file= dir23)
nimg4= PhotoImage(file= dir24)
nimg5= PhotoImage(file= dir25)
pimg= PhotoImage(file= dir29)
limg= PhotoImage(file= dir30)
pimg2= PhotoImage(file= dir31)
# Luigi
luimg= PhotoImage(file= dir32)
luimg2= PhotoImage(file= dir33)
luimg3= PhotoImage(file= dir34)
luimg4= PhotoImage(file= dir35)
luimg5= PhotoImage(file= dir36)
luimg6= PhotoImage(file= dir37)
# POW
powimg= PhotoImage(file= dir38)
powimg2= PhotoImage(file= dir39)
powimg3= PhotoImage(file= dir40)
# Power
simg= PhotoImage(file= dir41)
muimg= PhotoImage(file= dir42)
# Opciones
oimg= PhotoImage(file= dir43)
oimg2= PhotoImage(file= dir44)
fondo= Label(ventana, image=mapaimg).place(x=0, y=0)
c= Canvas(ventana,width=1920, height=1080)
c.config(bg="black")
c.pack()
# MENU
menu= c.create_image(0, 0, image=menuimg, anchor=NW)
x=0
y=0
z=0
tt=0
punt1= 0
punt2= 0
yatu={'Up':False,'Right':False,'Left':False,'w':False,'a':False,'d':False}
esm=True
esl=True
lod=False
#================= INICIO ================#
def sta():
    """
    funcion que inicia el menu principal del juego y da paso al mismo
    entrada: nada
    salida: muestra botones principales
    """
    global options, start, load, n1, n2, n3, n4, n5, em, caja, e2, em2, caja2, em0, loade, pp1, pp2, punt1, punt2, datos, guardar, loade, lod
    load.destroy()
    start.destroy()
    options.destroy()
    em0= Label(ventana, image=pimg)
    em0.place(x=600, y=380)
    caja= Entry(ventana)
    caja.place(x=600, y=445)
    e2= Label(ventana, image=pimg2)
    e2.place(x=755, y=380)
    caja2= Entry(ventana)
    caja2.place(x=755, y=445)
    
    # Botones de dificultad
    n1= Button(ventana, image= nimg1, command= dif1)
    n1.place(x=500, y=500)
    n2= Button(ventana, image= nimg2, command= dif2)
    n2.place(x=600, y=500)
    n3= Button(ventana, image= nimg3, command= dif3)
    n3.place(x=700, y=500)
    n4= Button(ventana, image= nimg4, command= dif4)
    n4.place(x=800, y=500)
    n5= Button(ventana, image= nimg5, command= dif5)
    n5.place(x=900, y=500)
#============ CARGAR PARTIDA ============#
def loade():
    """
    funcion encargada de cargar una partida ya guardada
    entrada: nada
    salida: comienza la partida guardada
    """
    global inf, options, start, load, n1, n2, n3, n4, n5, em, caja, e2, em2, caja2, em0, loade, pp1, pp2, punt1, punt2, datos, guardar, loade, lod
    load.destroy()
    start.destroy()
    options.destroy()
    em0= Label(ventana, image=pimg)
    em0.place(x=600, y=380)
    e2= Label(ventana, image=pimg2)
    e2.place(x=755, y=380)
        
    # Botones de dificultad
    n1= Button(ventana, image= nimg1, command= dif1)
    n1.place(x=500, y=500)
    n2= Button(ventana, image= nimg2, command= dif2)
    n2.place(x=600, y=500)
    n3= Button(ventana, image= nimg3, command= dif3)
    n3.place(x=700, y=500)
    n4= Button(ventana, image= nimg4, command= dif4)
    n4.place(x=800, y=500)
    n5= Button(ventana, image= nimg5, command= dif5)
    n5.place(x=900, y=500)
    g= open("partida.txt", "r")
    datos= g.readlines()
    g.close()
    lod=True
    print("buenas")

#=========== OPCIONES ==============#
def opt():
    """
    funcion que muestra los controles basicos del juego
    entrada: nada
    salida: mostrar controles
    """
    global inf, options, start, load, n1, n2, n3, n4, n5, em, caja, e2, em2, caja2, em0, loade, pp1, pp2, punt1, punt2, datos, guardar, loade, lod, tt, opc, pol
    load.destroy()
    start.destroy()
    options.destroy()
    opc= c.create_image(0, 0, image=oimg, anchor=NW)
    pol= Button(ventana, image= oimg2, command= men)
    pol.place(x=1100, y=350)
    tt+=1
#================== MENU ==================#
def men():
    """
    funcion que invoca o retorna al menu principal
    entrada: nada
    salida: aparece menu principal
    """
    global inf, options, start, load, n1, n2, n3, n4, n5, em, caja, e2, em2, caja2, em0, loade, pp1, pp2, punt1, punt2, datos, guardar, loade, lod, opc, tt, pol
    # Botones menu
    if(tt>=1):
        c.delete(opc)
        pol.destroy()
    load= Button(ventana, image= mimg3, command= loade)
    load.place(x=560, y=500)
    options= Button(ventana, image= mimg2, command= opt)
    options.place(x=560, y=600)    
    start= Button(ventana, image=mimg, command= sta)
    start.place(x=560, y=400)
men()
#============= Dificultades ==============#

# Dificultad 1
def dif1():
    """
    funcion que define la dificultad 1 (mas baja)
    entrada: nada
    salida: define varibles que modifican velocidad de cada enemigo
    y veloidad a la que aparecen
    """
    global x, y, z, v, n, lives, livesl
    x=0
    y=0
    z=0
    lives=3
    livesl=3
    n=1
    
    game()

# Dificultad 2
def dif2():
    """
    funcion que define la dificultad 2
    entrada: nada
    salida: define varibles que modifican velocidad de cada enemigo
    y veloidad a la que aparecen
    """
    global x, y, z, v, n, lives, livesl
    x=3
    y=10
    z=5000
    lives=3
    livesl=3
    n=2
    game()

# Dificultad 3
def dif3():
    """
    funcion que define la dificultad 3
    entrada: nada
    salida: define varibles que modifican velocidad de cada enemigo
    y veloidad a la que aparecen
    """
    global x, y, z, v, n, lives, livesl
    x=6
    y=20
    z=10000
    lives=4
    livesl=4
    n=3
    game()

# Dificultad 4
def dif4():
    """
    funcion que define la dificultad 4
    entrada: nada
    salida: define varibles que modifican velocidad de cada enemigo
    y veloidad a la que aparecen
    """
    global x, y, z, v, n, lives, livesl
    x=9
    y=30
    z=15000
    lives=4
    livesl=4
    n=4
    game()

# Dificultad 5
def dif5():
    """
    funcion que define la dificultad 5 (maxima)
    entrada: nada
    salida: define varibles que modifican velocidad de cada enemigo
    y veloidad a la que aparecen
    """
    global x, y, z, v, n, lives, livesl
    x=12
    y=40
    z=20000
    lives=5
    livesl=5
    n=5
    game()
    
#====================== FUNCION QUE COMIENZA EL JUEGO ===========================#
def game():
    """
    funcion que da inicio al juego, creando el mapa y hacindo aparecer jugadores y enemigos
    entrada: nada
    salida: mapa con respectivos jugadores y enemigos
    """
    global loade, pp1, pp2, punt1, punt2, datos, lod, esl, livel, livem, cv, ctm, xyz, h, POW, puntaje2,y, u, punt2, livesl, estadol, caja, luigi, caja2, pp1, pp2, puntaje1, punt1, esm, n, v, z, contene2,em0, em, caja, e2, em2, caja2, n1, n2, n3, n4, n5, m, ene, en, en1, n, esn, lives,contene, xz, x, estado, mario, q, a, te, te1,p, estado, mario, q, a, te, te1,p, ya, estado, lives, en, en1, ene, esn, y
    n1.destroy()
    n2.destroy()
    n3.destroy()
    n4.destroy()
    n5.destroy()
    if(lod==False):
        pp1= str(caja.get())
        pp2= str(caja2.get())
    elif(lod==True):
        pp1= datos[0]
        pp2= datos[1]
        punt1= int(datos[2])
        punt2= int(datos[3])
#============= PUNTUACION ============#
    pun1= Label(ventana, text= pp1, bg="red", fg="white", font=("Arial", 25), padx=6,pady=6)
    pun1.place(x=25, y=400)
    pun2= Label(ventana, text= pp2, bg="green", fg="white", font=("Arial", 25), padx=6,pady=6)
    pun2.place(x=1360, y=400)
    puntaje1= Label(ventana, text= punt1, bg="black", fg="white", font=("Arial", 25), padx=70,pady=0)
    puntaje1.place(x=20, y=450)
    puntaje2= Label(ventana, text= punt2, bg="black", fg="white", font=("Arial", 25), padx=70,pady=0)
    puntaje2.place(x=1340, y=450)
    if(lod==False):
        caja.destroy()
        caja2.destroy()
    em0.place(x=40, y=240)
    e2.place(x=1370, y=240)
#======================== creacion mapa y personajes =============================#
    mapa= c.create_image(0, 0, image=mapaimg, anchor=NW)
    mario= c.create_image(500, 665, image=marioimg, anchor=NW)
    luigi= c.create_image(800, 665, image=luimg, anchor=NW)
    POW= c.create_image(750, 450, image=powimg, anchor=NW)
    ene= [[c.create_image(900, 105, image=eneimg, anchor=NW),0]]
    ene.append([c.create_image(1000, 105, image=eneimg5, anchor=NW),3])
    ene.append([c.create_image(400, 105, image=eneimg11, anchor=NW), 9])

    # VIDAS
    livem= [c.create_image(85, 320, image=limg, anchor=NW)]
    livel= [c.create_image(1410, 320, image=limg, anchor=NW)]
    livem.append(c.create_image(45, 320, image=limg, anchor=NW))
    livem.append(c.create_image(125, 320, image=limg, anchor=NW))
    livel.append(c.create_image(1450, 320, image=limg, anchor=NW))
    livel.append(c.create_image(1370, 320, image=limg, anchor=NW))
    if(n==3 or n==4):
        livem.append(c.create_image(5, 320, image=limg, anchor=NW))
        livel.append(c.create_image(1490, 320, image=limg, anchor=NW))
    if(n==5):
        livem.append(c.create_image(5, 320, image=limg, anchor=NW))
        livem.append(c.create_image(165, 320, image=limg, anchor=NW))
        livel.append(c.create_image(1490, 320, image=limg, anchor=NW))
        livel.append(c.create_image(1330, 320, image=limg, anchor=NW))

    c.place(x= 0,y=0)
    # variables
    estado=2
    estadol=2
    esn=True
    ya=False
    q=False
    p=False
    y=False
    u=False
    xyz=False
    m=0
    h=0
    ctm= 0
    cv= 0
    contene=0
    contene2=0
    xz=0

    # aumento de puntuacion mario
    def puntuacion():
        """
        funcion encargada de actualizar la puntuacion de el jugador 1(MARIO)
        entrada: nada
        salida: actualiza la puntuacion cada tiempo cambiandola cada ves que mata a un enemigo
        """
        global caja, caja2, pp1, pp2, puntaje1, punt1, lives, livem, livesl
        puntaje1.destroy()
        punt1= punt1+10
        puntaje1= Label(ventana, text= punt1, bg="black", fg="white", font=("Arial", 25), padx=6,pady=0)
        puntaje1.place(x=60, y=460)
        if(punt1==100):
            lives=lives+1
            livem.append(c.create_image(5, 320, image=limg, anchor=NW))
    # aumento de puntaucion luigi
    def puntuacion2():
        """
        funcion encargada de actualizar la puntuacion de el jugador 2(LUIGI)
        entrada: nada
        salida: actualiza la puntuacion cada tiempo cambiandola cada ves que mata a un enemigo
        """
        global caja, caja2, pp1, pp2, puntaje1, punt1, lives, livem, livesl, puntaje2, punt2
        puntaje2.destroy()
        punt2= punt2+10
        puntaje2= Label(ventana, text= punt2, bg="black", fg="white", font=("Arial", 25), padx=6,pady=0)
        puntaje2.place(x=1400, y=460)
        if(punt2==100):
            livesl=livesl+1
            livel.append(c.create_image(1490, 320, image=limg, anchor=NW))

    # funcion que aparece los enemigos   
    def apareceenemi():
        """
        funcion que se encarga de aparecer un tipo de enemigo aleatoriamente
        entrada: nada
        salida: aparece un tipo de enemigo aleatoriamente
        """  
        global ene, t, z, ctm
        t= random.randint(1,6)

        # Tipos de enemigos a aparecer
        if(t==1):
            ene.append( [c.create_image(1280, 105, image=eneimg3, anchor=NW),3])
            ene.append([c.create_image(1200, 105, image=eneimg, anchor=NW), 0])
        elif(t==2):
            ene.append([c.create_image(1000, 105, image=eneimg5, anchor=NW),5])
            ene.append([c.create_image(1200, 105, image=eneimg9, anchor=NW), 6])
        elif(t==3):
            ene.append([c.create_image(1200, 105, image=eneimg7, anchor=NW), 7])
            ene.append([c.create_image(400, 105, image=eneimg11, anchor=NW), 9])
        elif(t==4):
            ene.append([c.create_image(1200, 105, image=eneimg9, anchor=NW), 6])
            ene.append([c.create_image(1000, 105, image=eneimg5, anchor=NW),5])            
        elif(t==5):
            ene.append([c.create_image(1200, 105, image=eneimg11, anchor=NW), 9])
            ene.append([c.create_image(1200, 105, image=eneimg7, anchor=NW), 7])            
        elif(t==6):
            ene.append([c.create_image(1200, 105, image=eneimg, anchor=NW), 0])
            ene.append( [c.create_image(1280, 105, image=eneimg3, anchor=NW),3])

        ventana.after(30000-z,apareceenemi)

#=========== HONGO =========# 
    def mush():
        """
        funcion que hace aparecer un hongo en el mapa el cual da un poder
        entrada: nada
        salida: aparece hongo en el mapa
        """
        global ctm, st, cv
        ctm+=1
        if(ctm==1):
            st= c.create_image(250, 300, image=muimg, anchor=NW)
        if(c.coords(mario)[0]> c.coords(st)[0]-25 and c.coords(mario)[0]< c.coords(st)[0]+25 and c.coords(mario)[1]> c.coords(st)[1]-30 and c.coords(mario)[1]< c.coords(st)[1]+30):
            cv=40
            c.coords(st, -3000, -3000)
        if(c.coords(luigi)[0]> c.coords(st)[0]-25 and c.coords(luigi)[0]< c.coords(st)[0]+25 and c.coords(luigi)[1]> c.coords(st)[1]-30 and c.coords(luigi)[1]< c.coords(st)[1]+30):
            cv=40
            c.coords(st, -3000, -3000)
        if(ctm==100):
            c.coords(st, -3000, -3000)
            cv=0
        if(ctm==500):
            c.coords(st, 1220, 300)
        if(ctm==600):
            c.coords(st, -3000, -3000)
            cv=0
        ventana.after(100, mush)
  
            
        
#===================== paramentros y acciones de los enemigos =========================#
    def enem():
        """
        funcion encargada de el movimiento de los enemigos y parametros de muerte de mario y cada enemigo
        enrada: nada
        salida: mover al enemigo respectivo o hacerlo morir segun la cituacion
        """
        global esl, xyz, h, POW, punt2, puntaje2, livesl, m, punt1, puntaje1, ene, en, en1, n, esn, lives,contene, xz, x, contene2, esm   
        for o in range(len(ene)):
 
            # golpear tortuga mario
            if((c.coords(mario)[0]> c.coords(ene[o][0])[0]-50 and c.coords(mario)[0]< c.coords(ene[o][0])[0]+50 and c.coords(mario)[1]> c.coords(ene[o][0])[1] and c.coords(mario)[1]< c.coords(ene[o][0])[1]+120 and ene[o][1]!=7 and ene[o][1]!=2 and ene[o][1]!=9) or xyz==True):
                ene[o][1]= 2
                en=c.coords(ene[o][0])[0]
                en1=c.coords(ene[o][0])[1]
                c.delete(ene[o][0])
                ene[o][0]= c.create_image(en, en1, image=eneimg1, anchor=NW)
            # golpear tortuga luigo
            if(c.coords(luigi)[0]> c.coords(ene[o][0])[0]-50 and c.coords(luigi)[0]< c.coords(ene[o][0])[0]+50 and c.coords(luigi)[1]> c.coords(ene[o][0])[1] and c.coords(luigi)[1]< c.coords(ene[o][0])[1]+100 and ene[o][1]!=7 and ene[o][1]!=2 and ene[o][1]!=9):
                ene[o][1]= 2
                en=c.coords(ene[o][0])[0]
                en1=c.coords(ene[o][0])[1]
                c.delete(ene[o][0])
                ene[o][0]= c.create_image(en, en1, image=eneimg1, anchor=NW)
            # morir mario
            if(c.coords(mario)[0]> c.coords(ene[o][0])[0]-25 and c.coords(mario)[0]< c.coords(ene[o][0])[0]+25 and c.coords(mario)[1]> c.coords(ene[o][0])[1]-30 and c.coords(mario)[1]< c.coords(ene[o][0])[1]+30 and ene[o][1]!=2 and esm==True):
                esm=False
                c.coords(mario, 750, 665)
                lives-=1
                if(lives==4):
                    c.delete(livem[len(livem)-1])
                    livem.pop(len(livem)-1)
                if(lives==3):
                    c.delete(livem[len(livem)-1])
                    livem.pop(len(livem)-1)
                if(lives==2):
                    c.delete(livem[len(livem)-1])
                    livem.pop(len(livem)-1)
                if(lives==1):
                    c.delete(livem[len(livem)-1])
                    livem.pop(len(livem)-1)
                if(lives==0):
                    c.delete(livem[len(livem)-1])
                    livem.pop(len(livem)-1)
                    c.coords(mario, -1000, -1000)
            # morir luigi
            if(c.coords(luigi)[0]> c.coords(ene[o][0])[0]-25 and c.coords(luigi)[0]< c.coords(ene[o][0])[0]+25 and c.coords(luigi)[1]> c.coords(ene[o][0])[1]-30 and c.coords(luigi)[1]< c.coords(ene[o][0])[1]+30 and ene[o][1]!=2 and esl==True):
                esl=False
                c.coords(luigi, 750, 665)
                livesl-=1
                if(livesl==4):
                    c.delete(livel[len(livel)-1])
                    livel.pop(len(livel)-1)
                if(livesl==3):
                    c.delete(livel[len(livel)-1])
                    livel.pop(len(livel)-1)
                if(livesl==2):
                    c.delete(livel[len(livel)-1])
                    livel.pop(len(livel)-1)
                if(livesl==1):
                    c.delete(livel[len(livel)-1])
                    livel.pop(len(livel)-1)
                if(livesl==0):
                    c.delete(livel[len(livel)-1])
                    livel.pop(len(livel)-1)
                    c.coords(luigi, -1000, -1000)
            # matar enemigo y puntuacion mario
            if(c.coords(mario)[0]> c.coords(ene[o][0])[0]-45 and c.coords(mario)[0]< c.coords(ene[o][0])[0]+45 and c.coords(mario)[1]> c.coords(ene[o][0])[1]-30 and c.coords(mario)[1]< c.coords(ene[o][0])[1]+30 and ene[o][1]==2):
                 puntuacion()
                 c.delete(ene[o][0])
                 ene.remove(ene[o])
                 break
            if(c.coords(mario)[0]> c.coords(ene[o][0])[0]-45 and c.coords(mario)[0]< c.coords(ene[o][0])[0]+45 and c.coords(mario)[1]> c.coords(ene[o][0])[1] and c.coords(mario)[1]< c.coords(ene[o][0])[1]+100 and (ene[o][1]==7 or ene[o][1]==9)):
                 puntuacion()
                 c.delete(ene[o][0])
                 ene.remove(ene[o])
                 break
            # matar enemigo y puntuacion luigi
            if(c.coords(luigi)[0]> c.coords(ene[o][0])[0]-45 and c.coords(luigi)[0]< c.coords(ene[o][0])[0]+45 and c.coords(luigi)[1]> c.coords(ene[o][0])[1]-30 and c.coords(luigi)[1]< c.coords(ene[o][0])[1]+30 and ene[o][1]==2):
                 puntuacion2()
                 c.delete(ene[o][0])
                 ene.remove(ene[o])
                 break
            if(c.coords(luigi)[0]> c.coords(ene[o][0])[0]-45 and c.coords(luigi)[0]< c.coords(ene[o][0])[0]+45 and c.coords(luigi)[1]> c.coords(ene[o][0])[1] and c.coords(luigi)[1]< c.coords(ene[o][0])[1]+100 and (ene[o][1]==7 or ene[o][1]==9)):
                 puntuacion2()
                 c.delete(ene[o][0])
                 ene.remove(ene[o])
                 break
            # movimiento enemigo 1
            if(ene[o][1]==0):
                en=c.coords(ene[o][0])[0]
                en1=c.coords(ene[o][0])[1]
                c.delete(ene[o][0])
                ene[o][0]= c.create_image(en, en1, image=eneimg, anchor=NW)
                c.move(ene[o][0],-3-x,0)
                ventana.update()
                ventana.after(1)
                ene[o][1]=1
            elif(ene[o][1]==1):
                en=c.coords(ene[o][0])[0]
                en1=c.coords(ene[o][0])[1]
                c.delete(ene[o][0])
                ene[o][0]= c.create_image(en, en1, image=eneimg2, anchor=NW)
                c.move(ene[o][0],-3-x,0)
                ventana.update()
                ventana.after(1)
                ene[o][1]=0
            # moviento enemigo 2
            if(ene[o][1]==3):
                en=c.coords(ene[o][0])[0]
                en1=c.coords(ene[o][0])[1]
                c.delete(ene[o][0])
                ene[o][0]= c.create_image(en, en1, image=eneimg3, anchor=NW)
                c.move(ene[o][0],3+x,0)
                ventana.update()
                ventana.after(1)
                ene[o][1]=4
            elif(ene[o][1]==4):
                en=c.coords(ene[o][0])[0]
                en1=c.coords(ene[o][0])[1]
                c.delete(ene[o][0])
                ene[o][0]= c.create_image(en, en1, image=eneimg4, anchor=NW)
                c.move(ene[o][0],3+x,0)
                ventana.update()
                ventana.after(1)
                ene[o][1]=3
            # movimiento enemigo 3
            if(contene<=5):    
                if(ene[o][1]==5):
                    en=c.coords(ene[o][0])[0]
                    en1=c.coords(ene[o][0])[1]
                    c.delete(ene[o][0])
                    ene[o][0]= c.create_image(en, en1, image=eneimg6, anchor=NW)
                    c.move(ene[o][0],-3-x,-10)
                    ventana.update()
                    ventana.after(1)
                    ene[o][1]=5
                    contene+=1
            elif(contene>=5):
                if(ene[o][1]==5):
                    en=c.coords(ene[o][0])[0]
                    en1=c.coords(ene[o][0])[1]
                    c.delete(ene[o][0])
                    ene[o][0]= c.create_image(en, en1, image=eneimg5, anchor=NW)
                    c.move(ene[o][0],-3-x,10)
                    ventana.update()
                    ventana.after(1)
                    ene[o][1]=5
                    contene+=1
            if(contene==15):
                contene=0
            # movimiento enemigo 4
            if(contene2<=5):    
                if(ene[o][1]==6):
                    en=c.coords(ene[o][0])[0]
                    en1=c.coords(ene[o][0])[1]
                    c.delete(ene[o][0])
                    ene[o][0]= c.create_image(en, en1, image=eneimg9, anchor=NW)
                    c.move(ene[o][0],3+x,-10)
                    ventana.update()
                    ventana.after(1)
                    ene[o][1]=6
                    contene2+=1
            elif(contene2>=5):
                if(ene[o][1]==6):
                    en=c.coords(ene[o][0])[0]
                    en1=c.coords(ene[o][0])[1]
                    c.delete(ene[o][0])
                    ene[o][0]= c.create_image(en, en1, image=eneimg10, anchor=NW)
                    c.move(ene[o][0],3+x,10)
                    ventana.update()
                    ventana.after(1)
                    ene[o][1]=6
                    contene2+=1
            if(contene2==15):
                contene2=0
            # movimiento enemigo 5
            if(ene[o][1]==7):
                    en=c.coords(ene[o][0])[0]
                    en1=c.coords(ene[o][0])[1]
                    c.delete(ene[o][0])
                    ene[o][0]= c.create_image(en, en1, image=eneimg7, anchor=NW)
                    c.move(ene[o][0],-9-x,0)
                    ventana.update()
                    ventana.after(1)
            if(ene[o][1]==9):
                    ca=c.coords(ene[o][0])[0]
                    ca1=c.coords(ene[o][0])[1]
                    c.delete(ene[o][0])
                    ene[o][0]= c.create_image(ca, ca1, image=eneimg11, anchor=NW)
                    c.move(ene[o][0],9+x,0)
                    ventana.update()
                    ventana.after(1)
        ventana.after(85-y, enem)


#============= POW ===============#
    def POWW():
        """
        funcuin que se encarga de hacer aparecer y funcionar al POW el cual es un cubo que voltea a todos los enemigos en el mapa
        entrada: nada
        salida: al golpearse se voltean todos los enemigos presentes en el mapa
        """
        global h, POW, mario, xyz
        xyz=False
        # Golpe 3
        if((h==2 and c.coords(luigi)[0]> c.coords(POW)[0]-50 and c.coords(luigi)[0]< c.coords(POW)[0]+50 and c.coords(luigi)[1]> c.coords(POW)[1]-50 and c.coords(luigi)[1]< c.coords(POW)[1]+100) or (h==2 and c.coords(mario)[0]> c.coords(POW)[0]-50 and c.coords(mario)[0]< c.coords(POW)[0]+50 and c.coords(mario)[1]> c.coords(POW)[1]-50 and c.coords(mario)[1]< c.coords(POW)[1]+100)):
            c.coords(POW, -2000, -2000)
            xyz=True
            h+=1
        # Golpe 2
        elif((h==1 and c.coords(luigi)[0]> c.coords(POW)[0]-50 and c.coords(luigi)[0]< c.coords(POW)[0]+50 and c.coords(luigi)[1]> c.coords(POW)[1]-50 and c.coords(luigi)[1]< c.coords(POW)[1]+100) or (h==1 and c.coords(mario)[0]> c.coords(POW)[0]-50 and c.coords(mario)[0]< c.coords(POW)[0]+50 and c.coords(mario)[1]> c.coords(POW)[1]-50 and c.coords(mario)[1]< c.coords(POW)[1]+100)):
            c.delete(POW)
            POW= c.create_image(750, 450, image=powimg3, anchor=NW)
            xyz=True
            h+=1
        # Golpe 1
        elif((h==0 and c.coords(luigi)[0]> c.coords(POW)[0]-50 and c.coords(luigi)[0]< c.coords(POW)[0]+50 and c.coords(luigi)[1]> c.coords(POW)[1]-50 and c.coords(luigi)[1]< c.coords(POW)[1]+100) or (h==0 and c.coords(mario)[0]> c.coords(POW)[0]-50 and c.coords(mario)[0]< c.coords(POW)[0]+50 and c.coords(mario)[1]> c.coords(POW)[1]-50 and c.coords(mario)[1]< c.coords(POW)[1]+100)):
            c.delete(POW)
            POW= c.create_image(750, 450, image=powimg2, anchor=NW)
            xyz=True
            h+=1
        ventana.after(30, POWW)



#=====MOVER MARIO=====#
    def movermario():
        """
        funcion encargada de mover a mario hacia la derecha o izquierda dependiendo de el boton presionado
        entrada: nada
        salida: mario se muve hacia la direccion indicada 
        """
        global estado, mario, q, a, te, te1,p, esm, yatu, cv, esl
        
#=================== mover izquierda mario =====================#
        # direccion
        if(yatu['Left']==True and q==False):
           esm=True
           te=c.coords(mario)[0]
           te1=c.coords(mario)[1]
           c.delete(mario)
           mario= c.create_image(te, te1, image=marioimg2, anchor=NW)
           c.move(mario,-3,0)
           ventana.update()
           ventana.after(2)
           estado=1
           q=True
        # animacion
        elif(yatu['Left']==True and q==True):
            esm=True
            if(p==False):
               te=c.coords(mario)[0]
               te1=c.coords(mario)[1]
               c.delete(mario)
               mario= c.create_image(te, te1, image=marioimg2, anchor=NW)
               c.move(mario,-9,0)
               ventana.update()
               ventana.after(2)
               estado=1
               p=True
            elif(p==True):
               te=c.coords(mario)[0]
               te1=c.coords(mario)[1]
               c.delete(mario)
               mario= c.create_image(te, te1, image=marioimg3, anchor=NW)
               c.move(mario,-9,0)
               ventana.update()
               ventana.after(2)
               estado=1
               p=False
                
        
        
          


           
#=================== mover derecha mario =======================#
        # direccion
        elif(yatu['Right']==True and q==True):
           esm=True
           te=c.coords(mario)[0]
           te1=c.coords(mario)[1]
           c.delete(mario)
           mario= c.create_image(te, te1, image=marioimg, anchor=NW)
           c.move(mario,9,0)
           ventana.update()
           ventana.after(2)
           estado=3
           q=False
        # animcaion
        elif(yatu['Right']==True and q==False):
          esm=True
          if(p==False):
               te=c.coords(mario)[0]
               te1=c.coords(mario)[1]
               c.delete(mario)
               mario= c.create_image(te, te1, image=marioimg, anchor=NW)
               c.move(mario,9,0)
               ventana.update()
               ventana.after(2)
               estado=3
               p=True
          elif(p==True):
               te=c.coords(mario)[0]
               te1=c.coords(mario)[1]
               c.delete(mario)
               mario= c.create_image(te, te1, image=marioimg4, anchor=NW)
               c.move(mario,9,0)
               ventana.update()
               ventana.after(2)
               estado=3
               p=False
               
            
          
        
        ventana.after(50-cv, movermario)


#=====MOVER LUIGI=====#  
    def moverluigi():
        """
        funcion encargada de mover a luigi hacia la derecha o izquierda dependiendo de el boton presionado
        entrada: nada
        salida: luigi se muve hacia la direccion indicada 
        """
        global estado, mario, q, a, te, te1,p, esm, luigi, yatu, estadol, y, u, cv, esl
        
#=========================== mover izquierda luigi ==============================#
        # Direccion
        if(yatu['a']==True and y==False):
           esl=True
           te=c.coords(luigi)[0]
           te1=c.coords(luigi)[1]
           c.delete(luigi)
           luigi= c.create_image(te, te1, image=luimg, anchor=NW)
           c.move(luigi,-3,0)
           ventana.update()
           ventana.after(2)
           estadol=1
           y=True
        # Animacion
        elif(yatu['a']==True and y==True):
            esl=True
            if(u==False):
               te=c.coords(luigi)[0]
               te1=c.coords(luigi)[1]
               c.delete(luigi)
               luigi= c.create_image(te, te1, image=luimg3, anchor=NW)
               c.move(luigi,-9,0)
               ventana.update()
               ventana.after(2)
               estadol=1
               u=True
            elif(u==True):
               te=c.coords(luigi)[0]
               te1=c.coords(luigi)[1]
               c.delete(luigi)
               luigi= c.create_image(te, te1, image=luimg, anchor=NW)
               c.move(luigi,-9,0)
               ventana.update()
               ventana.after(2)
               estadol=1
               u=False
            
        
          


           
#=================== mover derecha luigi ======================#
        # Direccion
        elif(yatu['d']==True and y==True):
           esl=True
           te=c.coords(luigi)[0]
           te1=c.coords(luigi)[1]
           c.delete(luigi)
           luigi= c.create_image(te, te1, image=luimg2, anchor=NW)
           c.move(luigi,9,0)
           ventana.update()
           ventana.after(2)
           estadol=3
           y=False
        # Animacion
        elif(yatu['d']==True and y==False):
          esl=True
          if(u==False):
               te=c.coords(luigi)[0]
               te1=c.coords(luigi)[1]
               c.delete(luigi)
               luigi= c.create_image(te, te1, image=luimg4, anchor=NW)
               c.move(luigi,9,0)
               ventana.update()
               ventana.after(2)
               estadol=3
               u=True
          elif(u==True):
               te=c.coords(luigi)[0]
               te1=c.coords(luigi)[1]
               c.delete(luigi)
               luigi= c.create_image(te, te1, image=luimg2, anchor=NW)
               c.move(luigi,9,0)
               ventana.update()
               ventana.after(2)
               estadol=3
               u=False
               
            
          
        ventana.after(50-cv, moverluigi)





#===================== SALTO MARIO ======================#  
    def salto():
        """
        funcion encargada de hacer saltar a mario en distintas direcciones dependido de su estado de direccion
        entrada: nada
        salida: mario salta hacia la direccion definida 
        """
        global estado, mario, q, a, te, te1,p, ya, esm
        if(yatu['Up']==True and ya == False):
            esm=True
            ya=True
            # salto arriba
            if(estado==2):
                contador=0
                contador2=0
                while(contador<20):
                    te=c.coords(mario)[0]
                    te1=c.coords(mario)[1]
                    c.delete(mario)
                    mario= c.create_image(te, te1, image=marioimg5, anchor=NW)
                    c.move(mario,0,-12)
                    ventana.update()
                    ventana.after(2)
                    contador+=1
                while(contador2<23):
                    c.move(mario,0,12)
                    ventana.update()
                    ventana.after(2)
                    contador2+=1
                te=c.coords(mario)[0]
                te1=c.coords(mario)[1]
                c.delete(mario)
                mario= c.create_image(te, te1, image=marioimg, anchor=NW)
                estado=2
                ya=False
            # salto derecha
            elif(estado == 3):
                    contador=0
                    contador2=0
                    contador3=0
                    while(contador<20):
                        te=c.coords(mario)[0]
                        te1=c.coords(mario)[1]
                        c.delete(mario)
                        mario= c.create_image(te, te1, image=marioimg5, anchor=NW)
                        c.move(mario,4,-12)
                        ventana.after(2)
                        ventana.update()
                        contador+=1
                    while(contador2<23):
                        c.move(mario,4,12)
                        ventana.update()
                        ventana.after(2)
                        contador2+=1
                    while(contador3<3):
                        c.move(mario,0,12)
                        ventana.after(2)
                        ventana.update()
                        contador3+=1
                    te=c.coords(mario)[0]
                    te1=c.coords(mario)[1]
                    c.delete(mario)
                    mario= c.create_image(te, te1, image=marioimg, anchor=NW)
                    estado=2
                    ya = False
                    while(contador<20):
                        c.move(mario,0,12)
                        ventana.after(2)
                        ventana.update()
                        contador3+=1
            # saltar izquierda
            elif(estado == 1): 
                contador4=0
                contador5=0
                contador6=0
                while(contador4<20):
                    te=c.coords(mario)[0]
                    te1=c.coords(mario)[1]
                    c.delete(mario)
                    mario= c.create_image(te, te1, image=marioimg6, anchor=NW)
                    c.move(mario,-4,-12)
                    ventana.update()
                    ventana.after(2)
                    contador4+=1
                while(contador5<23):
                    c.move(mario,-4,12)
                    ventana.update()
                    ventana.after(2)
                    contador5+=1
                while(contador6<3):
                    c.move(mario,0,12)
                    ventana.after(2)
                    ventana.update()
                    contador6+=1
                te=c.coords(mario)[0]
                te1=c.coords(mario)[1]
                c.delete(mario)
                mario= c.create_image(te, te1, image=marioimg2, anchor=NW)
                estado=2
                ya = False

        ventana.after(50, salto)



#======================= SALTO LUIGI ==========================#  
    def saltol():
        """
        funcion encargada de hacer saltar a luigi en distintas direcciones dependido de su estado de direccion
        entrada: nada
        salida: mario salta hacia la direccion definida 
        """
        global estado, mario, q, a, te, te1,p, ya, esm, luigi, estadol
        if(yatu['w']==True and ya == False):
            esm=True
            ya=True
            # salto arriba luigi
            if(estadol==2):
                contador=0
                contador2=0
                # Ascenso
                while(contador<20):
                    te=c.coords(luigi)[0]
                    te1=c.coords(luigi)[1]
                    c.delete(luigi)
                    luigi= c.create_image(te, te1, image=luimg5, anchor=NW)
                    c.move(luigi,0,-12)
                    ventana.update()
                    ventana.after(2)
                    contador+=1
                # Descenso
                while(contador2<23):
                    c.move(luigi,0,12)
                    ventana.update()
                    ventana.after(2)
                    contador2+=1
                te=c.coords(luigi)[0]
                te1=c.coords(luigi)[1]
                c.delete(luigi)
                luigi= c.create_image(te, te1, image=luimg2, anchor=NW)
                estadol=2
                ya=False
            # salto derecha luigi
            elif(estadol == 3):
                    contador=0
                    contador2=0
                    contador3=0
                    # Ascenso
                    while(contador<20):
                        te=c.coords(luigi)[0]
                        te1=c.coords(luigi)[1]
                        c.delete(luigi)
                        luigi= c.create_image(te, te1, image=luimg5, anchor=NW)
                        c.move(luigi,4,-12)
                        ventana.update()
                        ventana.after(2)
                        contador+=1
                    # Descenso
                    while(contador2<23):
                        c.move(luigi,4,12)
                        ventana.update()
                        ventana.after(2)
                        contador2+=1
                    while(contador3<3):
                        c.move(luigi,0,12)
                        ventana.update()
                        ventana.after(2)
                        contador3+=1
                    te=c.coords(luigi)[0]
                    te1=c.coords(luigi)[1]
                    c.delete(luigi)
                    luigi= c.create_image(te, te1, image=luimg2, anchor=NW)
                    estadol=2
                    ya = False
                    while(contador<20):
                        c.move(luigi,0,12)
                        ventana.after(2)
                        ventana.update()
                        contador3+=1
            # saltar izquierda luigi
            elif(estadol == 1): 
                contador4=0
                contador5=0
                contador6=0
                # Ascenso
                while(contador4<20):
                    te=c.coords(luigi)[0]
                    te1=c.coords(luigi)[1]
                    c.delete(luigi)
                    luigi= c.create_image(te, te1, image=luimg6, anchor=NW)
                    c.move(luigi,-4,-12)
                    ventana.update()
                    ventana.after(2)
                    contador4+=1
                # Descenso
                while(contador5<23):
                    c.move(luigi,-4,12)
                    ventana.update()
                    ventana.after(2)
                    contador5+=1
                while(contador6<3):
                    c.move(luigi,0,12)
                    ventana.after(2)
                    ventana.update()
                    contador6+=1
                te=c.coords(luigi)[0]
                te1=c.coords(luigi)[1]
                c.delete(luigi)
                luigi= c.create_image(te, te1, image=luimg, anchor=NW)
                estadol=2
                ya = False

        ventana.after(50, saltol)


#========== FUNCION ESTADO DE SALTO ==========#
    def para():
        """
        funcion que mantiene la direccion de salto tanto como para mario como para luigi
        entrada: nada
        salida: actualiza el esado de cada uno cada 500 milesimas
        """
        global estado, estadol
        estado=2
        estadol=2
        ventana.after(500,para)



#============== FUNCIONES TECLAS =============# 
    def tec(event):
        """
        funcion que identifica que tecla se esta presionando para haci denifir que accion hacer
        entrada: nada
        salida: identifica la tecla y la asigna 
        """
        global yatu
        pre = event.keysym
        let=['Up','Right','Left', 'w','a','d',]
        if (pre in let):
                yatu[pre]=True

    def ntec(event):
        """
        funcion que detecta una tecla que se acada de dejar de usar
        entrada: nada
        salida: entrega la tecla liberda
        """
        global yatu
        pre = event.keysym
        let=['Up','Right','Left', 'w','a','d']
        if (pre in let):
                yatu[pre]=False
        
#============ PARAMETROS DE CHOQUES Y CAIDAS ==============#
    def conti():
        """
        funcion que se encarga de definir los parametros de choques y caidas para cada personaje y enemigo del juego
        entrada: nada
        salida: hace que choque o caiga un individuo dependiendo de la cituacion
        """
        global estado, lives, en, en1, ene, esn
        # mapa continuo
        if(c.coords(mario)[0]>1287):
            te=c.coords(mario)[1]
            c.coords(mario, 216,te)
        if(c.coords(mario)[0]<212):
            te=c.coords(mario)[1]
            c.coords(mario, 1283,te)
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
            while(contador7<25):
                c.move(mario,0,10)
                ventana.update()
                time.sleep(0.0001)
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
                time.sleep(0.0001)
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
                time.sleep(0.0001)
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
                time.sleep(0.0001)
                contador9+=1
        # plataforma 7
        elif(c.coords(mario)[1]<198 and c.coords(mario)[1]>164 and c.coords(mario)[0]>810):
            te=c.coords(mario)[0]
            c.coords(mario,te,198)
        elif(c.coords(mario)[1]<198 and c.coords(mario)[1]>85 and c.coords(mario)[0]>810):
            te=c.coords(mario)[0]
            c.coords(mario,te,85)


        # mapa continuo luigi
        if(c.coords(luigi)[0]>1287):
            te=c.coords(luigi)[1]
            c.coords(luigi, 216,te)
        if(c.coords(luigi)[0]<212):
            te=c.coords(luigi)[1]
            c.coords(luigi, 1283,te)
        # suelo luigi
        if(c.coords(luigi)[1]>665):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,665)
        # plataforma 1 luigi
        elif(c.coords(luigi)[1]<583 and c.coords(luigi)[1]>552 and c.coords(luigi)[0]>912):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,583)
        elif(c.coords(luigi)[0]>912 and c.coords(luigi)[1]>472 and c.coords(luigi)[1]<583):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,472)
        # caida 1 luigi
        elif(c.coords(luigi)[0]<912 and c.coords(luigi)[0]>588 and c.coords(luigi)[1]==472):
            te=c.coords(luigi)[0]
            contador7=0
            while(contador7<25):
                c.move(luigi,0,10)
                ventana.update()
                time.sleep(0.0001)
                contador7+=1
        # plataforma 2 luigi
        elif(c.coords(luigi)[1]<583 and c.coords(luigi)[1]>565 and c.coords(luigi)[0]<588):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,583)
        elif(c.coords(luigi)[0]<588 and c.coords(luigi)[1]>472 and c.coords(luigi)[1]<583):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,472)
        # plataforma 3 luigi
        elif(c.coords(luigi)[1]<390 and c.coords(luigi)[1]>358 and c.coords(luigi)[0]<347):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,390)
        elif(c.coords(luigi)[1]<390 and c.coords(luigi)[1]>278 and c.coords(luigi)[0]<347):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,278)
        # caida 2 luigi
        elif(c.coords(luigi)[0]>347 and c.coords(luigi)[0]<466 and c.coords(luigi)[1]==278):
            te=c.coords(luigi)[0]
            contador7=0
            while(contador7<25):
                c.move(luigi,0,10)
                ventana.update()
                time.sleep(0.0001)
                contador7+=1
        # plataforma 4 luigi
        elif(c.coords(luigi)[1]<390 and c.coords(luigi)[1]>358 and c.coords(luigi)[0]<1037 and c.coords(luigi)[0]>466):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,390)
        elif(c.coords(luigi)[1]<390 and c.coords(luigi)[1]>278 and c.coords(luigi)[0]>466 and c.coords(luigi)[0]<1037):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,278)
        # caida 3 luigi
        elif(c.coords(luigi)[0]>1037 and c.coords(luigi)[0]<1154 and c.coords(luigi)[1]==278):
            te=c.coords(luigi)[0]
            contador8=0
            while(contador8<25):
                c.move(luigi,0,10)
                ventana.update()
                time.sleep(0.0001)
                contador8+=1
        # plataforma 5 luigi
        elif(c.coords(luigi)[1]<390 and c.coords(luigi)[1]>358 and c.coords(luigi)[0]>1154):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,390)
        elif(c.coords(luigi)[1]<390 and c.coords(luigi)[1]>278 and c.coords(luigi)[0]>1154):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,278)
        # plataforma 6 luigi
        elif(c.coords(luigi)[1]<198 and c.coords(luigi)[1]>164 and c.coords(luigi)[0]<692):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,198)
        elif(c.coords(luigi)[1]<198 and c.coords(luigi)[1]>83 and c.coords(luigi)[0]<692):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,85)
        # caida 4 luigi
        elif(c.coords(luigi)[0]>692 and c.coords(luigi)[0]<810 and c.coords(luigi)[1]==85):
            te=c.coords(luigi)[0]
            contador9=0
            while(contador9<25):
                c.move(luigi,0,10)
                ventana.update()
                time.sleep(0.0001)
                contador9+=1
        # plataforma 7 luigi
        elif(c.coords(luigi)[1]<198 and c.coords(luigi)[1]>164 and c.coords(luigi)[0]>810):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,198)
        elif(c.coords(luigi)[1]<198 and c.coords(luigi)[1]>85 and c.coords(luigi)[0]>810):
            te=c.coords(luigi)[0]
            c.coords(luigi,te,85)

      
        # mapa continuo tortuga
        for o in range(len(ene)):
            if(c.coords(ene[o][0])[0]>1287 and c.coords(ene[o][0])[1]<= 500):
                te=c.coords(ene[o][0])[1]
                c.coords(ene[o][0], 220,te)
            if(c.coords(ene[o][0])[0]<212 and c.coords(ene[o][0])[1]<= 500):
                te=c.coords(ene[o][0])[1]
                c.coords(ene[o][0], 1283,te)
            if(c.coords(ene[o][0])[0]>1287 and c.coords(ene[o][0])[1]>= 500):
                c.coords(ene[o][0], 220,105)
            if(c.coords(ene[o][0])[0]<212 and c.coords(ene[o][0])[1]>= 500):
                c.coords(ene[o][0], 1283,105)
            
            # suelo tortuga
            if(c.coords(ene[o][0])[1]>685):
                te=c.coords(ene[o][0])[0]
                c.coords(ene[o][0],te,685)
            # plataforma 1 tortuga
            elif(c.coords(ene[o][0])[0]>912 and c.coords(ene[o][0])[1]>492 and c.coords(ene[o][0])[1]<603):
                te=c.coords(ene[o][0])[0]
                c.coords(ene[o][0],te,492)
            # caida 1 tortuga
            elif(c.coords(ene[o][0])[0]<912 and c.coords(ene[o][0])[0]>588 and c.coords(ene[o][0])[1]==492):
                te=c.coords(ene[o][0])[0]
                contador7=0
                while(contador7<40):
                    c.move(ene[o][0],0,10)
                    ventana.update()
                    time.sleep(0.0001)
                    contador7+=1
            # plataforma 2 tortuga
            elif(c.coords(ene[o][0])[0]<588 and c.coords(ene[o][0])[1]>492 and c.coords(ene[o][0])[1]<603):
                te=c.coords(ene[o][0])[0]
                c.coords(ene[o][0],te,492)
            # plataforma 3 tortuga
            elif(c.coords(ene[o][0])[1]<410 and c.coords(ene[o][0])[1]>298 and c.coords(ene[o][0])[0]<347):
                te=c.coords(ene[o][0])[0]
                c.coords(ene[o][0],te,298)
            # caida 2 tortuga
            elif(c.coords(ene[o][0])[0]>347 and c.coords(ene[o][0])[0]<466 and c.coords(ene[o][0])[1]==298):
                te=c.coords(ene[o][0])[0]
                contador7=0
                while(contador7<25):
                    c.move(ene[o][0],0,10)
                    ventana.update()
                    time.sleep(0.0001)
                    contador7+=1
            # plataforma 4 tortuga
            elif(c.coords(ene[o][0])[1]<410 and c.coords(ene[o][0])[1]>298 and c.coords(ene[o][0])[0]>466 and c.coords(ene[o][0])[0]<1037):
                te=c.coords(ene[o][0])[0]
                c.coords(ene[o][0],te,298)
            # caida 3 tortuga
            elif(c.coords(ene[o][0])[0]>1037 and c.coords(ene[o][0])[0]<1154 and c.coords(ene[o][0])[1]==298):
                te=c.coords(ene[o][0])[0]
                contador8=0
                while(contador8<25):
                    c.move(ene[o][0],0,10)
                    ventana.update()
                    time.sleep(0.0001)
                    contador8+=1
            # plataforma 5 tortuga
            elif(c.coords(ene[o][0])[1]<410 and c.coords(ene[o][0])[1]>298 and c.coords(ene[o][0])[0]>1154):
                te=c.coords(ene[o][0])[0]
                c.coords(ene[o][0],te,298)
            # plataforma 6 tortuga
            elif(c.coords(ene[o][0])[1]<218 and c.coords(ene[o][0])[1]>103 and c.coords(ene[o][0])[0]<692):
                te=c.coords(ene[o][0])[0]
                c.coords(ene[o][0],te,105)
            # caida 4 tortuga
            elif(c.coords(ene[o][0])[0]>692 and c.coords(ene[o][0])[0]<810 and c.coords(ene[o][0])[1]==105):
                te=c.coords(ene[o][0])[0]
                contador9=0
                while(contador9<25):
                    c.move(ene[o][0],0,10)
                    ventana.update()
                    time.sleep(0.0001)
                    contador9+=1
            # plataforma 7 tortuga
            elif(c.coords(ene[o][0])[1]<218 and c.coords(ene[o][0])[1]>105 and c.coords(ene[o][0])[0]>810):
                te=c.coords(ene[o][0])[0]
                c.coords(ene[o][0],te,105)
        ventana.after(1, conti)
        
#=========== GUARDAR ============#
    def guardar(event):
        """
        funcion que guarda la partida tomando los valores nesezarios para su posterior carga
        entrada: nada
        salida: guarda los valores al presionar una tecla 
        """
        global pp1, pp2, punt1, punt2
        inf= [pp1,"\n", pp2, "\n", str(punt1), "\n", str(punt2)]
        g= open("partida.txt", "w")
        g.writelines(inf)
        g.close()
        print("melo")




#====== Llamado funciones ======#
    movermario()
    moverluigi()
    salto()
    saltol()
    conti()
    apareceenemi()
    enem()
    para()
    POWW()
    mush()
#============== Teclado ==============#
    c.bind_all("<KeyPress>",tec)
    c.bind_all("<KeyRelease>",ntec)
    c.bind_all("<KeyPress-g>", guardar)
    c.bind_all("<KeyPress-l>", loade)

    


#===== LOOP ======#
ventana.mainloop()

##c.bind_all("<KeyPress-Down>", movermario)
#http://www.mariouniverse.com/sprites/snes/smb3
#http://www.mariowiki.com/Gallery:Super_Mario_Bros._3#Mario






