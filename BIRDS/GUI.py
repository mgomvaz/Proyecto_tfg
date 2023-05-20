from tkinter import *
from Facebook import login
from Twitter import nube_palabras,opinion_tema
from pymongo import MongoClient
from PIL import Image, ImageTk
from lxml.html.builder import LI
import tkinter.font as tkFont

url = 'mongodb://localhost:27017'

class PaginaPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("BIRDS")
        master.geometry("800x300")
        master.resizable(False, False)
        fondo='azure'
        master.configure(bg=fondo)
        fuente =tkFont.Font(family="Helvetica ", size=20, weight="bold", slant="italic")

        self.titulo = Label(master,bg=fondo,fg='gray27',font=fuente, text="Seleccione la red social con la que quiera investigar")
        self.titulo.pack(fill=X)
        
        self.imagen = Image.open("img/facebook.png")
        #self.imagen = Image.open(r"TFG/img/facebook.png")
        #self.imagen = Image.open("TFG_miggomvaz_/TFG_miggomvaz/TFG/TFG/img/facebook.png")
        self.n = self.imagen.resize((100,100))
        self.imagen_tk = ImageTk.PhotoImage(self.n)
        self.boton_pagina1 = Button(master,bg=fondo,image=self.imagen_tk, command=self.abrir_pagina1)
        self.boton_pagina1.pack(side="left", padx=50)
        
        
        self.imagen2 =Image.open("img/signo-de-twitter.png")
        self.n2 = self.imagen2.resize((100, 100))
        self.imagen_tk2 = ImageTk.PhotoImage(self.n2)
        self.boton_pagina2 = Button(master,bg=fondo,image=self.imagen_tk2, command=self.abrir_pagina2)
        self.boton_pagina2.pack(side="right", padx=50)
        
    def abrir_pagina1(self):
        self.master.withdraw()
        pagina1 = Toplevel(self.master)
        Pagina1(pagina1)

    def abrir_pagina2(self):
        self.master.withdraw()
        pagina2 = Toplevel(self.master)
        Pagina2(pagina2)

class Pagina1:        
    def __init__(self, master):
        fuente =tkFont.Font(family="Helvetica ", size=20, weight="bold", slant="italic")  
        fuente1= tkFont.Font(family="Helvetica ", size=13, slant="italic")
        self.master = master
        master.geometry("800x300")
        master.resizable(False, False)
        fondo='azure'
        master.iconbitmap("img/logo_birds.ico")
        master.configure(bg=fondo)
        master.title("Facebook")

        self.titulo = Label(master,fg='gray27',bg=fondo,font=fuente, text="Investigar Facebook")
        self.titulo.pack(pady=10)
        
        self.etiqueta = Label(master,fg='gray27',bg=fondo,font=fuente1, text="Persona que buscamos:")
        self.etiqueta.pack()

        # Crea una entrada de texto y la coloca en la ventana
        self.entrada_texto = Entry(master)
        self.entrada_texto.pack()
        
        
        self.etiqueta1 = Label(master,fg='gray27',bg=fondo,font=fuente1, text="Tu Correo:")
        self.etiqueta1.pack()

        # Crea una entrada de texto y la coloca en la ventana
        self.correo = Entry(master)
        self.correo.pack()
        
        
        
        
        self.etiqueta2 = Label(master,fg='gray27',bg=fondo,font=fuente1, text="Contraseña:")
        self.etiqueta2.pack()

        # Crea una entrada de texto y la coloca en la ventana
        self.pw = Entry(master,show="*" )
        self.pw.pack()
        
        
                
        self.boton = Button(master, text="Investigarla", command=self.abrir_pagina31)
        self.boton.pack(pady=5)
    

        self.boton_volver = Button(master, text="Volver a la página principal", command=self.volver_pagina_principal)
        self.boton_volver.pack(padx=20,anchor='sw')

    def volver_pagina_principal(self):
        self.master.destroy()
        root.deiconify()
        

    def abrir_pagina31(self):
        self.texto = self.entrada_texto.get()
        self.correo = self.correo.get()
        self.pw = self.pw.get()
        self.master.withdraw()
        pagina31 = Toplevel(self.master)
        Pagina31(pagina31,self.texto,self.correo,self.pw)        

class Pagina31:

    def __init__(self, master,nombre,correo,pw):      
        self.master = master
        fondo='azure'
        master.configure(bg=fondo)
        master.iconbitmap("img/logo_birds.ico")
        master.title("Datos Facebook")

        self.titulo = Label(master,bg=fondo,font="Helvetica", text="Datos de "+nombre)
        self.titulo.grid(pady=10,row=0)
        
        dbName = 'TFG'
        collectionName = 'facebook'
        client = MongoClient(url)
        db = client[dbName]
        collection = db[collectionName]
        resultado = collection.find_one({"Face_id": nombre}) 
        dato=None
        if(resultado):
            dato=resultado
        else:
            dato=login(str(correo),str(pw),nombre)
            if(dato=="error"):
                self.error = Label(master,bg=fondo, text="Vuelva a poner el usuario y contraseña") 
                self.error.grid(pady=5,padx=5)
                
                self.boton_volver2 = Button(master, text="Atras", command=self.abrir_pagina1)
                self.boton_volver2.grid(padx=20)
            else:
                collection.insert_one(dato)
                    
        self.dato2 = Label(master,bg=fondo, text=dato["Face_id"]) 
        self.dato2.grid(pady=5,padx=5)
        
        self.dato3 = Label(master,bg=fondo, text="nombre: "+dato["nombre"]) 
        self.dato3.grid(pady=5,padx=5)
        
        self.dato4 = Label(master,bg=fondo, text="trabajo: "+dato["trabajo"]) 
        self.dato4.grid(pady=5,padx=5)
        
        self.dato5 = Label(master,bg=fondo, text="estudio: "+dato["estudio"]) 
        self.dato5.grid(pady=5,padx=5)
        
        self.dato6 = Label(master,bg=fondo, text="nace: "+dato["nace"]) 
        self.dato6.grid(pady=5,padx=5)
        
        self.dato7 = Label(master,bg=fondo, text="pareja: "+dato["pareja"]) 
        self.dato7.grid(pady=5,padx=5)
        
        self.dato8 = Label(master,bg=fondo, text="estado_civil: "+dato["estado_civil"]) 
        self.dato8.grid(pady=5,padx=5)
        
        trabajos=dato["trabajos"]
        try:
            self.dato9 = Label(master,bg=fondo, text="trabajos: "+trabajos[0]) 
            self.dato9.grid(pady=5,padx=5)
        except:pass
        
        try:
            self.dato91 = Label(master,bg=fondo, text="trabajos: "+trabajos[0]) 
            self.dato91.grid(pady=5,padx=5)
        except:pass
        
        try:
            self.dato92 = Label(master,bg=fondo, text="trabajos: "+trabajos[0]) 
            self.dato92.grid(pady=5,padx=5)
        except:pass
        
        
        universidades=dato["universidades"]
        try:
            self.dato10 = Label(master,bg=fondo, text="universidad: "+universidades[0]) 
            self.dato10.grid(pady=5,padx=5)
        except:pass
        
        try:
            self.dato101 = Label(master,bg=fondo, text="universidad: "+universidades[1]) 
            self.dato101.grid(pady=5,padx=5)
        except:pass
        
        try:
            self.dato102 = Label(master,bg=fondo, text="universidad: "+universidades[2]) 
            self.dato102.grid(pady=5,padx=5)
        except:pass
        
        
        lugares=dato["pl"]
        try:
            self.dato11 = Label(master,bg=fondo, text="sitio: "+lugares[0]) 
            self.dato11.grid(pady=5,padx=5)
        except:pass
        
        try:
            self.dato111 = Label(master,bg=fondo, text="sitio: "+lugares[1]) 
            self.dato111.grid(pady=5,padx=5)
        except:pass
        
        try:
            self.dato112 = Label(master,bg=fondo, text="sitio: "+lugares[2]) 
            self.dato112.grid(pady=5,padx=5)
        except:pass

        
        self.dato12 = Label(master,bg=fondo, text="redes sociales: "+dato["red"]) 
        self.dato12.grid(pady=5,padx=5)
        
        self.dato13 = Label(master,bg=fondo, text="genero: "+dato["genero"]) 
        self.dato13.grid(pady=5,padx=5)
        
        self.dato14 = Label(master,bg=fondo, text="cumpleaños: "+dato["cumpleaños"]) 
        self.dato14.grid(pady=5,padx=5)
        
        self.dato14= Label(master,bg=fondo, text="año nacimineto: "+dato["año"]) 
        self.dato14.grid(pady=5,padx=5)
        
        self.dato15  = Label(master,bg=fondo, text="Ultimas fotos: ") 
        self.dato15.grid(pady=5,padx=5)
        
        fotos=dato["fo"]
        
        try:
            self.imagen = Image.open(fotos[0])
            self.n = self.imagen.resize((100,100))
            self.imagen_tk = ImageTk.PhotoImage(self.n)       
            self.dato16  = Label(master,bg=fondo,image=self.imagen_tk, text="fotos: "+fotos[0]) 
            self.dato16.grid(pady=5,padx=5)
        except:pass
        
        try:
            self.imagen1 = Image.open(fotos[1])
            self.n1 = self.imagen1.resize((100,100))
            self.imagen_tk1 = ImageTk.PhotoImage(self.n1)       
            self.dato17  = Label(master,bg=fondo,image=self.imagen_tk1, text="fotos: "+fotos[1]) 
            self.dato17.grid(pady=5,padx=5)
        except:pass
        
        try:
            self.imagen2 = Image.open(fotos[2])
            self.n1 = self.imagen2.resize((100,100))
            self.imagen_tk2 = ImageTk.PhotoImage(self.n1)       
            self.dato18  = Label(master,bg=fondo,image=self.imagen_tk2, text="fotos: "+fotos[2]) 
            self.dato18.grid(pady=5,padx=5)
        except:pass

          
        self.boton_volver = Button(master, text="Atras", command=self.abrir_pagina1)
        self.boton_volver.grid(padx=20)
        

    def abrir_pagina1(self):
        self.master.withdraw()
        pagina1 = Toplevel(self.master)
        Pagina1(pagina1)

class Pagina2:
    def __init__(self, master):
        self.master = master
        master.geometry("800x300")
        master.resizable(False, False)
        fuente=tkFont.Font(family="Helvetica ", size=20, weight="bold", slant="italic") 
        fuente1= tkFont.Font(family="Helvetica ", size=13, slant="italic") 
        fondo='azure'
        master.iconbitmap("img/logo_birds.ico")
        master.title("Twitter")
        master.configure(bg=fondo)
        self.titulo = Label(master,fg='gray27',bg=fondo,font=fuente, text="Investigar Twitter")
        self.titulo.pack()
        
        self.etiqueta = Label(master,bg=fondo,font=fuente1, text="Persona que buscamos:")
        self.etiqueta.pack(anchor="center")

        # Crea una entrada de texto y la coloca en la ventana
        self.entrada_texto = Entry(master)
        self.entrada_texto.pack(anchor="center")
                
        self.boton = Button(master, text="Investigarla", command=self.obtener_texto)
        self.boton.pack()

        self.boton_volver = Button(master, text="Volver", command=self.volver_pagina_principal)
        self.boton_volver.pack(padx=5,anchor="sw")

    def volver_pagina_principal(self):
        self.master.destroy()
        root.deiconify()
        
    def obtener_texto(self):
            self.texto = self.entrada_texto.get()
            #lista=nube_palabras(self.texto)
            
            self.master.withdraw()
            pagina3 = Toplevel(self.master)
            lista=[]
            dbName = 'TFG'
            collectionName = 'twitter'
            client = MongoClient(url)
            db = client[dbName]
            collection = db[collectionName]
            resultado = collection.find_one({"twitter_id": self.texto})
            if(resultado):
                lista=[]
                for i in resultado["nube"]:
                    lista.append((i[0],i[1]))
                    
            else:
                lista=nube_palabras(self.texto)
                datos_twitter = {
                    'twitter_id':self.texto,
                    'nube':lista
                    }
        
                collection.insert_one(datos_twitter)
                
            Pagina3(pagina3,lista,self.texto)

class Pagina3:

    def __init__(self, master,palabras,User):      
        self.master = master
        fuente =tkFont.Font(family="Helvetica ", size=13, slant="italic")  
        master.configure(bg='azure')
        master.iconbitmap("img/logo_birds.ico")
        master.title("Nube Palabras")

        self.titulo = Label(master,bg='azure',font=fuente, text="Palabras más usadas por "+User+", pincha en ellas para saber lo que piensa")
        self.titulo.pack(pady=10)
        
        if len(palabras)==0:
            self.ad = Label(master,bg="lavender", text="No se ha encontrado la cuenta") 
            self.ad.pack(pady=5,padx=5)
        
           
        #for i in palabras[0:10]:
            #aqui necesito crear los nombre de la variable boton con la variable i, boton0,boton1...
        self.boton = Button(master,bg="lavender", text=palabras[0][0], command=lambda:self.abrir_pagina4(User,palabras[0][0])) 
        self.boton.pack(side="top", fill="both", expand=True)
        
        self.boton1 = Button(master,bg="lavender", text=palabras[1][0], command=lambda:self.abrir_pagina4(User,palabras[1][0])) 
        self.boton1.pack(side="top", fill="both", expand=True)
               
        self.boton2 = Button(master,bg="lavender", text=palabras[2][0], command=lambda:self.abrir_pagina4(User,palabras[2][0])) 
        self.boton2.pack(side="top", fill="both", expand=True)
        
        self.boton3 = Button(master,bg="lavender", text=palabras[3][0], command=lambda:self.abrir_pagina4(User,palabras[3][0])) 
        self.boton3.pack(side="top", fill="both", expand=True)
        
        self.boton4 = Button(master,bg="lavender", text=palabras[4][0], command=lambda:self.abrir_pagina4(User,palabras[4][0])) 
        self.boton4.pack(side="top", fill="both", expand=True)
        
        self.boton5 = Button(master,bg="lavender", text=palabras[5][0], command=lambda:self.abrir_pagina4(User,palabras[5][0])) 
        self.boton5.pack(side="top", fill="both", expand=True)
        
        self.boton6 = Button(master,bg="lavender", text=palabras[6][0], command=lambda:self.abrir_pagina4(User,palabras[6][0])) 
        self.boton6.pack(side="top", fill="both", expand=True)
        
        self.boton7 = Button(master,bg="lavender", text=palabras[7][0], command=lambda:self.abrir_pagina4(User,palabras[7][0])) 
        self.boton7.pack(side="top", fill="both", expand=True)
        
        self.boton8 = Button(master,bg="lavender", text=palabras[8][0], command=lambda:self.abrir_pagina4(User,palabras[8][0])) 
        self.boton8.pack(side="top", fill="both", expand=True)
        
        self.boton9 = Button(master,bg="lavender", text=palabras[9][0], command=lambda:self.abrir_pagina4(User,palabras[9][0])) 
        self.boton9.pack(side="top", fill="both", expand=True)
        
        self.boton10 = Button(master,bg="lavender", text=palabras[10][0], command=lambda:self.abrir_pagina4(User,palabras[10][0])) 
        self.boton10.pack(side="top", fill="both", expand=True)
        
        
          
        self.boton_volver = Button(master, text="Volver", command=self.abrir_pagina2)
        self.boton_volver.pack(padx=5,anchor='sw')
        
    def opinion(self,User,palabra):
        opinion=opinion_tema(User, palabra)
        self.titulo = Label(self, text=opinion[1]+" con una nota de "+ str(opinion[2]))
        self.titulo.grid(pady=10,row=0)
        
    def abrir_pagina2(self):
        self.master.withdraw()
        pagina2 = Toplevel(self.master)
        Pagina2(pagina2)
        
    def abrir_pagina4(self,User,palabra):
        pagina4 = Toplevel(self.master)
        Pagina4(pagina4,User,palabra)
              
class Pagina4:
    global tema
    def __init__(self, master,User,palabra):      
        self.master = master
        master.iconbitmap("img/logo_birds.ico")
        master.title("Que opina de esto")
        self.titulo = Label(master, text="Cuando habla de "+palabra)
        self.titulo.grid(pady=10,row=0)
        
        opinion=opinion_tema(User, palabra)
        
        self.titulo = Label(master, text=opinion[1])
        self.titulo.grid(pady=10,row=0)



root = Tk()
root.iconbitmap("img/logo_birds.ico")
root.config(width="800", height="600")
mi_app = PaginaPrincipal(root)
root.mainloop()