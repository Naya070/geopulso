from re import X
import tkinter as tk
from tkinter import BOTH, BOTTOM, DISABLED, END, LEFT, RIGHT, TOP, Y, X, StringVar, ttk
from tkinter import messagebox
from turtle import bgcolor, heading, left, right, width
from tkinter import ttk
from webbrowser import get
from PIL import ImageTk, Image
from datetime import datetime

import tkinter.font as font

#from clientes import Clase_clientes
from data_base import bd
import mysql.connector



class Login1(tk.Frame):  
    control_bd = bd() 

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  
        
        def salir():
            self.master.destroy()
            self.master.quit()


        def widgets():
            global entry_usuario_var
            global entry_contrase_var

            self.fondo = ImageTk.PhotoImage(Image.open("img/fondo.jpg"))
            self.login = tk.PhotoImage(file="img/login.png")
            self.label_fondo = tk.Label(self, image= self.fondo).pack(expand=True)

            self.fondo1 = ImageTk.PhotoImage(Image.open("img/label.png"))
            self.label_fondo1 = tk.Label(self, image= self.fondo1).pack(expand=True)
                
            self.fuente1 = font.Font(family= 'FreeSerif', size=20, weight='bold')

            label_cuadro = tk.Label(self, bg="#ecf0f6").place(x=20, y=60, width=360, height=500)
            label_login = tk.Label(self, image= self.login, bg="#ecf0f6").place(x=140, y=60)
            self.ingrese_aqui = tk.Label(self, text="Ingrese Aquí", font= self.fuente1, bg="#ecf0f6", fg="#303452").place(x=110, y=170)
                
                #Componentes de la ventana de inicio de sesion
            entry_usuario_var = StringVar()
            entry_contrase_var = StringVar()

            self.label_usuario = tk.Label(self, text="Usuario o correo", font=("Cambria", 15, "bold"), bg="#ecf0f6", fg="#303452").place(x=50, y=230)
            self.label_contrase = tk.Label(self, text="Contraseña", font=("Cambria", 15, "bold"), bg="#ecf0f6", fg="#303452").place(x=50, y=330)
                
            self.entry_usuario = tk.Entry(self, textvariable = entry_usuario_var, font=("Cambria", 15, "bold")).place(x=50, y=270, width=290, height=30)
            self.entry_contrase = tk.Entry(self, textvariable = entry_contrase_var, show='*', font=("Cambria", 15, "bold")).place(x=50, y=370, width=290, height=30)

            self.button_acceder = tk.Button(self, text="Acceder", command = comprobar_datos, font=(
                    "Cambria", 15, "bold"), bg="#303452", fg="white", width=15, height=2).place(x=100, y=430)
            self.button_registrar = tk.Button(self, text="Registrarse", command= registro, font=(
                    "Cambria", 15, "bold"), bg="white", fg="#303452", width=15, height=2).place(x=650, y=430)
            


			#CREAMOS VENTANA PARA REGISTRO.
        def registro():
            
            ventana_registro = tk.Toplevel()
            ventana_registro.configure(bg="#ecf0f6")
            ventana_registro.title("Registro")
            ventana_registro.geometry("320x400")
		
            global nombre_usuario
            global clave
            global clave_repetir
            global nombres
            global apellidos
            global correo
            global clave_acceso

            global entrada_nombre
            global entrada_clave

            #Componentes de la ventana de registro de usuario

            nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario" y los otros datos.
            clave = StringVar() 
            clave_repetir = StringVar() 
            nombres = StringVar() 
            apellidos = StringVar() 
            correo = StringVar() 
            clave_acceso  = StringVar()


            tk.Label(ventana_registro, text="Introduzca datos", bg="#ecf0f6", font=("Cambria", 12, "bold")).pack()
            tk.Label(ventana_registro, text="", bg="#ecf0f6").pack()
            etiqueta_nombre = tk.Label(ventana_registro, text="Nombre de usuario", bg="#ecf0f6", font=("Cambria", 12, "bold"))
            etiqueta_nombre.pack()
            entrada_nombre = tk.Entry(ventana_registro, textvariable=nombre_usuario, font=("Cambria", 12, "bold")) #ESPACIO PARA INTRODUCIR EL NOMBRE.
            entrada_nombre.pack()

            etiqueta_clave = tk.Label(ventana_registro, text="Contraseña", bg="#ecf0f6", font=("Cambria", 12, "bold"))
            etiqueta_clave.pack()
            entrada_clave = tk.Entry(ventana_registro, textvariable=clave, show='*',font=("Cambria", 12, "bold")) #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
            entrada_clave.pack()

            etiqueta_clave_repetir = tk.Label(ventana_registro, text="Confirmar Contraseña", bg="#ecf0f6", font=("Cambria", 12, "bold"))
            etiqueta_clave_repetir.pack()
            entrada_clave_repetir = tk.Entry(ventana_registro, textvariable=clave_repetir, show='*',font=("Cambria", 12, "bold")) #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
            entrada_clave_repetir.pack()

            etiqueta_nombs = tk.Label(ventana_registro, text="Nombres", bg="#ecf0f6", font=("Cambria", 12, "bold"))
            etiqueta_nombs.pack()
            entrada_nombs = tk.Entry(ventana_registro, textvariable=nombres, font=("Cambria", 12, "bold")) #ESPACIO PARA INTRODUCIR EL NOMBRE.
            entrada_nombs.pack()

            etiqueta_apellidos = tk.Label(ventana_registro, text="Apellidos", bg="#ecf0f6", font=("Cambria", 12, "bold"))
            etiqueta_apellidos.pack()
            entrada_apellidos = tk.Entry(ventana_registro, textvariable=apellidos, font=("Cambria", 12, "bold")) 
            entrada_apellidos.pack()

            etiqueta_correo = tk.Label(ventana_registro, text="Correo", bg="#ecf0f6", font=("Cambria", 12, "bold"))
            etiqueta_correo.pack()
            entrada_correo = tk.Entry(ventana_registro, textvariable=correo, font=("Cambria", 12, "bold")) 
            entrada_correo.pack()

            etiqueta_clave_acceso = tk.Label(ventana_registro, text="Inserte clave de acceso*", bg="#ecf0f6", font=("Cambria", 12, "bold"))
            etiqueta_clave_acceso.pack()
            entrada_clave_acceso = tk.Entry(ventana_registro, textvariable=clave_acceso, show='*',font=("Cambria", 12, "bold")) #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
            entrada_clave_acceso.pack()

            tk.Label(ventana_registro, bg="#ecf0f6", text="").pack()
            tk.Button(ventana_registro, text="Registrarse", width=10, height=1, bg="#ecf0f6", command = registro_usuario).pack() #BOTÓN "Registrarse"

            etiqueta_clave_acceso = tk.Label(ventana_registro, text="", bg="#ecf0f6", font=("Cambria", 12, "bold"))
            etiqueta_clave_acceso.pack()
            etiqueta_clave_acceso = tk.Label(ventana_registro, text="*Solicite clave al administrador", bg="#ecf0f6", font=("Cambria", 9, "bold"))
            etiqueta_clave_acceso.pack()


			
		
        def comprobar_datos():
            print("entry_usuario_var:", entry_usuario_var.get())
            global usuario

            control_bd = bd() 
            control_bd.colocar_usuario_escrito(entry_usuario_var.get())

            a = control_bd.buscar_usuario(entry_usuario_var.get())
            #Busca si el usuario escrito existe en base de datos y de existir devuelve su id
            #Si el usuario no existe devuelve 0
            print("a:", a)
            usuario_contrasenna = control_bd.comprobar_usuario(a)
            #Busca usuario y password segun el id del usuario existente

            for row in usuario_contrasenna:
                usuario = row[0]
                contrasenna = row[1]

            if len(entry_usuario_var.get()) < 1:
                messagebox.showinfo("ADVERTENCIA","Coloque el nombre de usuario")

            elif len(entry_contrase_var.get()) < 1:
                messagebox.showinfo("ADVERTENCIA","Coloque la contraseña")

            elif a ==0:
                messagebox.showinfo("ADVERTENCIA","El usuario no existe")

            elif entry_contrase_var.get() != contrasenna:
                messagebox.showinfo("ADVERTENCIA","Contraseña inválida")

            else:
                control_bd.colocar_usuario_escrito(entry_usuario_var.get())
                #Subir a la base de datos el nombre ingresado del usuario escrito al hacer login
                controller.show_frame(Clase_menu) # Entrar a la ventana principal
                controller.protocol("WM_DELETE_WINDOW", salir)
                usuario_loggeado()
		

        def usuario_loggeado():
            return usuario


		#REGISTRO DE USUARIO
        def registro_usuario():
            control_bd = bd() 
            rows = control_bd.obtener_log()
            for row in rows:
                print(row[0])


            try:

                if len(nombre_usuario.get()) < 1:
                    messagebox.showinfo("ADVERTENCIA","Coloque el nuevo nombre de usuario")

                elif len(clave.get()) < 1:
                    messagebox.showinfo("ADVERTENCIA","Coloque la contraseña")

                elif len(clave_repetir.get()) < 1:
                    messagebox.showinfo("ADVERTENCIA","Confirme la contraseña")

                elif len(nombres.get()) < 1:
                    messagebox.showinfo("ADVERTENCIA","Coloque sus nombres")

                elif len(apellidos.get()) < 1:
                    messagebox.showinfo("ADVERTENCIA","Coloque sus apellidos")

                elif len(correo.get()) < 1:
                    messagebox.showinfo("ADVERTENCIA","Coloque su correo")

                elif len(clave_acceso.get()) < 1:
                    messagebox.showinfo("ADVERTENCIA","Coloque la clave de acceso, pidala al gerente de la empresa")
                    
                elif clave.get() != clave_repetir.get():
                    messagebox.showinfo("ADVERTENCIA","Error en la confirmación de contraseña")

                elif row[0] != clave_acceso.get():
                    messagebox.showinfo("ADVERTENCIA","Clave de acceso incorrecta")

                else:
                    response = messagebox.askokcancel("AVISO","Se creará un nuevo usuario")
                    if response == True:
                        control_bd.crear_nuevo_usuario(nombres.get(), apellidos.get(), nombre_usuario.get(), correo.get(), clave.get())
                        messagebox.showinfo("HECHO","Nuevo usuario creado")
                    if response == False:
                        pass
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al registrar usuario.")
                pass


        widgets()
		


class Clase_menu(tk.Frame): 
    
    def __init__(self, parent, controller):
		
        tk.Frame.__init__(self, parent)  
        print("MENU")
		
        print("Clase_menu interfaz_menu")

        control_bd = bd()

        usuario = control_bd.seleccion_usuario()
        print("usuario:", usuario)

        id_del_usuario = control_bd.buscar_usuario(usuario)
        print("id_del_usuario:", id_del_usuario)
            #busca el id del usuario segun el usuario
        control_bd.colocar_id_usuariologin(id_del_usuario)
            #Sube el id del usuario que hizo login a la base de datos
        seleccion_id =control_bd.seleccion_id()
        print("seleccion_id:", seleccion_id)
            #Selecciona id de la base da datos (para asegurar que se subio)
        datos_usuario = control_bd.tomar_datos_usuario(seleccion_id)
        print("datos_usuario:", datos_usuario )
            #ya tengo los datos del usuario que hizo Login
        g = ("1","2","3"),("1","2","3"),("1","2","3")

        for datos in g:
                print("Datos:", datos)
                nombres = datos[0]
                apellidos = datos[1]
                usuario = datos[2]




        s = ttk.Style()
        s.configure('TFrame', background='#ecf0f6')
            
        self.frame_fondo = ttk.Frame(self, style= 'TFrame')
        self.frame_fondo.pack(expand=True, fill=BOTH)
        self.frame_fondo.config(width=1024, height=768)

        self.fondo = ImageTk.PhotoImage(Image.open("img/fondo4.jpg"))
        self.label_fondo = tk.Label(self.frame_fondo, image= self.fondo, bg='#ecf0f6').pack(side=LEFT, expand=False, fill=Y)

        self.logo = ImageTk.PhotoImage(Image.open("img/geopulso2.jpg"))
        self.label_logo = tk.Label(self.frame_fondo, image= self.logo, bg='#303452').pack(side=BOTTOM)
            
        datos_usuario_texto= ("\n\n Bienvenido al sistema de gestion de su empresa")
            
        self.label_fondo = tk.Label(self.frame_fondo, text=datos_usuario_texto, font=("Cambria", 12, "bold"), bg='#ecf0f6', fg='#303452').pack(side=TOP, expand=False, fill=X)
        self.bajo_botones = tk.Label(self.frame_fondo, text="\n\n\n\n\n", bg='#ecf0f6').pack()

        self.button_proyectos = tk.Button(self.frame_fondo, text="Proyectos", width=20, height=2, bg='#303452', fg='white', font=("Cambria", 12, "bold")).pack()
        self.label_espacio = tk.Label(self.frame_fondo, text="\n", bg='#ecf0f6').pack()

        self.button_clientes = tk.Button(self.frame_fondo, command = lambda:controller.show_frame(Clase_clientes),  text="Clientes", width=20, height=2, bg='#303452', fg='white', font=("Cambria", 12, "bold")).pack()
        self.label_espacio = tk.Label(self.frame_fondo, text="\n", bg='#ecf0f6').pack()
            
        self.button_proveedores = tk.Button(self.frame_fondo, command = lambda:controller.show_frame(Clase_proveedores), text="Proveedores", width=20, height=2, bg='#303452', fg='white', font=("Cambria", 12, "bold")).pack( )
        self.label_espacio = tk.Label(self.frame_fondo, text="\n", bg='#ecf0f6').pack()
            
        self.button_material= tk.Button(self.frame_fondo,command = lambda:controller.show_frame(Clase_material), text="Material", width=20, height=2, bg='#303452', fg='white', font=("Cambria", 12, "bold")).pack()
        self.label_espacio = tk.Label(self.frame_fondo, text="\n", bg='#ecf0f6').pack()

        self.button_equipo = tk.Button(self.frame_fondo,command = lambda:controller.show_frame(Clase_equipo), text="Equipo", width=20, height=2, bg='#303452', fg='white', font=("Cambria", 12, "bold")).pack()
        self.label_espacio = tk.Label(self.frame_fondo, text="\n", bg='#ecf0f6').pack()

        self.button_empleados = tk.Button(self.frame_fondo, command = lambda:controller.show_frame(Clase_empleados), text="Empleados", width=20, height=2, bg='#303452', fg='white', font=("Cambria", 12, "bold")).pack()
        self.label_espacio = tk.Label(self.frame_fondo, text="\n", bg='#ecf0f6').pack()

        self.button_cerrar = tk.Button(self.frame_fondo, text="Cerrar sesión", command = lambda:controller.show_frame(Login1) ,width=20, height=2, bg='#303452', fg='white', font=("Cambria", 12, "bold")).pack()
        self.label_espacio = tk.Label(self.frame_fondo, text="\n\n\n                             ", bg='#ecf0f6').pack(expand=True, fill=BOTH, side=RIGHT)

        self.fuente1 = font.Font(family= 'FreeSerif', size=20, weight='bold')





class Clase_clientes(tk.Frame): 
    
    def __init__(self, parent, controller):
		
        tk.Frame.__init__(self, parent) 
        control_bd = bd()
        
        print("CLASE_CLIENTES") 


        def mientras():
            pass
        
        def salir():
            self.master.destroy()
            self.master.quit()
        

        self.config(bg="#ecf0f6", width=2440, height=300)

        self.frame_fondo = tk.Frame(self)
        self.frame_fondo.pack(expand=True)
        self.frame_fondo.config(bg="#ecf0f6", width=1440, height=500)
            

        self.fondo = ImageTk.PhotoImage(Image.open("img/fondo_azul.jpg"))
        
        self.frame_1 = tk.Frame(self.frame_fondo)
        self.frame_1.pack(fill=tk.BOTH, side=tk.TOP)
        self.frame_1.config(bg="#ecf0f6", width=1440, height=400)

        self.label_a= tk.Label(self.frame_1, image= self.fondo, relief=tk.SUNKEN)
        self.label_a.place(x=10, y=90, width=350, height= 300)

        self.label_b= tk.Label(self.frame_1,bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_b.place(x=365,y=90, width=290, height= 300)

        self.label_c= tk.Label(self.frame_1, image= self.fondo, relief=tk.SUNKEN)
        self.label_c.place(x=660,y=90, width=355, height= 300)

                #Buttons
        self.button_proyectos = tk.Button(self, text="Proyectos", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20, height=1 ).place(x = 0, y = 0)      
        self.button_proveedores = tk.Button(self, text="Proveedores", command = lambda:controller.show_frame(Clase_proveedores), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 170, y = 0)     
        self.button_material = tk.Button(self, text="Material", command = lambda:controller.show_frame(Clase_material), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 340, y = 0) 
        self.button_equipo = tk.Button(self, text="Equipo", command = lambda:controller.show_frame(Clase_equipo), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20,height=1).place(x=510, y=0)
        self.button_empleados = tk.Button(self, text="Empleados", command = lambda:controller.show_frame(Clase_empleados),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=680, y=0)
        self.button_menu = tk.Button(self, text="Menu", command = lambda:controller.show_frame(Clase_menu),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=850, y=0)

        self.anadir = tk.Button(self, text="Añadir cliente", command = self.anadir_cliente, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 680, y = 250) 
        self.actualizar_b = tk.Button(self, text="Actualizar", command = self.actualizar,bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 865, y = 250)
        self.eliminar = tk.Button(self, text="Eliminar cliente", command = self.borrar, bg='#72729a', fg='white', font=("Arial",10,"bold"),width=15, height=2).place(x = 680, y = 325) 
        self.limpiar = tk.Button(self, text="Limpiar campos", command = self.limpiarCampos, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 865, y = 325)  

        self.buscar = tk.Button(self, text="Buscar", command = self.busqueda, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=920, y=140)  


                #Labels
        self.modificar_datos= tk.Label(self, text="Modificar Datos", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=15, y=80)   
            
        self.nombres = tk.Label(self, text="Nombres:", font=("Arial"), bg="#f6fbff", fg="#303452" ).place(x=13, y=120)  
        self.apellidos = tk.Label(self, text="Apellidos:", font=("Arial"), bg="#f6fbff", fg="#303452" ).place(x=13, y=170)
        self.cedula = tk.Label(self, text="Cédula:", font=("Arial"), bg="#f6fbff", fg="#303452" ).place(x=13, y=220)
        self.telefono = tk.Label(self, text="Teléfono:", font=("Arial"), bg="#f5fafe", fg="#303452" ).place(x=13, y=270)
        self.correo= tk.Label(self, text="Correo:", font=("Arial"), bg="#f3fbfe", fg="#303452" ).place(x=13, y=320) 

        self.direccion_vivienda = tk.Label(self, text="Direccion de la vivienda:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=120)
        self.empresa = tk.Label(self, text="Empresa en donde labora:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=170)
        self.direccion_empresa = tk.Label(self, text="Direccion de la empresa:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=220)
            
        self.comentarios= tk.Label(self, text="Comentarios:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=270)
            
                #Entry
            
            
            
        self.nombres_var = StringVar()
        self.apellidos_var = StringVar()
        self.cedula_var = StringVar()
        self.telefono_var = StringVar()
        self.correo_var = StringVar()
        self.direccion_vivienda_var = StringVar()
        self.empresa_var = StringVar()
        self.direccion_empresa_var = StringVar()
            #self.comentarios_var = StringVar()
            

        self.buscar_entry_var = StringVar()
            



            
        self.nombres_entry = tk.Entry(self, textvariable= self.nombres_var).place(x=15, y=145, width=250)
        self.apellidos_entry= tk.Entry(self, textvariable= self.apellidos_var).place(x=15, y=195, width=250)
        self.cedula_entry = tk.Entry(self, textvariable= self.cedula_var).place(x=15, y=245, width=250)
        self.telefono_entry = tk.Entry(self, textvariable= self.telefono_var).place(x=15, y=295, width=250)
        self.correo_entry = tk.Entry(self, textvariable= self.correo_var).place(x=15, y=345, width=250)

        self.direccion_vivienda_entry= tk.Entry(self, textvariable= self.direccion_vivienda_var).place(x=370, y=145, width=250)
        self.empresa_entry = tk.Entry(self, textvariable= self.empresa_var).place(x=370, y=195, width=250)
        self.direccion_empresa_entry = tk.Entry(self, textvariable= self.direccion_empresa_var).place(x=370, y=245, width=250)

        #Comentarios
        self.textBox=tk.Text(self, height=6, width=35) 
        self.textBox.place(x=370, y=295)
        self.textBox.get('1.0','end')
            
            
            
        self.buscar = tk.Label(self, text="Buscar", font=("Arial"),
                                bg="#f9fdff", fg="#303452", width=6, height=1).place(x=665, y=120)

        self.buscar_entry = tk.Entry(self, textvariable= self.buscar_entry_var).place(x=665, y=145, width=250)

            # Frame del treeview
        self.frame_treeview = tk.Frame(self.frame_fondo)
        self.frame_treeview.pack(fill=tk.BOTH, side=tk.BOTTOM)
        self.frame_treeview.config(bg="white", width=1440, height=300)

        style = ttk.Style()
        style.configure("mystyle.Treeview",
            background = "red",
            foreground = "#303452",
            rowheight = 30,
            fieldbackground = "white"
        )

                    # Set the treeview
        self.tree = ttk.Treeview(self.frame_treeview, style="mystyle.Treeview", height=17)

        self.treexscroll = tk.Scrollbar(self.frame_treeview, orient=tk.HORIZONTAL)
        self.treexscroll.pack(fill=tk.X, side=tk.BOTTOM)
            # configurar scrollbar
        self.treexscroll.config(command=self.tree.xview)

        self.treeyscroll = tk.Scrollbar(self.frame_treeview, orient=tk.VERTICAL)
        self.treeyscroll.pack(fill=tk.Y, side=tk.RIGHT)
            # configurar scrollbar
        self.treeyscroll.config(command=self.tree.yview)

            # TREEVIEW
        self.tree.config(xscrollcommand=self.treexscroll.set, yscrollcommand=self.treeyscroll.set, 
        columns=(
                    "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))

        
        self.tree.column("#0", width=150, stretch= False)
        self.tree.column("col1", width=150, stretch= False)
        self.tree.column("col2", width=150, stretch= False)
        self.tree.column("col3", width=150, stretch= False)
        self.tree.column("col4", width=160, stretch= False)
        self.tree.column("col5", width=150, stretch= False)
        self.tree.column("col6", width=150, stretch= False)
        self.tree.column("col7", width=150, stretch= False)
        self.tree.column("col8", width=150, stretch= False)
        self.tree.column("col9", width=150, stretch= False)
            
        

            
        self.tree.heading("#0", text="Id", anchor=tk.CENTER)
        self.tree.heading("col1", text="Nombres", anchor=tk.CENTER)
        self.tree.heading("col2", text="Apellidos", anchor=tk.CENTER)
        self.tree.heading("col3", text="Cédula", anchor=tk.CENTER)
        self.tree.heading("col4", text="Teléfono", anchor=tk.CENTER)
        self.tree.heading("col5", text="Correo", anchor=tk.CENTER)
        self.tree.heading("col6", text="Direccion de la vivienda", anchor=tk.CENTER)
        self.tree.heading("col7", text= "Empresa", anchor=tk.CENTER)
        self.tree.heading("col8", text="Direccion de la empresa", anchor=tk.CENTER)
        self.tree.heading("col9", text="Comentarios", anchor=tk.CENTER)
            
            

        self.tree.pack()
        self.treeview = self.tree
            
        self.id = 0
        self.iid = 0

        self.mostrar()
            
            
        self.tree.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick)
        self.tree.bind('<<TreeviewSelect>>', self.bindings)
        #self.frame_fondo.bind('<Return>', self.busqueda)
        #self.bindings()




    def mostrar(self): #Actualizar treeview luego de modificar
            
            control_bd = bd()
            datos_apt = control_bd.mostrar_clientes()
            
            registros = self.tree.get_children()
            for elemento in registros:
                self.tree.delete(elemento)
            try:
                self.indice= 1
                for row in datos_apt:			
                    self.tree.tag_configure("#ecf0f6", background="#ecf0f6")
                    self.tree.tag_configure("white", background="white")
                    color = "white" if self.indice % 2 else "#ecf0f6"
                    id_cliente = row[0]
                    
                    self.tree.insert("",END, tag=('fuente', color), iid=id_cliente, text = row[0], values =(row[1], 
                    row[2],row[3], row[4], row[5],row[6], row[7],row[8], row[9]))
                    self.indice= self.indice+1
                            
            except:
                pass


    def limpiarCampos(self):
        

            self.nombres_var.set("")
            self.apellidos_var.set("")
            self.cedula_var.set("")
            self.telefono_var.set("")
            self.correo_var.set("")
            self.direccion_vivienda_var.set("")
            self.empresa_var.set("")
            self.direccion_empresa_var.set("")
            self.textBox.delete('1.0','end')
            
        
	
    def seleccionarUsandoClick(self, event):
            item = self.tree.identify('item', event.x, event.y)

            self.nombres_var.set(self.tree.item(item, "values")[0])
            self.apellidos_var.set(self.tree.item(item, "values")[1])
            self.cedula_var.set(self.tree.item(item, "values")[2])
            self.telefono_var.set(self.tree.item(item, "values")[3])
            self.correo_var.set(self.tree.item(item, "values")[4])
            self.direccion_vivienda_var.set(self.tree.item(item, "values")[5])
            self.empresa_var.set(self.tree.item(item, "values")[6])
            self.direccion_empresa_var.set(self.tree.item(item, "values")[7])
            self.textBox.delete('1.0','end')
            self.textBox.insert('end', self.tree.item(item, "values")[8])

            print("you clicked on", self.tree.item(item,"text"))
            self.id_c = self.tree.item(item,"text")
            print(self.id_c)
            #self.tree.selection_set('0')
			
    def busqueda(self):
            control_bd = bd()
            

            try:
                self.criterio1 = ''
                self.criterio = self.buscar_entry_var.get()
                print(self.criterio)
                self.criterio1 = "%s" % self.criterio +"%"
                self.datos = control_bd.busqueda_clientes(self.criterio1)
                print("Criterio1: ", self.criterio1)

                if self.criterio1 == '%':
                    messagebox.showwarning("ADVERTENCIA","Coloque criterio de busqueda")
                    
                elif self.criterio1 != '':
                    numeros = []
                    for row in self.datos:
                        numeros.append(row[0])
                        self.row_id = row[0]
                    self.tree.selection
                    self.tree.selection_set(self.tree.tag_has(self.row_id))
                    self.tree.selection_set(numeros) # move selection
                    self.tree.focus(self.row_id) # move focus
                    self.tree.see(self.row_id)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error de búsqueda")
                pass


    def bindings(self, event):
            self.tree.bind("<Button-1>", self.seleccionarUsandoClick)
            


    def anadir_cliente(self):
        control_bd = bd()

        try:
            if self.nombres_var.get() == '' or self.apellidos_var.get()=='':
                messagebox.showwarning("ADVERTENCIA","Debe introducir nombre y apellido del cliente")
            else:
                datos = self.nombres_var.get(), self.apellidos_var.get(), self.cedula_var.get(), self.telefono_var.get(), self.correo_var.get(), self.direccion_vivienda_var.get(), self.empresa_var.get(), self.direccion_empresa_var.get(), self.textBox.get(1.0, tk.END+"-1c")
                control_bd.anadir_cli_bd(datos)
                messagebox.showinfo("REALIZADO","Cliente anadido")
        
        except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al anadir cliente")
                pass

        self.limpiarCampos()
        self.mostrar()



    def actualizar(self):
            control_bd = bd()
            try:
                datos_actualizar = self.nombres_var.get(), self.apellidos_var.get(), self.cedula_var.get(),self.telefono_var.get(), self.correo_var.get(), self.direccion_vivienda_var.get(), self.empresa_var.get(), self.direccion_empresa_var.get(), self.textBox.get(1.0, tk.END+"-1c"), self.id_c 
                control_bd.actualizar_cliente(datos_actualizar)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
                pass
            self.limpiarCampos()
            self.mostrar()

        
    def borrar(self):
        control_bd = bd()
        try:
            if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                control_bd.borrar_cliente(self.id_c)
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
            pass

        self.limpiarCampos()
        self.mostrar()




class Clase_empleados(tk.Frame): 
    
    def __init__(self, parent, controller):
		
        tk.Frame.__init__(self, parent) 
        control_bd = bd()
        
        print("CLASE_EMPLEADOS") 


        def mientras():
            pass
        

        self.config(bg="#ecf0f6", width=2440, height=300)

        self.frame_fondo = tk.Frame(self)
        self.frame_fondo.pack(expand=True)
        self.frame_fondo.config(bg="#ecf0f6", width=1440, height=500)
            

        self.frame_1 = tk.Frame(self.frame_fondo)
        self.frame_1.pack(fill=tk.BOTH, side=tk.TOP)
        self.frame_1.config(bg="#ecf0f6", width=1440, height=400)

        self.label_a= tk.Label(self.frame_1, bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_a.place(x=10, y=90, width=350, height= 300)

        self.fondo1 = ImageTk.PhotoImage(Image.open("img/fondo_empleados.jpg"))

        self.label_b= tk.Label(self.frame_1,image= self.fondo1, relief=tk.SUNKEN)
        self.label_b.place(x=365,y=90, width=290, height= 300)

        self.label_c= tk.Label(self.frame_1,bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_c.place(x=660,y=90, width=355, height= 300)

                #Buttons
        self.button_proyectos = tk.Button(self, text="Proyectos", command = lambda:controller.show_frame(mientras),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20, height=1 ).place(x = 0, y = 0)      
        self.button_proveedores = tk.Button(self, text="Proveedores", command = lambda:controller.show_frame(Clase_proveedores),bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 170, y = 0)     
        self.button_material = tk.Button(self, text="Material", command = lambda:controller.show_frame(Clase_material), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 340, y = 0) 
        self.button_equipo = tk.Button(self, text="Equipo", command = lambda:controller.show_frame(Clase_equipo),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=510, y=0)
        self.button_clientes = tk.Button(self, text="Clientes", command = lambda:controller.show_frame(Clase_clientes), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20,height=1).place(x=680, y=0)
        self.button_menu = tk.Button(self, text="Menu", command = lambda:controller.show_frame(Clase_menu), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20,height=1).place(x=850, y=0)

        self.anadir = tk.Button(self, text="Añadir empleado", command = self.anadir_empleados,bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 680, y = 250) 
        self.actualizar_b = tk.Button(self, text="Actualizar", command = self.actualizar, bg='#72729a', fg='white', font=("Arial",10,"bold"),width=15, height=2).place(x = 865, y = 250)
        self.eliminar = tk.Button(self, text="Eliminar empleado", command = self.borrar,bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 680, y = 325) 
        self.limpiar = tk.Button(self, text="Limpiar campos", command = self.limpiarCampos ,bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 865, y = 325)  

        self.buscar = tk.Button(self, text="Buscar", command = self.busqueda,bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=920, y=140)  


                #Labels
        self.modificar_datos= tk.Label(self, text="Modificar Datos", font=("Arial"), bg="#ecf0f6",fg='#72729a' ).place(x=15, y=80)   
            
        self.nombres = tk.Label(self, text="Nombres:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=120)  
        self.apellidos = tk.Label(self, text="Apellidos:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=170)
        self.cedula = tk.Label(self, text="Cargo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=220)
        self.telefono = tk.Label(self, text="Cédula:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=270)
        self.correo= tk.Label(self, text="Teléfono:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=320) 

        self.direccion_vivienda = tk.Label(self, text="Correo:", font=("Arial"), bg="white", fg="#303452" ).place(x=370, y=120)
        self.empresa = tk.Label(self, text="Direccion de la vivienda:", font=("Arial"), bg="white", fg="#303452" ).place(x=370, y=170)
        
            
        self.comentarios= tk.Label(self, text="Comentarios:", font=("Arial"), bg="white", fg="#303452" ).place(x=370, y=270)
            
                #Entry
            
            
            
        self.nombres_var = StringVar()
        self.apellidos_var = StringVar()
        self.cargo_var = StringVar()
        self.cedula_var = StringVar()
        self.telefono_var = StringVar()
        self.correo_var = StringVar()
        self.direccion_vivienda_var = StringVar()
        self.direccion_empresa_var = StringVar()
            

        self.buscar_entry_var = StringVar()
            



            
        self.nombres_entry = tk.Entry(self, textvariable= self.nombres_var).place(x=15, y=145, width=250)
        self.apellidos_entry= tk.Entry(self, textvariable= self.apellidos_var).place(x=15, y=195, width=250)
        self.cargo_entry = tk.Entry(self, textvariable= self.cargo_var).place(x=15, y=245, width=250)
        self.cedula_entry = tk.Entry(self, textvariable= self.cedula_var).place(x=15, y=295, width=250)
        self.telefono_entry = tk.Entry(self, textvariable= self.telefono_var).place(x=15, y=345, width=250)

        self.correo_entry= tk.Entry(self, textvariable= self.correo_var).place(x=370, y=145, width=250)
        self.direccion_vivienda_entry = tk.Entry(self, textvariable= self.direccion_vivienda_var).place(x=370, y=195, width=250)
        

        #Comentarios
        self.textBox=tk.Text(self, height=6, width=35) 
        self.textBox.place(x=370, y=295)
        self.textBox.get('1.0','end')
            
            
            
        self.buscar = tk.Label(self, text="Buscar", font=("Arial"),
                                bg="#ecf0f6", fg="#303452", width=6, height=1).place(x=665, y=120)

        self.buscar_entry = tk.Entry(self, textvariable= self.buscar_entry_var).place(x=665, y=145, width=250)

            # Frame del treeview
        self.frame_treeview = tk.Frame(self.frame_fondo)
        self.frame_treeview.pack(fill=tk.BOTH, side=tk.BOTTOM)
        self.frame_treeview.config(bg="white", width=1440, height=300)


            # Set the treeview
        self.tree = ttk.Treeview(self.frame_treeview, style="mystyle.Treeview", height=17)

        self.treexscroll = tk.Scrollbar(self.frame_treeview, orient=tk.HORIZONTAL)
        self.treexscroll.pack(fill=tk.X, side=tk.BOTTOM)
            # configurar scrollbar
        self.treexscroll.config(command=self.tree.xview)

        self.treeyscroll = tk.Scrollbar(self.frame_treeview, orient=tk.VERTICAL)
        self.treeyscroll.pack(fill=tk.Y, side=tk.RIGHT)
            # configurar scrollbar
        self.treeyscroll.config(command=self.tree.yview)

            # TREEVIEW
        self.tree.config(xscrollcommand=self.treexscroll.set, yscrollcommand=self.treeyscroll.set,
        columns=(
                    "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))

        
        self.tree.column("#0", width=150, stretch= False)
        self.tree.column("col1", width=150, stretch= False)
        self.tree.column("col2", width=150, stretch= False)
        self.tree.column("col3", width=150, stretch= False)
        self.tree.column("col4", width=160, stretch= False)
        self.tree.column("col5", width=150, stretch= False)
        self.tree.column("col6", width=150, stretch= False)
        self.tree.column("col7", width=150, stretch= False)
        self.tree.column("col8", width=150, stretch= False)
            
        

            
        self.tree.heading("#0", text="Id", anchor=tk.CENTER)
        self.tree.heading("col1", text="Nombres", anchor=tk.CENTER)
        self.tree.heading("col2", text="Apellidos", anchor=tk.CENTER)
        self.tree.heading("col3", text="Cargo", anchor=tk.CENTER)
        self.tree.heading("col4", text="Cédula", anchor=tk.CENTER)
        self.tree.heading("col5", text="Teléfono", anchor=tk.CENTER)
        self.tree.heading("col6", text="Correo", anchor=tk.CENTER)
        self.tree.heading("col7", text= "Direccion de la vivienda", anchor=tk.CENTER)
        self.tree.heading("col8", text="Comentarios", anchor=tk.CENTER)
            
            

        self.tree.pack()
        self.treeview = self.tree
            
        self.id = 0
        self.iid = 0

        self.mostrar()
            
            
        self.tree.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick)
        self.tree.bind('<<TreeviewSelect>>', self.bindings)
        #self.frame_fondo.bind('<Return>', self.busqueda)
        #self.bindings()




    def mostrar(self): #Actualizar treeview luego de modificar
            
            control_bd = bd()
            datos_apt = control_bd.mostrar_empleados()
            
            registros = self.tree.get_children()
            for elemento in registros:
                self.tree.delete(elemento)
            try:
                self.indice= 1
                for row in datos_apt:			
                    self.tree.tag_configure("#ecf0f6", background="#ecf0f6")
                    self.tree.tag_configure("white", background="white")
                    color = "white" if self.indice % 2 else "#ecf0f6"
                    id_cliente = row[0]
                    
                    self.tree.insert("",END, tag=('fuente', color), iid=id_cliente, text = row[0], values =(row[1], 
                    row[2],row[3], row[4], row[5],row[6], row[7],row[8]))
                    self.indice= self.indice+1
                            
            except:
                pass


    def limpiarCampos(self):
        

            self.nombres_var.set("")
            self.apellidos_var.set("")
            self.cargo_var.set("")
            self.cedula_var.set("")
            self.telefono_var.set("")
            self.correo_var.set("")
            self.direccion_vivienda_var.set("")
            self.textBox.delete('1.0','end')
            
        
	
    def seleccionarUsandoClick(self, event):
            item = self.tree.identify('item', event.x, event.y)

            self.nombres_var.set(self.tree.item(item, "values")[0])
            self.apellidos_var.set(self.tree.item(item, "values")[1])
            self.cargo_var.set(self.tree.item(item, "values")[2])
            self.cedula_var.set(self.tree.item(item, "values")[3])
            self.telefono_var.set(self.tree.item(item, "values")[4])
            self.correo_var.set(self.tree.item(item, "values")[5])
            self.direccion_vivienda_var.set(self.tree.item(item, "values")[6])
            self.textBox.delete('1.0','end')
            self.textBox.insert('end', self.tree.item(item, "values")[7])

            print("you clicked on", self.tree.item(item,"text"))
            self.id_c = self.tree.item(item,"text")
            print(self.id_c)
            #self.tree.selection_set('0')
			
    def busqueda(self):
            control_bd = bd()
            

            try:
                self.criterio1 = ''
                self.criterio = self.buscar_entry_var.get()
                print(self.criterio)
                self.criterio1 = "%s" % self.criterio +"%"
                self.datos = control_bd.busqueda_empleados(self.criterio1)
                print("Criterio1: ", self.criterio1)

                if self.criterio1 == '%':
                    messagebox.showwarning("ADVERTENCIA","Coloque criterio de busqueda")
                    
                elif self.criterio1 != '':
                    numeros = []
                    for row in self.datos:
                        numeros.append(row[0])
                        self.row_id = row[0]
                    self.tree.selection
                    self.tree.selection_set(self.tree.tag_has(self.row_id))
                    self.tree.selection_set(numeros) # move selection
                    self.tree.focus(self.row_id) # move focus
                    self.tree.see(self.row_id)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error de búsqueda")
                pass


    def bindings(self, event):
            self.tree.bind("<Button-1>", self.seleccionarUsandoClick)
            


    def anadir_empleados(self):
        control_bd = bd()

        try:
            if self.nombres_var.get() == '' or self.apellidos_var.get()=='':
                messagebox.showwarning("ADVERTENCIA","Debe introducir nombre y apellido del empleado")
            else:
                datos = self.nombres_var.get(), self.apellidos_var.get(), self.cargo_var.get(), self.cedula_var.get(), self.telefono_var.get(), self.correo_var.get(), self.direccion_vivienda_var.get(), self.textBox.get(1.0, tk.END+"-1c")
                control_bd.anadir_empl_bd(datos)
                messagebox.showinfo("REALIZADO","Empleado anadido")
        
        except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al anadir empleado")
                pass

        self.limpiarCampos()
        self.mostrar()



    def actualizar(self):
            control_bd = bd()
            try:
                datos_actualizar = self.nombres_var.get(), self.apellidos_var.get(), self.cargo_var.get(),self.cedula_var.get(), self.telefono_var.get(), self.correo_var.get(), self.direccion_vivienda_var.get(), self.textBox.get(1.0, tk.END+"-1c"), self.id_c 
                control_bd.actualizar_empleados(datos_actualizar)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
                pass
            self.limpiarCampos()
            self.mostrar()

        
    def borrar(self):
        control_bd = bd()
        try:
            if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                control_bd.borrar_empleados(self.id_c)
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
            pass

        self.limpiarCampos()
        self.mostrar()






#CLASE PROVEEDORES

class Clase_proveedores(tk.Frame): 
    
    def __init__(self, parent, controller):
		
        tk.Frame.__init__(self, parent) 
        control_bd = bd()
        
        print("CLASE_PROVEEDORES") 


        def mientras():
            pass
        
        def salir():
            self.master.destroy()
            self.master.quit()
        

        self.config(bg="#ecf0f6", width=2440, height=300)

        self.frame_fondo = tk.Frame(self)
        self.frame_fondo.pack(expand=True)
        self.frame_fondo.config(bg="#ecf0f6", width=1440, height=500)
            

        self.fondo = ImageTk.PhotoImage(Image.open("img/fondo_azul.jpg"))
        
        self.frame_1 = tk.Frame(self.frame_fondo)
        self.frame_1.pack(fill=tk.BOTH, side=tk.TOP)
        self.frame_1.config(bg="#ecf0f6", width=1440, height=400)

        self.label_a= tk.Label(self.frame_1, image= self.fondo, relief=tk.SUNKEN)
        self.label_a.place(x=10, y=90, width=350, height= 300)

        self.label_b= tk.Label(self.frame_1,bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_b.place(x=365,y=90, width=290, height= 300)

        self.label_c= tk.Label(self.frame_1, image= self.fondo, relief=tk.SUNKEN)
        self.label_c.place(x=660,y=90, width=355, height= 300)

                #Buttons
        self.button_proyectos = tk.Button(self, text="Proyectos", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20, height=1 ).place(x = 0, y = 0)      
        self.button_clientes = tk.Button(self, text="Clientes", command = lambda:controller.show_frame(Clase_clientes), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 170, y = 0)     
        self.button_material = tk.Button(self, text="Material", command = lambda:controller.show_frame(Clase_material), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 340, y = 0) 
        self.button_equipo = tk.Button(self, text="Equipo", command = lambda:controller.show_frame(Clase_equipo), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20,height=1).place(x=510, y=0)
        self.button_empleados = tk.Button(self, text="Empleados", command = lambda:controller.show_frame(Clase_empleados),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=680, y=0)
        self.button_menu = tk.Button(self, text="Menu", command = lambda:controller.show_frame(Clase_menu),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=850, y=0)

        self.anadir = tk.Button(self, text="Añadir proveedor", command = self.anadir_proveedor, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 680, y = 250) 
        self.actualizar_b = tk.Button(self, text="Actualizar", command = self.actualizar,bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 865, y = 250)
        self.eliminar = tk.Button(self, text="Eliminar proveedor", command = self.borrar, bg='#72729a', fg='white', font=("Arial",10,"bold"),width=15, height=2).place(x = 680, y = 325) 
        self.limpiar = tk.Button(self, text="Limpiar campos", command = self.limpiarCampos, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 865, y = 325)  

        self.buscar = tk.Button(self, text="Buscar", command = self.busqueda, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=920, y=140)  


                #Labels
        self.modificar_datos= tk.Label(self, text="Modificar Datos", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=15, y=80)   
            
        self.nombres = tk.Label(self, text="Nombre de la empresa:", font=("Arial"), bg="#f6fbff", fg="#303452" ).place(x=13, y=120)  
        self.apellidos = tk.Label(self, text="Producto o servicio ofrecido:", font=("Arial"), bg="#f6fbff", fg="#303452" ).place(x=13, y=170)
        self.cedula = tk.Label(self, text="Nombre del contacto de la empresa:", font=("Arial"), bg="#f6fbff", fg="#303452" ).place(x=13, y=220)
        self.telefono = tk.Label(self, text="Cargo del contacto de la empresa:", font=("Arial"), bg="#f5fafe", fg="#303452" ).place(x=13, y=270)
        self.correo= tk.Label(self, text="Telefono:", font=("Arial"), bg="#f3fbfe", fg="#303452" ).place(x=13, y=320) 

        self.direccion_vivienda = tk.Label(self, text="Correo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=120)
        self.empresa = tk.Label(self, text="RIF:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=170)
        self.direccion_empresa = tk.Label(self, text="Sitio web:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=220)
            
        self.comentarios= tk.Label(self, text="Comentarios:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=270)
            
                #Entry
            
            
            
        self.nombre_empresa_var = StringVar()
        self.producto_servicio_var = StringVar()
        self.nombre_contacto_var = StringVar()
        self.cargo_contacto_var = StringVar()
        self.telefono_var = StringVar()
        self.correo_var = StringVar()
        self.rif_var = StringVar()
        self.sitio_web_var = StringVar()
            

        self.buscar_entry_var = StringVar()
            



            
        self.nombre_empresa_entry = tk.Entry(self, textvariable= self.nombre_empresa_var).place(x=15, y=145, width=250)
        self.producto_servicio_entry= tk.Entry(self, textvariable= self.producto_servicio_var).place(x=15, y=195, width=250)
        self.nombre_contacto_entry = tk.Entry(self, textvariable= self.cargo_contacto_var).place(x=15, y=245, width=250)
        self.cargo_contacto_entry = tk.Entry(self, textvariable= self.telefono_var).place(x=15, y=295, width=250)
        self.telefono_entry = tk.Entry(self, textvariable= self.telefono_var).place(x=15, y=345, width=250)

        self.correo_entry= tk.Entry(self, textvariable= self.correo_var).place(x=370, y=145, width=250)
        self.rif_entry = tk.Entry(self, textvariable= self.rif_var).place(x=370, y=195, width=250)
        self.sitio_web_entry = tk.Entry(self, textvariable= self.sitio_web_var).place(x=370, y=245, width=250)

        #Comentarios
        self.textBox=tk.Text(self, height=6, width=35) 
        self.textBox.place(x=370, y=295)
        self.textBox.get('1.0','end')
            
            
            
        self.buscar = tk.Label(self, text="Buscar", font=("Arial"),
                                bg="#f9fdff", fg="#303452", width=6, height=1).place(x=665, y=120)

        self.buscar_entry = tk.Entry(self, textvariable= self.buscar_entry_var).place(x=665, y=145, width=250)

            # Frame del treeview
        self.frame_treeview = tk.Frame(self.frame_fondo)
        self.frame_treeview.pack(fill=tk.BOTH, side=tk.BOTTOM)
        self.frame_treeview.config(bg="white", width=1440, height=300)

        style = ttk.Style()
        style.configure("mystyle.Treeview",
            background = "red",
            foreground = "#303452",
            rowheight = 30,
            fieldbackground = "white"
        )

                    # Set the treeview
        self.tree = ttk.Treeview(self.frame_treeview, style="mystyle.Treeview", height=17)

        self.treexscroll = tk.Scrollbar(self.frame_treeview, orient=tk.HORIZONTAL)
        self.treexscroll.pack(fill=tk.X, side=tk.BOTTOM)
            # configurar scrollbar
        self.treexscroll.config(command=self.tree.xview)

        self.treeyscroll = tk.Scrollbar(self.frame_treeview, orient=tk.VERTICAL)
        self.treeyscroll.pack(fill=tk.Y, side=tk.RIGHT)
            # configurar scrollbar
        self.treeyscroll.config(command=self.tree.yview)

            # TREEVIEW
        self.tree.config(xscrollcommand=self.treexscroll.set, yscrollcommand=self.treeyscroll.set, 
        columns=(
                    "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))

        
        self.tree.column("#0", width=150, stretch= False)
        self.tree.column("col1", width=150, stretch= False)
        self.tree.column("col2", width=150, stretch= False)
        self.tree.column("col3", width=150, stretch= False)
        self.tree.column("col4", width=160, stretch= False)
        self.tree.column("col5", width=150, stretch= False)
        self.tree.column("col6", width=150, stretch= False)
        self.tree.column("col7", width=150, stretch= False)
        self.tree.column("col8", width=150, stretch= False)
        self.tree.column("col9", width=150, stretch= False)
            
        

            
        self.tree.heading("#0", text="Id", anchor=tk.CENTER)
        self.tree.heading("col1", text="Nombre de la empresa", anchor=tk.CENTER)
        self.tree.heading("col2", text="Producto o servicio", anchor=tk.CENTER)
        self.tree.heading("col3", text="Nombre del contacto de la empresa", anchor=tk.CENTER)
        self.tree.heading("col4", text="Cargo del contacto de la empresa", anchor=tk.CENTER)
        self.tree.heading("col5", text="Telefono", anchor=tk.CENTER)
        self.tree.heading("col6", text="Correo", anchor=tk.CENTER)
        self.tree.heading("col7", text= "RIF", anchor=tk.CENTER)
        self.tree.heading("col8", text="Sitio web", anchor=tk.CENTER)
        self.tree.heading("col9", text="Comentarios", anchor=tk.CENTER)
            
            

        self.tree.pack()
        self.treeview = self.tree
            
        self.id = 0
        self.iid = 0

        self.mostrar()
            
            
        self.tree.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick)
        self.tree.bind('<<TreeviewSelect>>', self.bindings)
        #self.frame_fondo.bind('<Return>', self.busqueda)
        #self.bindings()




    def mostrar(self): #Actualizar treeview luego de modificar
            
            control_bd = bd()
            datos_apt = control_bd.mostrar_proveedores()
            
            registros = self.tree.get_children()
            for elemento in registros:
                self.tree.delete(elemento)
            try:
                self.indice= 1
                for row in datos_apt:			
                    self.tree.tag_configure("#ecf0f6", background="#ecf0f6")
                    self.tree.tag_configure("white", background="white")
                    color = "white" if self.indice % 2 else "#ecf0f6"
                    id_cliente = row[0]
                    
                    self.tree.insert("",END, tag=('fuente', color), iid=id_cliente, text = row[0], values =(row[1], 
                    row[2],row[3], row[4], row[5],row[6], row[7],row[8], row[9]))
                    self.indice= self.indice+1
                            
            except:
                pass


    def limpiarCampos(self):
        
            self.nombre_empresa_var.set("")
            self.producto_servicio_var.set("")
            self.nombre_contacto_var.set("")
            self.cargo_contacto_var.set("")
            self.telefono_var.set("")
            self.correo_var .set("")
            self.rif_var.set("")
            self.sitio_web_var.set("")
            self.textBox.delete('1.0','end')
            


    def seleccionarUsandoClick(self, event):
            item = self.tree.identify('item', event.x, event.y)

            self.nombre_empresa_var.set(self.tree.item(item, "values")[0])
            self.producto_servicio_var.set(self.tree.item(item, "values")[1])
            self.nombre_contacto_var.set(self.tree.item(item, "values")[2])
            self.cargo_contacto_var.set(self.tree.item(item, "values")[3])
            self.telefono_var.set(self.tree.item(item, "values")[4])
            self.correo_var.set(self.tree.item(item, "values")[5])
            self.rif_var.set(self.tree.item(item, "values")[6])
            self.sitio_web_var.set(self.tree.item(item, "values")[7])
            self.textBox.delete('1.0','end')
            self.textBox.insert('end', self.tree.item(item, "values")[8])

            print("you clicked on", self.tree.item(item,"text"))
            self.id_c = self.tree.item(item,"text")
            print(self.id_c)
            #self.tree.selection_set('0')
			
    def busqueda(self):
            control_bd = bd()
            

            try:
                self.criterio1 = ''
                self.criterio = self.buscar_entry_var.get()
                print(self.criterio)
                self.criterio1 = "%s" % self.criterio +"%"
                self.datos = control_bd.busqueda_proveedores(self.criterio1)
                print("Criterio1: ", self.criterio1)

                if self.criterio1 == '%':
                    messagebox.showwarning("ADVERTENCIA","Coloque criterio de busqueda")
                    
                elif self.criterio1 != '':
                    numeros = []
                    for row in self.datos:
                        numeros.append(row[0])
                        self.row_id = row[0]
                    self.tree.selection
                    self.tree.selection_set(self.tree.tag_has(self.row_id))
                    self.tree.selection_set(numeros) # move selection
                    self.tree.focus(self.row_id) # move focus
                    self.tree.see(self.row_id)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error de búsqueda")
                pass


    def bindings(self, event):
            self.tree.bind("<Button-1>", self.seleccionarUsandoClick)
            


    def anadir_proveedor(self):
        control_bd = bd()

        try:
            if self.nombre_empresa_var.get() == '' or self.producto_servicio_var.get()=='':
                messagebox.showwarning("ADVERTENCIA","Debe introducir nombre de la empresa y producto o servicio que ofrece")
            else:
                datos = self.nombre_empresa_var.get(), self.producto_servicio_var.get(), self.nombre_contacto_var.get(), self.cargo_contacto_var.get(), self.telefono_var.get(), self.correo_var.get(), self.rif_var.get(), self.sitio_web_var.get(), self.textBox.get(1.0, tk.END+"-1c")
                control_bd.anadir_pro_bd(datos)
                messagebox.showinfo("REALIZADO","Proveedor anadido")
        
        except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al anadir proveedor")
                pass

        self.limpiarCampos()
        self.mostrar()



    def actualizar(self):
            control_bd = bd()
            try:
                datos_actualizar = self.nombre_empresa_var.get(), self.producto_servicio_var.get(), self.nombre_contacto_var.get(), self.cargo_contacto_var.get(), self.telefono_var.get(), self.correo_var.get(), self.rif_var.get(), self.sitio_web_var.get(), self.textBox.get(1.0, tk.END+"-1c"), self.id_c 
                control_bd.actualizar_proveedores(datos_actualizar)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
                pass
            self.limpiarCampos()
            self.mostrar()

        
    def borrar(self):
        control_bd = bd()
        try:
            if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                control_bd.borrar_proveedores(self.id_c)
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
            pass

        self.limpiarCampos()
        self.mostrar()


#CLASE MATERIAL

class VentanaCategoriaEnMateriales(tk.Toplevel):
        def __init__(self, *args, callback=None, **kwargs):
            super().__init__(*args, **kwargs)
            
            self.wm_attributes("-topmost", True)
            self.geometry("640x600")
            self.title("Tabla categorias")
            self.configure(background="#ecf0f6")

            self.frame_fondo_toplevel = tk.Frame(self)
            self.frame_fondo_toplevel.pack(expand=True)
            self.frame_fondo_toplevel.config(bg="#ecf0f6", width=900, height=200)

            #Label fondo
            self.label_a= tk.Label(self.frame_fondo_toplevel, bg="#ecf0f6", relief=tk.SUNKEN)
            self.label_a.place(x=10, y=10, width=610, height= 225)
        
            #Stringvar
            self.categoria_id_var = StringVar()   
            self.categoria_nombre_var = StringVar()

            self.buscar_entry_cat_var = StringVar()

            #Labels
            self.agregar_categoria= tk.Label(self.frame_fondo_toplevel, text="Agregar categoria", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=15, y=1)

            self.categoria_id = tk.Label(self.frame_fondo_toplevel, text="ID de la Categoria:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=60)  
            self.categoria_nombre = tk.Label(self.frame_fondo_toplevel, text="Nombre de la categoria:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=100)

            #Entry
            self.buscar_entry_ca = tk.Entry(self.frame_fondo_toplevel, textvariable= self.buscar_entry_cat_var).place(x=15, y=30, width=250)
            self.categoria_id_entry = tk.Entry(self.frame_fondo_toplevel, textvariable= self.categoria_id_var).place(x=260, y=60, width=250)
            self.categoria_nombre_entry= tk.Entry(self.frame_fondo_toplevel, textvariable= self.categoria_nombre_var).place(x=260, y=100, width=250)

            #Buttom
            self.buscar_ca = tk.Button(self.frame_fondo_toplevel, text="Buscar", command= self.busqueda_categ, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=280, y=26) 

            self.anadir_ca= tk.Button(self.frame_fondo_toplevel, text="Agregar", command= self.anadir_material_ca, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 15, y = 150) 
            self.actualizar_ca = tk.Button(self.frame_fondo_toplevel, text="Actualizar", command= self.actualizar_categ, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 160, y = 150)
            self.eliminar_ca = tk.Button(self.frame_fondo_toplevel, text="Borrar", command= self.borrar_categ, bg='#72729a', fg='white', font=("Arial",10,"bold"),width=15, height=1).place(x = 310, y = 150) 
            self.limpiar_ca = tk.Button(self.frame_fondo_toplevel, text="Limpiar campos", command= self.limpiarCampos_ca, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 460, y = 150) 

            # Frame del treeview
            self.frame_treeview2 = tk.Frame(self)
            self.frame_treeview2.pack(fill=tk.Y, side=tk.BOTTOM)
            self.frame_treeview2.config(bg="white", width=20, height=30)

            style2 = ttk.Style()
            style2.configure("mystyle.Treeview",
                background = "red",
                foreground = "#303452",
                rowheight = 30,
                fieldbackground = "white"
                )

                    # Set the treeview
            self.tree2 = ttk.Treeview(self.frame_treeview2, style="mystyle.Treeview", height=12)

            self.treexscroll2 = tk.Scrollbar(self.frame_treeview2, orient=tk.HORIZONTAL)
            self.treexscroll2.pack(fill=tk.X, side=tk.BOTTOM)
            # configurar scrollbar
            self.treexscroll2.config(command=self.tree2.xview)

            self.treeyscroll2 = tk.Scrollbar(self.frame_treeview2, orient=tk.VERTICAL)
            self.treeyscroll2.pack(fill=tk.Y, side=tk.RIGHT)
            # configurar scrollbar
            self.treeyscroll2.config(command=self.tree2.yview)

            # TREEVIEW
            self.tree2.config(xscrollcommand=self.treexscroll2.set, yscrollcommand=self.treeyscroll2.set, 
            columns=(
                    "col1"))

        
            self.tree2.column("#0", width=150, stretch= False)
            self.tree2.column("col1", width=150, stretch= False)
            
            self.tree2.heading("#0", text="Id categoria", anchor=tk.CENTER)
            self.tree2.heading("col1", text="Categoria", anchor=tk.CENTER)
            
            
            self.tree2.pack()
            self.treeview2 = self.tree2
            
            self.id = 0
            self.iid = 0

            self.tree2.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick_ca)
            self.tree2.bind('<<TreeviewSelect>>', self.bindings_ca)

            self.mostrar_ca()

            

        def mostrar_ca(self): #Actualizar treeview luego de modificar
            
            control_bd = bd()
            datos_apt2 = control_bd.mostrar_categoria_material()
            
            registros2 = self.tree2.get_children()
            for elemento2 in registros2:
                self.tree2.delete(elemento2)
            try:
                self.indice= 1
                for row2 in datos_apt2:			
                    self.tree2.tag_configure("#ecf0f6", background="#ecf0f6")
                    self.tree2.tag_configure("white", background="white")
                    color = "white" if self.indice % 2 else "#ecf0f6"
                    id_cliente2 = row2[0]
                    
                    self.tree2.insert("",END, tag=('fuente', color), iid=id_cliente2, text = row2[0], values =(row2[1]))
                    self.indice= self.indice+1
                            
            except:
                self.wm_attributes("-topmost", False)
                print("ocurrio un error en mostrar_tabla_categoria")
                self.wm_attributes("-topmost", True)


        def limpiarCampos_ca(self):
        
            self.categoria_id_var.set("")
            self.categoria_nombre_var.set("")
            
        
        def seleccionarUsandoClick_ca(self, event):

            item = self.tree2.identify('item', event.x, event.y)
            self.categoria_id_var.set(self.tree2.item(item, "text"))
            self.categoria_nombre_var.set(self.tree2.item(item, "values")[0])

            print("you clicked on", self.tree2.item(item,"text"))
            self.id_c = self.tree2.item(item,"text")
            print(self.id_c)


        def bindings_ca(self, event):
            self.tree2.bind("<Button-1>", self.seleccionarUsandoClick_ca)

        def anadir_material_ca(self):
            control_bd = bd()

            try:
                if self.categoria_id_var.get() == '' or self.categoria_nombre_var.get()=='':
                    self.wm_attributes("-topmost", False)
                    messagebox.showwarning("ADVERTENCIA","Debe introducir id del producto, nombre y categoria del producto, asi como el id de su proveedor")
                    self.wm_attributes("-topmost", True)
                else:
                    datos = self.categoria_id_var.get(), self.categoria_nombre_var.get()
                    control_bd.anadir_mat_ca_bd(datos)
                    self.wm_attributes("-topmost", False)
                    messagebox.showinfo("REALIZADO","Material anadido")
                    self.wm_attributes("-topmost", True)
        
            except:
                self.wm_attributes("-topmost", False)
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al anadir material")
                self.wm_attributes("-topmost", True)
                pass

            self.limpiarCampos_ca()
            self.mostrar_ca()

        def actualizar_categ(self):
            control_bd = bd()

            try:
                datos_actualizar = self.categoria_id_var.get(), self.categoria_nombre_var.get(), self.id_c
                control_bd.actualizar_material_ca(datos_actualizar)

            except:
                self.wm_attributes("-topmost", False)
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
                self.wm_attributes("-topmost", True)
                pass
            
            self.limpiarCampos_ca()
            self.mostrar_ca()

        
        def borrar_categ(self):
            control_bd = bd()
            try:
                self.wm_attributes("-topmost", False)
                if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                    self.wm_attributes("-topmost", True)
                    control_bd.borrar_material_ca(self.id_c)
                self.wm_attributes("-topmost", True)

            except:
                self.wm_attributes("-topmost", False)
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
                self.wm_attributes("-topmost", True)
                pass

            self.limpiarCampos_ca()
            self.mostrar_ca()


        def busqueda_categ(self):
            control_bd = bd()
            
            try:
                self.criterio1 = ''
                self.criterio = self.buscar_entry_cat_var.get()
                print(self.criterio)
                self.criterio1 = "%s" % self.criterio +"%"
                self.datos = control_bd.busqueda_material_ca(self.criterio1)
                print("Criterio1: ", self.criterio1)

                if self.criterio1 == '%':
                    self.wm_attributes("-topmost", False)
                    messagebox.showwarning("ADVERTENCIA","Coloque criterio de busqueda")
                    self.wm_attributes("-topmost", True)
                    
                elif self.criterio1 != '':
                    numeros = []
                    for row in self.datos:
                        numeros.append(row[0])
                        self.row_id = row[0]
                    self.tree2.selection
                    self.tree2.selection_set(self.tree2.tag_has(self.row_id))
                    self.tree2.selection_set(numeros) # move selection
                    self.tree2.focus(self.row_id) # move focus
                    self.tree2.see(self.row_id)
            except:
                self.wm_attributes("-topmost", False)
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error de búsqueda")
                self.wm_attributes("-topmost", True)
                pass





#Clase material

class Clase_material(tk.Frame): 
    
    def __init__(self, parent, controller):
		
        tk.Frame.__init__(self, parent) 
        control_bd = bd()
        
        print("CLASE_MATERIAL") 


        def mientras():
            pass
        
        

        self.config(bg="#ecf0f6", width=2440, height=300)

        self.frame_fondo = tk.Frame(self)
        self.frame_fondo.pack(expand=True)
        self.frame_fondo.config(bg="#ecf0f6", width=1440, height=20)

        self.label_a= tk.Label(self.frame_fondo, bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_a.place(x=10, y=90, width=610, height= 70)  

        #self.fondo = ImageTk.PhotoImage(Image.open("img/fondo_azul.jpg"))
        
        self.frame_1 = tk.Frame(self.frame_fondo)
        self.frame_1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.frame_1.config(bg="#ecf0f6", width=500, height=90)

        self.frame_2 = tk.Frame(self.frame_fondo)
        self.frame_2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        self.frame_2.config(bg="#ecf0f6", width=400, height=700)

        self.label_b= tk.Label(self.frame_2, bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_b.place(x=10, y=1, width=380, height= 610)


                #Buttons
        self.button_proyectos = tk.Button(self, text="Proyectos", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20, height=1 ).place(x = 0, y = 0)      
        self.button_clientes = tk.Button(self, text="Clientes", command = lambda:controller.show_frame(Clase_clientes), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 170, y = 0)     
        self.button_proveedores = tk.Button(self, text="Proveedores", command = lambda:controller.show_frame(Clase_proveedores), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 340, y = 0) 
        self.button_equipo = tk.Button(self, text="Equipo", command = lambda:controller.show_frame(Clase_equipo), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20,height=1).place(x=510, y=0)
        self.button_empleados = tk.Button(self, text="Empleados", command = lambda:controller.show_frame(Clase_empleados),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=680, y=0)
        self.button_menu = tk.Button(self, text="Menu", command = lambda:controller.show_frame(Clase_menu),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=850, y=0)

        
        self.mostrar_tabla_de_categoria = tk.Button(self, text="Mostrar tabla categorias", command = self.mostrar_tabla_categoria, bg='#72729a', fg='white', font=("Arial",10,"bold"),width=25, height=1).place(x = 190, y = 105) 
        

        self.anadir_pro = tk.Button(self, text="Añadir material",command = self.anadir_material, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 680, y = 610) 
        self.actualizar_pro = tk.Button(self, text="Actualizar", command = self.actualizar, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 865, y = 610)
        self.eliminar_pro = tk.Button(self, text="Eliminar material", command = self.borrar, bg='#72729a', fg='white', font=("Arial",10,"bold"),width=15, height=1).place(x = 680, y = 650) 
        self.limpiar_pro = tk.Button(self, text="Limpiar campos", command = self.limpiarCampos, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 865, y = 650)  
        

        self.buscar_pro = tk.Button(self, text="Buscar", command = self.busqueda, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=910, y=115) 

        
        self.poner_fecha = tk.Button(self, text="Fecha", command = self.fecha_poner, bg='#72729a', fg='white', font=("Arial",8,"bold"), width=5).place(x=945, y=508) 

        

        #Labels
        self.agregar_categoria= tk.Label(self, text="Agregar categoria", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=15, y=80)   
        self.gestion_producto= tk.Label(self, text="Gestion de producto", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=650, y=80) 
            
        
        
        
        
        self.id_producto_label = tk.Label(self, text="ID producto:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=150)
        self.categoria_label = tk.Label(self, text="Categoria:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=190)
        self.producto_label = tk.Label(self, text="Producto:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=230)
        self.descripcion_label = tk.Label(self, text="Descripcion:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=270)
        self.marca_label = tk.Label(self, text="Marca:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=310)
        self.modelo_label = tk.Label(self, text="Modelo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=350)
        self.id_proveedor_label = tk.Label(self, text="ID proveedor:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=390)
        self.cantidad_label = tk.Label(self, text="Cantidad:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=430)
        self.precio_label = tk.Label(self, text="Precio:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=470)
        self.ultima_entrada_label = tk.Label(self, text="Ultima entrada:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=510)
        self.comentarios_label = tk.Label(self, text="Comentarios:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=550)
        
            
        #Entry
            
            
        self.categoria_id_var = StringVar()   
        self.categoria_nombre_var = StringVar() 
        
        self.id_producto_var = StringVar()
        self.categoria_var = StringVar()
        self.producto_var = StringVar()
        self.descripcion_var = StringVar()
        self.marca_var = StringVar()
        self.modelo_var = StringVar()
        
        self.id_proveedor_var = StringVar()

        self.cantidad_var = StringVar()
        self.precio_var = StringVar()
        self.ultima_entrada_var = StringVar()
            

        self.buscar_entry_pro_var = StringVar()
        
        
        self.id_producto_entry = tk.Entry(self, textvariable= self.id_producto_var).place(x=780, y=150, width=200)
        
        self.categoria_en_material = control_bd.mostrar_categoria_material()
        self.lista_cat= []
        for self.cat in self.categoria_en_material:
            self.lista_cat.append("%s-%s" % (self.cat[0], self.cat[1]) )
            
        self.combo_categoria = ttk.Combobox(self,
        values=self.lista_cat)
        self.combo_categoria.place(x=780, y=190, width=200)
        
        self.producto_entry = tk.Entry(self, textvariable= self.producto_var).place(x=780, y=230, width=200)
        self.descripcion_entry= tk.Entry(self, textvariable= self.descripcion_var).place(x=780, y=270, width=200)
        self.marca_entry = tk.Entry(self, textvariable= self.marca_var).place(x=780, y=310, width=200)
        self.modelo_entry = tk.Entry(self, textvariable= self.modelo_var).place(x=780, y=350, width=200)
        self.proveedores_en_material = control_bd.mostrar_proveedores()
        self.lista_pro= []
        for self.pro in self.proveedores_en_material:
            self.lista_pro.append("%s-%s" % (self.pro[0], self.pro[1]) )
            
        self.combo_proveedor = ttk.Combobox(self,
        values=self.lista_pro)
        self.combo_proveedor.place(x=780, y=390, width=200)
        
        self.cantidad_entry = tk.Entry(self, textvariable= self.cantidad_var).place(x=780, y=430, width=200)
        self.precio_entry = tk.Entry(self, textvariable= self.precio_var).place(x=780, y=470, width=200)
        self.ultima_entrada_entry = tk.Entry(self, textvariable= self.ultima_entrada_var).place(x=794, y=510, width=150)

        #Comentarios
        self.textBox=tk.Text(self, height=4, width=28) 
        self.textBox.place(x=800, y=540)
        self.textBox.get('1.0','end')
            
            
        self.buscar_entry_pro = tk.Entry(self, textvariable= self.buscar_entry_pro_var).place(x=640, y=120, width=250)


            # Frame del treeview
        self.frame_treeview = tk.Frame(self.frame_fondo)
        self.frame_treeview.pack(fill=tk.Y, side=tk.BOTTOM)
        self.frame_treeview.config(bg="white", width=20, height=700)

        style = ttk.Style()
        style.configure("mystyle.Treeview",
            background = "red",
            foreground = "#303452",
            rowheight = 30,
            fieldbackground = "white"
        )

            # Set the treeview
        self.tree = ttk.Treeview(self.frame_treeview, style="mystyle.Treeview", height=17) #height ALTURA DEL TREEVIEW

        self.treexscroll = tk.Scrollbar(self.frame_treeview, orient=tk.HORIZONTAL)
        self.treexscroll.pack(fill=tk.X, side=tk.BOTTOM)
            # configurar scrollbar
        self.treexscroll.config(command=self.tree.xview)

        self.treeyscroll = tk.Scrollbar(self.frame_treeview, orient=tk.VERTICAL)
        self.treeyscroll.pack(fill=tk.Y, side=tk.RIGHT)
            # configurar scrollbar
        self.treeyscroll.config(command=self.tree.yview)

            # TREEVIEW
        self.tree.config(xscrollcommand=self.treexscroll.set, yscrollcommand=self.treeyscroll.set, 
        columns=(
                    "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10"))

        
        self.tree.column("#0", width=150, stretch= False)
        self.tree.column("col1", width=150, stretch= False)
        self.tree.column("col2", width=150, stretch= False)
        self.tree.column("col3", width=150, stretch= False)
        self.tree.column("col4", width=160, stretch= False)
        self.tree.column("col5", width=150, stretch= False)
        self.tree.column("col6", width=150, stretch= False)
        self.tree.column("col7", width=150, stretch= False)
        self.tree.column("col8", width=150, stretch= False)
        self.tree.column("col9", width=150, stretch= False)
        self.tree.column("col10", width=150, stretch= False)
            
            
        self.tree.heading("#0", text="Id producto", anchor=tk.CENTER)
        self.tree.heading("col1", text="Categoria", anchor=tk.CENTER)
        self.tree.heading("col2", text="Producto", anchor=tk.CENTER)
        self.tree.heading("col3", text="Descripcion", anchor=tk.CENTER)
        self.tree.heading("col4", text="Marca", anchor=tk.CENTER)
        self.tree.heading("col5", text="Modelo", anchor=tk.CENTER)
        self.tree.heading("col6", text="Id proveedor", anchor=tk.CENTER)
        self.tree.heading("col7", text= "cantidad", anchor=tk.CENTER)
        self.tree.heading("col8", text="precio", anchor=tk.CENTER)
        self.tree.heading("col9", text="Ultima entrada", anchor=tk.CENTER)
        self.tree.heading("col10", text="Comentarios", anchor=tk.CENTER)
            
            
        self.tree.pack()
        self.treeview = self.tree
            
        self.id = 0
        self.iid = 0

        self.mostrar()
            
            
        self.tree.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick)
        self.tree.bind('<<TreeviewSelect>>', self.bindings)


        #GESTION DE PRODUCTOS FUNCIONES


    def mostrar(self): #Actualizar treeview luego de modificar
            
            control_bd = bd()
            datos_apt = control_bd.mostrar_material()
            
            registros = self.tree.get_children()
            for elemento in registros:
                self.tree.delete(elemento)
            try:
                self.indice= 1
                for row in datos_apt:			
                    self.tree.tag_configure("#ecf0f6", background="#ecf0f6")
                    self.tree.tag_configure("white", background="white")
                    color = "white" if self.indice % 2 else "#ecf0f6"
                    id_cliente = row[0]
                    
                    self.tree.insert("",END, tag=('fuente', color), iid=id_cliente, text = row[0], values =(row[1], 
                    row[2],row[3], row[4], row[5],row[6], row[7],row[8], row[9], row[10]))
                    self.indice= self.indice+1
                            
            except:
                pass


        
        
    def mostrar_tabla_categoria(self):
            # Crear la ventana secundaria y pasar como argumento
            # la función en la cual queremos recibir el dato
            # ingresado.
            self.ventana_nombre = VentanaCategoriaEnMateriales()


    def limpiarCampos(self):
        
            self.id_producto_var.set("")
            self.combo_categoria.set("")
            self.producto_var.set("")
            self.descripcion_var.set("")
            self.marca_var.set("")
            self.modelo_var.set("")
            self.combo_proveedor.set("")
            self.cantidad_var.set("")
            self.precio_var.set("")
            self.ultima_entrada_var.set("")
            self.textBox.delete('1.0','end')
    

    def seleccionarUsandoClick(self, event):
            control_bd = bd()

            item = self.tree.identify('item', event.x, event.y)
            
            self.categoria_en_material = control_bd.mostrar_categoria_material()
            self.lista= list(enumerate(self.categoria_en_material))
            for segmento in self.lista:
                if int(self.tree.item(item, "values")[0]) == int(segmento[1][0]):
                    self.combo_categoria.current(int(segmento[0]))

            
            self.id_producto_var.set(self.tree.item(item, "text"))

            self.producto_var.set(self.tree.item(item, "values")[1])
            self.descripcion_var.set(self.tree.item(item, "values")[2])
            self.marca_var.set(self.tree.item(item, "values")[3])
            self.modelo_var.set(self.tree.item(item, "values")[4])
            
            self.proveedores_en_material = control_bd.mostrar_proveedores_para_material()
            self.lista2= list(enumerate(self.proveedores_en_material))
            for segmento2 in self.lista2:
                if int(self.tree.item(item, "values")[5]) == int(segmento2[1][0]):
                    self.combo_proveedor.current(int(segmento2[0]))
            
            self.id_proveedor_var.set(self.tree.item(item, "values")[5])
            
            self.cantidad_var.set(self.tree.item(item, "values")[6])
            self.precio_var.set(self.tree.item(item, "values")[7])
            self.ultima_entrada_var.set(self.tree.item(item, "values")[8])
            self.textBox.delete('1.0','end')
            self.textBox.insert('end', self.tree.item(item, "values")[9])

            print("you clicked on", self.tree.item(item,"text"))
            self.id_c = self.tree.item(item,"text")
            print(self.id_c)
            #self.tree.selection_set('0')
			
    
    
    def busqueda(self):
            control_bd = bd()
            

            try:
                self.criterio1 = ''
                self.criterio = self.buscar_entry_pro_var.get()
                print(self.criterio)
                self.criterio1 = "%s" % self.criterio +"%"
                self.datos = control_bd.busqueda_material(self.criterio1)
                print("Criterio1: ", self.criterio1)

                if self.criterio1 == '%':
                    messagebox.showwarning("ADVERTENCIA","Coloque criterio de busqueda")
                    
                elif self.criterio1 != '':
                    numeros = []
                    for row in self.datos:
                        numeros.append(row[0])
                        self.row_id = row[0]
                    self.tree.selection
                    self.tree.selection_set(self.tree.tag_has(self.row_id))
                    self.tree.selection_set(numeros) # move selection
                    self.tree.focus(self.row_id) # move focus
                    self.tree.see(self.row_id)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error de búsqueda")
                pass


    def bindings(self, event):
            self.tree.bind("<Button-1>", self.seleccionarUsandoClick)

    def bindings_ca(self, event):
            self.tree.bind("<Button-1>", self.seleccionarUsandoClick)
            


    def anadir_material(self):
        control_bd = bd()

        try:
            if self.id_producto_var.get() == '' or self.combo_categoria.get()=='' or self.producto_var.get()=='' or self.combo_proveedor.get()=='':
                messagebox.showwarning("ADVERTENCIA","Debe introducir id del producto, nombre y categoria del producto, asi como el id de su proveedor")
            else:
                datos = self.id_producto_var.get(), self.combo_categoria_var, self.producto_var.get(), self.descripcion_var.get(), self.marca_var.get(), self.modelo_var.get(), self.combo_proveedor_var, self.cantidad_var.get(), self.precio_var.get(), self.ultima_entrada_var.get(), self.textBox.get(1.0, tk.END+"-1c")
                control_bd.anadir_mat_bd(datos)
                messagebox.showinfo("REALIZADO","Material anadido")
        
        except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al anadir material")
                pass

        self.limpiarCampos()
        self.mostrar()



    def actualizar(self):
            control_bd = bd()

            try:
                self.combo_categoria_var = self.combo_categoria.get().split('-')
                self.combo_categoria_var = int(self.combo_categoria_var[0])
                print(self.combo_categoria_var)
                print(type(self.combo_categoria_var))
                

                self.combo_proveedor_var = self.combo_proveedor.get().split('-')
                self.combo_proveedor_var = int(self.combo_proveedor_var[0])
                print(self.combo_proveedor_var)
                print(type(self.combo_proveedor_var))


                datos_actualizar = self.id_producto_var.get(), self.combo_categoria_var, self.producto_var.get(), self.descripcion_var.get(), self.marca_var.get(), self.modelo_var.get(), self.combo_proveedor_var, self.cantidad_var.get(), self.precio_var.get(), self.ultima_entrada_var.get(), self.textBox.get(1.0, tk.END+"-1c"), self.id_c
                print("datos_actualizar:", datos_actualizar)
                control_bd.actualizar_material(datos_actualizar)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
                pass
            self.limpiarCampos()
            self.mostrar()

        
    def borrar(self):
        control_bd = bd()
        try:
            if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                control_bd.borrar_material(self.id_c)
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
            pass

        self.limpiarCampos()
        self.mostrar()

    def fecha_poner(self):
        self.fecha = datetime.today().strftime('%d-%m-%Y')
        self.ultima_entrada_var.set(self.fecha)


#---------------------------------------------------------------------------


#CLASE EQUIPO

class VentanaCategoriaEnEquipo(tk.Toplevel):
        def __init__(self, *args, callback=None, **kwargs):
            super().__init__(*args, **kwargs)
            
            self.wm_attributes("-topmost", True)
            self.geometry("640x600")
            self.title("Tabla categorias")
            self.configure(background="#ecf0f6")

            self.frame_fondo_toplevel = tk.Frame(self)
            self.frame_fondo_toplevel.pack(expand=True)
            self.frame_fondo_toplevel.config(bg="#ecf0f6", width=900, height=200)

            #Label fondo
            self.label_a= tk.Label(self.frame_fondo_toplevel, bg="#ecf0f6", relief=tk.SUNKEN)
            self.label_a.place(x=10, y=10, width=610, height= 225)
        
            #Stringvar
            self.categoria_id_var = StringVar()   
            self.categoria_nombre_var = StringVar()

            self.buscar_entry_cat_var = StringVar()

            #Labels
            self.agregar_categoria= tk.Label(self.frame_fondo_toplevel, text="Agregar categoria", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=15, y=1)

            self.categoria_id = tk.Label(self.frame_fondo_toplevel, text="ID de la Categoria:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=60)  
            self.categoria_nombre = tk.Label(self.frame_fondo_toplevel, text="Nombre de la categoria:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=100)

            #Entry
            self.buscar_entry_ca = tk.Entry(self.frame_fondo_toplevel, textvariable= self.buscar_entry_cat_var).place(x=15, y=30, width=250)
            self.categoria_id_entry = tk.Entry(self.frame_fondo_toplevel, textvariable= self.categoria_id_var).place(x=260, y=60, width=250)
            self.categoria_nombre_entry= tk.Entry(self.frame_fondo_toplevel, textvariable= self.categoria_nombre_var).place(x=260, y=100, width=250)

            #Buttom
            self.buscar_ca = tk.Button(self.frame_fondo_toplevel, text="Buscar", command= self.busqueda_categ, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=280, y=26) 

            self.anadir_ca= tk.Button(self.frame_fondo_toplevel, text="Agregar", command= self.anadir_equipo_ca, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 15, y = 150) 
            self.actualizar_ca = tk.Button(self.frame_fondo_toplevel, text="Actualizar", command= self.actualizar_categ, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 160, y = 150)
            self.eliminar_ca = tk.Button(self.frame_fondo_toplevel, text="Borrar", command= self.borrar_categ, bg='#72729a', fg='white', font=("Arial",10,"bold"),width=15, height=1).place(x = 310, y = 150) 
            self.limpiar_ca = tk.Button(self.frame_fondo_toplevel, text="Limpiar campos", command= self.limpiarCampos_ca, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 460, y = 150) 

            # Frame del treeview
            self.frame_treeview2 = tk.Frame(self)
            self.frame_treeview2.pack(fill=tk.Y, side=tk.BOTTOM)
            self.frame_treeview2.config(bg="white", width=20, height=30)

            style2 = ttk.Style()
            style2.configure("mystyle.Treeview",
                background = "red",
                foreground = "#303452",
                rowheight = 30,
                fieldbackground = "white"
                )

            # Set the treeview
            self.tree2 = ttk.Treeview(self.frame_treeview2, style="mystyle.Treeview", height=12)

            self.treexscroll2 = tk.Scrollbar(self.frame_treeview2, orient=tk.HORIZONTAL)
            self.treexscroll2.pack(fill=tk.X, side=tk.BOTTOM)
            # configurar scrollbar
            self.treexscroll2.config(command=self.tree2.xview)

            self.treeyscroll2 = tk.Scrollbar(self.frame_treeview2, orient=tk.VERTICAL)
            self.treeyscroll2.pack(fill=tk.Y, side=tk.RIGHT)
            # configurar scrollbar
            self.treeyscroll2.config(command=self.tree2.yview)

            # TREEVIEW
            self.tree2.config(xscrollcommand=self.treexscroll2.set, yscrollcommand=self.treeyscroll2.set, 
            columns=(
                    "col1"))

        
            self.tree2.column("#0", width=150, stretch= False)
            self.tree2.column("col1", width=150, stretch= False)
            
            self.tree2.heading("#0", text="Id categoria", anchor=tk.CENTER)
            self.tree2.heading("col1", text="Categoria", anchor=tk.CENTER)
            
            
            self.tree2.pack()
            self.treeview2 = self.tree2
            
            self.id = 0
            self.iid = 0

            self.tree2.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick_ca)
            self.tree2.bind('<<TreeviewSelect>>', self.bindings_ca)

            self.mostrar_ca()

            

        def mostrar_ca(self): #Actualizar treeview luego de modificar
            
            control_bd = bd()
            datos_apt2 = control_bd.mostrar_categoria_equipo()
            
            registros2 = self.tree2.get_children()
            for elemento2 in registros2:
                self.tree2.delete(elemento2)
            try:
                self.indice= 1
                for row2 in datos_apt2:	
                    print(row2[1])		
                    self.tree2.tag_configure("#ecf0f6", background="#ecf0f6")
                    self.tree2.tag_configure("white", background="white")
                    color = "white" if self.indice % 2 else "#ecf0f6"
                    
                    self.tree2.insert("",END, tag=('fuente', color), iid= row2[0], text = row2[0], values =row2[1])
                    self.indice= self.indice+1
                            
            except:
                self.wm_attributes("-topmost", False)
                print("ocurrio un error en mostrar_tabla_categoria")
                self.wm_attributes("-topmost", True)


        def limpiarCampos_ca(self):
        
            self.categoria_id_var.set("")
            self.categoria_nombre_var.set("")
            
        
        def seleccionarUsandoClick_ca(self, event):

            item = self.tree2.identify('item', event.x, event.y)
            self.categoria_id_var.set(self.tree2.item(item, "text"))
            self.categoria_nombre_var.set(self.tree2.item(item, "values")[0])

            print("you clicked on", self.tree2.item(item,"text"))
            self.id_c = self.tree2.item(item,"text")
            print(self.id_c)


        def bindings_ca(self, event):
            self.tree2.bind("<Button-1>", self.seleccionarUsandoClick_ca)

        def anadir_equipo_ca(self):
            control_bd = bd()

            try:
                if self.categoria_id_var.get() == '' or self.categoria_nombre_var.get()=='':
                    self.wm_attributes("-topmost", False)
                    messagebox.showwarning("ADVERTENCIA","Debe introducir id del producto, nombre y categoria del producto, asi como el id de su proveedor")
                    self.wm_attributes("-topmost", True)
                else:
                    datos = self.categoria_id_var.get(), self.categoria_nombre_var.get()
                    control_bd.anadir_eq_ca_bd(datos)
                    self.wm_attributes("-topmost", False)
                    messagebox.showinfo("REALIZADO","Nueva categoria agregada")
                    self.wm_attributes("-topmost", True)
        
            except:
                self.wm_attributes("-topmost", False)
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al anadir material")
                self.wm_attributes("-topmost", True)
                pass

            self.limpiarCampos_ca()
            self.mostrar_ca()

        def actualizar_categ(self):
            control_bd = bd()

            try:
                datos_actualizar = self.categoria_id_var.get(), self.categoria_nombre_var.get(), self.id_c
                control_bd.actualizar_equipo_ca(datos_actualizar)

            except:
                self.wm_attributes("-topmost", False)
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
                self.wm_attributes("-topmost", True)
                pass
            
            self.limpiarCampos_ca()
            self.mostrar_ca()

        
        def borrar_categ(self):
            control_bd = bd()
            try:
                self.wm_attributes("-topmost", False)
                if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                    self.wm_attributes("-topmost", True)
                    control_bd.borrar_equipo_ca(self.id_c)
                self.wm_attributes("-topmost", True)

            except:
                self.wm_attributes("-topmost", False)
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
                self.wm_attributes("-topmost", True)
                pass

            self.limpiarCampos_ca()
            self.mostrar_ca()


        def busqueda_categ(self):
            control_bd = bd()
            
            try:
                self.criterio1 = ''
                self.criterio = self.buscar_entry_cat_var.get()
                print(self.criterio)
                self.criterio1 = "%s" % self.criterio +"%"
                self.datos = control_bd.busqueda_equipo_ca(self.criterio1)
                print("Criterio1: ", self.criterio1)

                if self.criterio1 == '%':
                    self.wm_attributes("-topmost", False)
                    messagebox.showwarning("ADVERTENCIA","Coloque criterio de busqueda")
                    self.wm_attributes("-topmost", True)
                    
                elif self.criterio1 != '':
                    numeros = []
                    for row in self.datos:
                        numeros.append(row[0])
                        self.row_id = row[0]
                    self.tree2.selection
                    self.tree2.selection_set(self.tree2.tag_has(self.row_id))
                    self.tree2.selection_set(numeros) # move selection
                    self.tree2.focus(self.row_id) # move focus
                    self.tree2.see(self.row_id)
            except:
                self.wm_attributes("-topmost", False)
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error de búsqueda")
                self.wm_attributes("-topmost", True)
                pass




#Clase equipo

class Clase_equipo(tk.Frame): 
    
    def __init__(self, parent, controller):
		
        tk.Frame.__init__(self, parent) 
        control_bd = bd()
        
        print("CLASE_EQUIPO") 


        def mientras():
            pass
        
        

        self.config(bg="#ecf0f6", width=2440, height=300)

        self.frame_fondo = tk.Frame(self)
        self.frame_fondo.pack(expand=True)
        self.frame_fondo.config(bg="#ecf0f6", width=1440, height=20)

        self.label_a= tk.Label(self.frame_fondo, bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_a.place(x=10, y=90, width=610, height= 70)  

        #self.fondo = ImageTk.PhotoImage(Image.open("img/fondo_azul.jpg"))
        
        self.frame_1 = tk.Frame(self.frame_fondo)
        self.frame_1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.frame_1.config(bg="#ecf0f6", width=500, height=90)

        self.frame_2 = tk.Frame(self.frame_fondo)
        self.frame_2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        self.frame_2.config(bg="#ecf0f6", width=400, height=700)

        self.label_b= tk.Label(self.frame_2, bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_b.place(x=10, y=1, width=380, height= 610)

        self.label_c= tk.Label(self.frame_fondo, bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_c.place(x=10, y=180, width=610, height= 190) 


                #Buttons
        self.button_proyectos = tk.Button(self, text="Proyectos", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20, height=1 ).place(x = 0, y = 0)      
        self.button_clientes = tk.Button(self, text="Clientes", command = lambda:controller.show_frame(Clase_clientes), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 170, y = 0)     
        self.button_proveedores = tk.Button(self, text="Proveedores", command = lambda:controller.show_frame(Clase_proveedores), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 340, y = 0) 
        self.button_material = tk.Button(self, text="Material", command = lambda:controller.show_frame(Clase_material), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20,height=1).place(x=510, y=0)
        self.button_empleados = tk.Button(self, text="Empleados", command = lambda:controller.show_frame(Clase_empleados),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=680, y=0)
        self.button_menu = tk.Button(self, text="Menu", command = lambda:controller.show_frame(Clase_menu),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=850, y=0)


        self.mostrar_tabla_de_categoria = tk.Button(self, text="Mostrar tabla categorias", command = self.mostrar_tabla_categoria, bg='#72729a', fg='white', font=("Arial",10,"bold"),width=25, height=1).place(x = 190, y = 105) 
        

        self.anadir_eq = tk.Button(self, text="Añadir equipo",command = self.anadir_equipo, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 680, y = 610) 
        self.actualizar_eq = tk.Button(self, text="Actualizar", command = self.actualizar, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 865, y = 610)
        self.eliminar_eq = tk.Button(self, text="Eliminar equipo", command = self.borrar, bg='#72729a', fg='white', font=("Arial",10,"bold"),width=15, height=1).place(x = 680, y = 650) 
        self.limpiar_eq = tk.Button(self, text="Limpiar equipo", command = self.limpiarCampos, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 865, y = 650)  
        

        self.buscar_eq = tk.Button(self, text="Buscar", command = self.busqueda, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=910, y=115) 

        
        #Depreciacion de equipo
        self.linea_recta_anual = tk.Button(self, text="Por linea recta anual", command = self.mostrar_ventana_depreciacion_LRA, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 40, y = 210) 
        self.Linea_recta_mensual = tk.Button(self, text="Por linea recta mensual",command = self.mostrar_ventana_depreciacion_LRM, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 40, y = 250)
        self.suma_digitos_anuales = tk.Button(self, text="Por suma de los digitos anuales", bg='#72729a', fg='white', font=("Arial",10,"bold"),width=29, height=1).place(x = 40, y = 290) 
        self.reduccion_datos = tk.Button(self, text="Por reduccion de datos", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 40, y = 330)  


        self.linea_recta_anual_gr = tk.Button(self, text="Ver valor recta anual", command = self.Valor_Depreciacion_LRA, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 210) 
        self.Linea_recta_mensual_gr = tk.Button(self, text="Ver valor recta mensual", command = self.Valor_Depreciacion_LRM, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 250)
        self.suma_digitos_anuales_gr = tk.Button(self, text="Ver grafica digitos anuales", bg='#72729a', fg='white', font=("Arial",10,"bold"),width=29, height=1).place(x = 350, y = 290) 
        self.reduccion_datos_gr = tk.Button(self, text="Ver grafica reduccion de datos", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 330)  



                #Labels
        self.agregar_categoria= tk.Label(self, text="Agregar categoria", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=15, y=80)   
        self.depreciacion_equip= tk.Label(self, text="Depreciacion de equipo", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=15, y=170)   
        self.gestion_equipo= tk.Label(self, text="Gestion de equipo", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=650, y=80) 
        
        
        self.id_equipo_label = tk.Label(self, text="ID equipo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=150)
        self.categoria_label = tk.Label(self, text="Categoria:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=200)
        self.equipo_label = tk.Label(self, text="Equipo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=250)
        self.descripcion_label = tk.Label(self, text="Descripcion:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=300)
        self.marca_label = tk.Label(self, text="Marca:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=350)
        self.modelo_label = tk.Label(self, text="Modelo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=400)
        self.id_proveedor_label = tk.Label(self, text="ID proveedor:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=450)
        self.comentarios_label = tk.Label(self, text="Comentarios:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=640, y=500)
        
            
        
        #Entry    
        self.categoria_id_var = StringVar()   
        self.categoria_nombre_var = StringVar() 
        
        self.id_equipo_var = StringVar()
        self.categoria_var = StringVar()
        self.equipo_var = StringVar()
        self.descripcion_var = StringVar()
        self.marca_var = StringVar()
        self.modelo_var = StringVar()
        self.id_proveedor_var = StringVar()
            
        self.buscar_entry_eq_var = StringVar()

        
        self.id_equipo_entry = tk.Entry(self,  textvariable= self.id_equipo_var).place(x=780, y=150, width=200)
        
        self.categoria_en_material = control_bd.mostrar_categoria_equipo()
        self.lista_cat= []
        for self.cat in self.categoria_en_material:
            self.lista_cat.append("%s-%s" % (self.cat[0], self.cat[1]) )
            
        self.combo_categoria = ttk.Combobox(self,
        values=self.lista_cat)
        self.combo_categoria.place(x=780, y=200, width=200)
        
        self.equipo_entry = tk.Entry(self, textvariable= self.equipo_var).place(x=780, y=250, width=200)
        self.descripcion_entry= tk.Entry(self, textvariable= self.descripcion_var).place(x=780, y=300, width=200)
        self.marca_entry = tk.Entry(self, textvariable= self.marca_var).place(x=780, y=350, width=200)
        self.modelo_entry = tk.Entry(self, textvariable= self.modelo_var).place(x=780, y=400, width=200)
        self.proveedores_en_equipo = control_bd.mostrar_proveedores_para_equipo()
        self.lista_eq= []
        for self.eq in self.proveedores_en_equipo:
            self.lista_eq.append("%s-%s" % (self.eq[0], self.eq[1]) )
            
        self.combo_proveedor = ttk.Combobox(self,
        values=self.lista_eq)
        self.combo_proveedor.place(x=780, y=450, width=200)
        

        #Comentarios
        self.textBox=tk.Text(self, height=4, width=28) 
        self.textBox.place(x=800, y=500)
        self.textBox.get('1.0','end')
            
            
        self.buscar_entry_eq = tk.Entry(self, textvariable= self.buscar_entry_eq_var).place(x=640, y=120, width=250)


        # Frame del treeview
        self.frame_treeview = tk.Frame(self.frame_fondo)
        self.frame_treeview.pack(fill=tk.Y, side=tk.BOTTOM)
        self.frame_treeview.config(bg="white", width=20, height=700)

        style = ttk.Style()
        style.configure("mystyle.Treeview",
            background = "red",
            foreground = "#303452",
            rowheight = 30,
            fieldbackground = "white"
        )

        # Set the treeview
        self.tree = ttk.Treeview(self.frame_treeview, style="mystyle.Treeview", height=10) #height ALTURA DEL TREEVIEW

        self.treexscroll = tk.Scrollbar(self.frame_treeview, orient=tk.HORIZONTAL)
        self.treexscroll.pack(fill=tk.X, side=tk.BOTTOM)
        # configurar scrollbar
        self.treexscroll.config(command=self.tree.xview)

        self.treeyscroll = tk.Scrollbar(self.frame_treeview, orient=tk.VERTICAL)
        self.treeyscroll.pack(fill=tk.Y, side=tk.RIGHT)
        # configurar scrollbar
        self.treeyscroll.config(command=self.tree.yview)

        # TREEVIEW
        self.tree.config(xscrollcommand=self.treexscroll.set, yscrollcommand=self.treeyscroll.set, 
        columns=(
                    "col1", "col2", "col3", "col4", "col5", "col6", "col7"))

        
        self.tree.column("#0", width=150, stretch= False)
        self.tree.column("col1", width=150, stretch= False)
        self.tree.column("col2", width=150, stretch= False)
        self.tree.column("col3", width=150, stretch= False)
        self.tree.column("col4", width=160, stretch= False)
        self.tree.column("col5", width=150, stretch= False)
        self.tree.column("col6", width=150, stretch= False)
        self.tree.column("col7", width=150, stretch= False)
            
        
            
        self.tree.heading("#0", text="Id equipo", anchor=tk.CENTER)
        self.tree.heading("col1", text="Categoria", anchor=tk.CENTER)
        self.tree.heading("col2", text="Equipo", anchor=tk.CENTER)
        self.tree.heading("col3", text="Descripcion", anchor=tk.CENTER)
        self.tree.heading("col4", text="Marca", anchor=tk.CENTER)
        self.tree.heading("col5", text="Modelo", anchor=tk.CENTER)
        self.tree.heading("col6", text="Id proveedor", anchor=tk.CENTER)
        self.tree.heading("col7", text="Comentarios", anchor=tk.CENTER)
            
            

        self.tree.pack()
        self.treeview = self.tree
            
        self.id = 0
        self.iid = 0

        self.mostrar()
            
            
        self.tree.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick)
        self.tree.bind('<<TreeviewSelect>>', self.bindings)



    #GESTION DE PRODUCTOS FUNCIONES

    def mostrar(self): #Actualizar treeview luego de modificar
            
            control_bd = bd()
            datos_apt = control_bd.mostrar_equipo()
            
            registros = self.tree.get_children()
            for elemento in registros:
                self.tree.delete(elemento)
            try:
                self.indice= 1
                for row in datos_apt:			
                    self.tree.tag_configure("#ecf0f6", background="#ecf0f6")
                    self.tree.tag_configure("white", background="white")
                    color = "white" if self.indice % 2 else "#ecf0f6"
                    id_cliente = row[0]
                    
                    self.tree.insert("",END, tag=('fuente', color), iid=id_cliente, text = row[0], values =(row[1], 
                    row[2],row[3], row[4], row[5],row[6], row[7]))
                    self.indice= self.indice+1
                            
            except:
                pass


        
        
    def mostrar_tabla_categoria(self):
            # Crear la ventana secundaria y pasar como argumento
            # la función en la cual queremos recibir el dato
            # ingresado.
            self.ventana_nombre = VentanaCategoriaEnEquipo()


    def mostrar_ventana_depreciacion_LRA(self):
            
            self.ventana_depreciacion_LRA = VentanaDepreciacionLRA()


    def mostrar_ventana_depreciacion_LRM(self):
            
            self.ventana_depreciacion_LRM = VentanaDepreciacionLRM()


    def limpiarCampos(self):
        
            self.id_equipo_var.set("")
            self.combo_categoria.set("")
            self.equipo_var.set("")
            self.descripcion_var.set("")
            self.marca_var.set("")
            self.modelo_var.set("")
            self.combo_proveedor.set("")
            
            self.textBox.delete('1.0','end')
    

    def seleccionarUsandoClick(self, event):
            control_bd = bd()

            item = self.tree.identify('item', event.x, event.y)
            
            self.categoria_en_equipo = control_bd.mostrar_categoria_equipo()
            self.lista= list(enumerate(self.categoria_en_equipo))
            for segmento in self.lista:
                if int(self.tree.item(item, "values")[0]) == int(segmento[1][0]):
                    self.combo_categoria.current(int(segmento[0]))

            
            self.id_equipo_var.set(self.tree.item(item, "text"))

            self.equipo_var.set(self.tree.item(item, "values")[1])
            self.descripcion_var.set(self.tree.item(item, "values")[2])
            self.marca_var.set(self.tree.item(item, "values")[3])
            self.modelo_var.set(self.tree.item(item, "values")[4])
            
            self.proveedores_en_equipo = control_bd.mostrar_proveedores_para_equipo()
            self.lista2= list(enumerate(self.proveedores_en_equipo))
            for segmento2 in self.lista2:
                if int(self.tree.item(item, "values")[5]) == int(segmento2[1][0]):
                    self.combo_proveedor.current(int(segmento2[0]))
            
            self.id_proveedor_var.set(self.tree.item(item, "values")[5])
            

            self.textBox.delete('1.0','end')
            self.textBox.insert('end', self.tree.item(item, "values")[6])

            self.id_c = self.tree.item(item,"text")
            self.lista_depreciacion = control_bd.detectar_depreciacion(self.id_c)

            for self.dep in self.lista_depreciacion:
                if self.dep[0] is not None:
                    if len(self.dep[0]) < 1 or self.dep[0] == 0:
                        self.linea_recta_anual_gr = tk.Button(self, text="Ver valor recta anual", command = self.Valor_Depreciacion_LRA, bg='red', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 210) 
                    if len(self.dep[0]) >= 1 and self.dep[0] != 0:
                        self.linea_recta_anual_gr = tk.Button(self, text="Ver valor recta anual", command = self.Valor_Depreciacion_LRA, bg='green', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 210) 
                if self.dep[0] is None:
                    self.linea_recta_anual_gr = tk.Button(self, text="Ver valor recta anual", command = self.Valor_Depreciacion_LRA, bg='red', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 210) 


                if self.dep[1] is not None:
                    if len(self.dep[1]) < 1 or self.dep[1] == 0:
                        self.Linea_recta_mensual_gr = tk.Button(self, text="Ver valor recta mensual", bg='red', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 250) 
                    if len(self.dep[1]) >= 1 and self.dep[1] != 0:
                        self.Linea_recta_mensual_gr = tk.Button(self, text="Ver valor recta mensual", bg='green', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 250)
                if self.dep[1] is None:
                    self.Linea_recta_mensual_gr = tk.Button(self, text="Ver valor recta mensual", bg='red', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 250)  


                if self.dep[2] is not None:
                    if len(self.dep[2]) < 1 or self.dep[2] == 0:
                        self.suma_digitos_anuales_gr = tk.Button(self, text="Ver grafica digitos anuales", bg='red', fg='white', font=("Arial",10,"bold"),width=29, height=1).place(x = 350, y = 290)  
                    if len(self.dep[2]) >= 1 and self.dep[2] != 0:
                        self.suma_digitos_anuales_gr = tk.Button(self, text="Ver grafica digitos anuales", bg='green', fg='white', font=("Arial",10,"bold"),width=29, height=1).place(x = 350, y = 290)  
                if self.dep[2] is None:
                    self.suma_digitos_anuales_gr = tk.Button(self, text="Ver grafica digitos anuales", bg='red', fg='white', font=("Arial",10,"bold"),width=29, height=1).place(x = 350, y = 290) 

                if self.dep[3] is not None:
                    if len(self.dep[3]) < 1 or self.dep[3] == 0:
                        self.reduccion_datos_gr = tk.Button(self, text="Ver grafica reduccion de datos", bg='red', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 330)  
                    if len(self.dep[3]) >= 1 and self.dep[3] != 0:
                        self.reduccion_datos_gr = tk.Button(self, text="Ver grafica reduccion de datos", bg='green', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 330) 
                if self.dep[3] is None:
                    self.reduccion_datos_gr = tk.Button(self, text="Ver grafica reduccion de datos", bg='red', fg='white', font=("Arial",10,"bold"), width=29, height=1).place(x = 350, y = 330) 



            print("you clicked on", self.tree.item(item,"text"))
            self.id_c = self.tree.item(item,"text")
            print(self.id_c)
            control_bd.poner_id_equipo(self.id_c)
            #self.tree.selection_set('0')
			
    
    
    def busqueda(self):
            control_bd = bd()
            

            try:
                self.criterio1 = ''
                self.criterio = self.buscar_entry_eq_var.get()
                print(self.criterio)
                self.criterio1 = "%s" % self.criterio +"%"
                self.datos = control_bd.busqueda_equipo(self.criterio1)
                print("Criterio1: ", self.criterio1)

                if self.criterio1 == '%':
                    messagebox.showwarning("ADVERTENCIA","Coloque criterio de busqueda")
                    
                elif self.criterio1 != '':
                    numeros = []
                    for row in self.datos:
                        numeros.append(row[0])
                        self.row_id = row[0]
                    self.tree.selection
                    self.tree.selection_set(self.tree.tag_has(self.row_id))
                    self.tree.selection_set(numeros) # move selection
                    self.tree.focus(self.row_id) # move focus
                    self.tree.see(self.row_id)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error de búsqueda")
                pass


    def bindings(self, event):
            self.tree.bind("<Button-1>", self.seleccionarUsandoClick)

    def bindings_ca(self, event):
            self.tree.bind("<Button-1>", self.seleccionarUsandoClick)
            


    def anadir_equipo(self):
        control_bd = bd()
        print("A")

        try:
            print("B")
            if self.id_equipo_var.get() == '' or self.combo_categoria.get()=='' or self.equipo_var.get()=='' or self.combo_proveedor.get()=='':
                messagebox.showwarning("ADVERTENCIA","Debe introducir id del producto, nombre y categoria del producto, asi como el id de su proveedor")
            else:
                print("C")
                print(self.id_equipo_var.get(), self.combo_categoria_var, self.equipo_var.get(), self.descripcion_var.get(), self.marca_var.get(), self.modelo_var.get(), self.combo_proveedor_var, self.textBox.get(1.0, tk.END+"-1c"))
                self.data = self.id_equipo_var.get(), self.combo_categoria_var, self.equipo_var.get(), self.descripcion_var.get(), self.marca_var.get(), self.modelo_var.get(), self.combo_proveedor_var, self.textBox.get(1.0, tk.END+"-1c")
                print("self.data", self.data)
                print("D")
                control_bd.anadir_eq_bd(self.data)
                print("E")
                messagebox.showinfo("REALIZADO","Material anadido")
        
        except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al anadir equipo")
                pass

        self.limpiarCampos()
        self.mostrar()



    def actualizar(self):
            control_bd = bd()

            try:
                self.combo_categoria_var = self.combo_categoria.get().split('-')
                self.combo_categoria_var = int(self.combo_categoria_var[0])
                print(self.combo_categoria_var)
                print(type(self.combo_categoria_var))
                

                self.combo_proveedor_var = self.combo_proveedor.get().split('-')
                self.combo_proveedor_var = int(self.combo_proveedor_var[0])
                print(self.combo_proveedor_var)
                print(type(self.combo_proveedor_var))


                datos_actualizar = self.id_equipo_var.get(), self.combo_categoria_var, self.equipo_var.get(), self.descripcion_var.get(), self.marca_var.get(), self.modelo_var.get(), self.combo_proveedor_var, self.textBox.get(1.0, tk.END+"-1c"), self.id_c
                print("datos_actualizar:", datos_actualizar)
                control_bd.actualizar_equipo(datos_actualizar)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error al actualizar el registro")
                pass
            self.limpiarCampos()
            self.mostrar()

        
    def borrar(self):
        control_bd = bd()
        try:
            if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
                control_bd.borrar_equipo(self.id_c)
        except:
            messagebox.showwarning("ADVERTENCIA","Ocurrió un error al tratar de eliminar el registro")
            pass

        self.limpiarCampos()
        self.mostrar()

    def Valor_Depreciacion_LRA(self):
        print("Valor depreciacion anual")
        control_bd = bd()
        self.top = tk.Toplevel(self)
        self.top.wm_attributes("-topmost", True)
        self.top.geometry("640x200")
        self.top.title("Tabla categorias")
        self.top.configure(background="#ecf0f6")

        self.frame_fondo_toplevel = tk.Frame(self.top)
        self.frame_fondo_toplevel.pack(expand=True)
        self.frame_fondo_toplevel.config(bg="#ecf0f6", width=900, height=50)

        self.id = control_bd.tomar_id_equipo()
        print("self.id", self.id[0][0])

        self.lista_depreciacion = control_bd.detectar_depreciacion(self.id[0][0])

        for self.dep in self.lista_depreciacion:
            print(self.dep[0])
        
        self.ver = tk.Label(self.frame_fondo_toplevel, text="Depreciacion por linea recta anual:", font=("Arial", 15, "bold"), bg="#ecf0f6", fg='#72729a' ).place(x=20, y=1) 
        self.ver = tk.Label(self.frame_fondo_toplevel, text=str(self.dep[0]), font=("Arial", 18, "bold"), bg="#ecf0f6", fg='#72729a' ).place(x=450, y=1)          


    def Valor_Depreciacion_LRM(self):

        print("Valor depreciacion mensual")
        control_bd = bd()
        self.top1 = tk.Toplevel(self)
        self.top1.wm_attributes("-topmost", True)
        self.top1.geometry("640x200")
        self.top1.title("Tabla categorias")
        self.top1.configure(background="#ecf0f6")

        self.frame_fondo_toplevel1 = tk.Frame(self.top1)
        self.frame_fondo_toplevel1.pack(expand=True)
        self.frame_fondo_toplevel1.config(bg="#ecf0f6", width=900, height=50)

        self.id = control_bd.tomar_id_equipo()
        print("self.id", self.id[0][0])

        self.lista_depreciacion1 = control_bd.detectar_depreciacion(self.id[0][0])

        for self.dep1 in self.lista_depreciacion1:
            print(self.dep1[1])
        
        self.ver1 = tk.Label(self.frame_fondo_toplevel1, text="Depreciacion por linea recta mensual:", font=("Arial", 15, "bold"), bg="#ecf0f6", fg='#72729a' ).place(x=20, y=1) 
        self.ver1 = tk.Label(self.frame_fondo_toplevel1, text=str(self.dep1[1]), font=("Arial", 18, "bold"), bg="#ecf0f6", fg='#72729a' ).place(x=450, y=1)        


#DEPRECIACION DE EQUIPO

#Ventana depreciacion por linea recta anual

class VentanaDepreciacionLRA(tk.Toplevel):
        def __init__(self, *args, callback=None, **kwargs):
            super().__init__(*args, **kwargs)
            
            self.wm_attributes("-topmost", True)
            self.geometry("640x800")
            self.title("Tabla categorias")
            self.configure(background="#ecf0f6")

            self.frame_fondo_toplevel = tk.Frame(self)
            self.frame_fondo_toplevel.pack(expand=True)
            self.frame_fondo_toplevel.config(bg="#ecf0f6", width=900, height=400)

            #Label fondo
            self.label_a= tk.Label(self.frame_fondo_toplevel, bg="#ecf0f6", relief=tk.SUNKEN)
            self.label_a.place(x=15, y=10, width=610, height= 350)
        
            #Stringvar
            self.categoria_id_var = StringVar()   
            self.categoria_nombre_var = StringVar()
            
            self.valor_equipo_var = StringVar()
            self.equipo_vida_util_var = StringVar()
            self.valor_residual_opcional_var = StringVar()
            
            self.depreciacion_anual_var = StringVar()


            self.buscar_entry_var = StringVar()

            #Labels
            self.agregar_categoria= tk.Label(self.frame_fondo_toplevel, text="Agregar categoria", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=20, y=1)

            self.id_equipo = tk.Label(self.frame_fondo_toplevel, text="ID Equipo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=20, y=60)  
            self.equipo = tk.Label(self.frame_fondo_toplevel, text="Equipo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=300, y=60)
            self.valor_equipo = tk.Label(self.frame_fondo_toplevel, text="Valor Equipo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=20, y=100)  
            self.equipo_vida_util= tk.Label(self.frame_fondo_toplevel, text="Equipo Vida Util (años):", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=20, y=140)
            self.valor_residual_opcional = tk.Label(self.frame_fondo_toplevel, text="Valor Residual :", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=20, y=180)
            self.valor_residual_opcional = tk.Label(self.frame_fondo_toplevel, text="(Puede ser igual a cero)", font=("Arial",8), bg="#ecf0f6", fg="#303452" ).place(x=20, y=200)
            self.depreciacion_anual = tk.Label(self.frame_fondo_toplevel, text="Depreciacion anual:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=20, y=260)

            self.id_equipo_ver = tk.Label(self.frame_fondo_toplevel, textvariable=self.categoria_id_var, relief=tk.SUNKEN, font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=130, y=60, width=150)
            self.equipo_ver = tk.Label(self.frame_fondo_toplevel, textvariable=self.categoria_nombre_var, relief=tk.SUNKEN, font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=390, y=60, width=220)
            self.depreciacion_ver = tk.Label(self.frame_fondo_toplevel, textvariable=self.depreciacion_anual_var, relief=tk.SUNKEN, font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=300, y=260, width=220)


            #Entry
            self.buscar_entry_ca = tk.Entry(self.frame_fondo_toplevel, textvariable= self.buscar_entry_var).place(x=20, y=30, width=250)
            
            self.valor_equipo_entry = tk.Entry(self.frame_fondo_toplevel, textvariable= self.valor_equipo_var).place(x=280, y=100, width=250)
            self.equipo_vida_util_entry= tk.Entry(self.frame_fondo_toplevel, textvariable= self.equipo_vida_util_var).place(x=280, y=140, width=250)

            self.valor_residual_opcional_entry= tk.Entry(self.frame_fondo_toplevel, textvariable= self.valor_residual_opcional_var).place(x=280, y=180, width=250)

            #Buttom
            self.buscar_ca = tk.Button(self.frame_fondo_toplevel, text="Buscar", command= self.busqueda , bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=280, y=26) 

            self.calcular_boton = tk.Button(self.frame_fondo_toplevel, text="Calcular", command= self.calcular, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 250, y = 220)
            

            # Frame del treeview
            self.frame_treeview3 = tk.Frame(self)
            self.frame_treeview3.pack(fill=tk.Y, side=tk.BOTTOM)
            self.frame_treeview3.config(bg="white", width=20, height=30)

            style2 = ttk.Style()
            style2.configure("mystyle.Treeview",
                background = "red",
                foreground = "#303452",
                rowheight = 30,
                fieldbackground = "white"
                )

                    # Set the treeview
            self.tree3 = ttk.Treeview(self.frame_treeview3, style="mystyle.Treeview", height=12)

            self.treexscroll3 = tk.Scrollbar(self.frame_treeview3, orient=tk.HORIZONTAL)
            self.treexscroll3.pack(fill=tk.X, side=tk.BOTTOM)
            # configurar scrollbar
            self.treexscroll3.config(command=self.tree3.xview)

            self.treeyscroll3 = tk.Scrollbar(self.frame_treeview3, orient=tk.VERTICAL)
            self.treeyscroll3.pack(fill=tk.Y, side=tk.RIGHT)
            # configurar scrollbar
            self.treeyscroll3.config(command=self.tree3.yview)

            # TREEVIEW
            self.tree3.config(xscrollcommand=self.treexscroll3.set, yscrollcommand=self.treeyscroll3.set, 
            columns=(
                    "col1", "col2", "col3", "col4", "col5"))

        
            self.tree3.column("#0", width=150, stretch= False)
            self.tree3.column("col1", width=150, stretch= False)
            self.tree3.column("col2", width=150, stretch= False)
            self.tree3.column("col3", width=190, stretch= False)
            self.tree3.column("col4", width=150, stretch= False)
            self.tree3.column("col5", width=250, stretch= False)
            
            
            self.tree3.heading("#0", text="ID equipo", anchor=tk.CENTER)
            self.tree3.heading("col1", text="equipo", anchor=tk.CENTER)
            self.tree3.heading("col2", text="Valor del activo", anchor=tk.CENTER)
            self.tree3.heading("col3", text="Vida util activo años", anchor=tk.CENTER)
            self.tree3.heading("col4", text="Valor residual", anchor=tk.CENTER)
            self.tree3.heading("col5", text="Depreciacion linea recta anual", anchor=tk.CENTER)
            
            
            self.tree3.pack()
            self.treeview3 = self.tree3
            
            self.id = 0
            self.iid = 0

            self.tree3.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick_3)
            self.tree3.bind('<<TreeviewSelect>>', self.bindings_3)

            self.mostrar_ca()

            

        def mostrar_ca(self): #Actualizar treeview luego de modificar
            
            control_bd = bd()
            datos_apt3 = control_bd.mostrar_equipo()
            
            registros3 = self.tree3.get_children()
            for elemento3 in registros3:
                self.tree3.delete(elemento3)
            try:
                self.indice= 1
                for row2 in datos_apt3:		
                    self.tree3.tag_configure("#ecf0f6", background="#ecf0f6")
                    self.tree3.tag_configure("white", background="white")
                    color = "white" if self.indice % 2 else "#ecf0f6"
                    id_cliente3 = row2[0]
                    
                    self.tree3.insert("",END, tag=('fuente', color), iid=id_cliente3, text = row2[0], values =(row2[2],row2[8], str(row2[9]).replace('.',','),str(row2[11]).replace('.',','),str(row2[14]).replace('.',',')))
                    self.indice= self.indice+1
                            
            except:
                self.wm_attributes("-topmost", False)
                print("ocurrio un error en mostrar_tabla_categoria")
                self.wm_attributes("-topmost", True)


        def seleccionarUsandoClick_3(self, event):
            control_bd = bd()

            item = self.tree3.identify('item', event.x, event.y)
            
            self.categoria_id_var.set(self.tree3.item(item, "text"))
            self.categoria_nombre_var.set(self.tree3.item(item, "values")[0])
            
            self.valor_equipo_var.set(self.tree3.item(item, "values")[1])
            self.equipo_vida_util_var.set(self.tree3.item(item, "values")[2])
            self.valor_residual_opcional_var.set(self.tree3.item(item, "values")[3])
            self.depreciacion_anual_var.set(self.tree3.item(item, "values")[4])
            
            print("you clicked on", self.tree3.item(item,"text"))
            self.id_c = self.tree3.item(item,"text")
            print(self.id_c)
            #self.tree.selection_set('0')

        def bindings_3(self, event):
            self.tree3.bind("<Button-1>", self.seleccionarUsandoClick_3)


        def calcular(self):
            control_bd = bd()
            self.depreciacion_lra = 0
            self.c =0

            
            print("a")
            try:
                if self.valor_equipo_var.get() == '' or self.equipo_vida_util_var.get()=='':
                    print("b")
                    self.wm_attributes("-topmost", False)
                    messagebox.showwarning("ADVERTENCIA","Debe introducir el valor del equipo y su vida util en anos")
                    self.wm_attributes("-topmost", True)
                if self.valor_equipo_var.get() != '' or self.equipo_vida_util_var.get()!='':
                    if self.valor_residual_opcional_var.get() == '' or self.valor_residual_opcional_var.get() == None:
                        self.a = float(self.valor_equipo_var.get().replace(',','.'))
                        self.b = float(self.equipo_vida_util_var.get().replace(',','.'))
                        print("c")
                        
                        self.depreciacion_lra = (self.a/self.b)
                        self.dat = self.a, self.b, self.c, self.id_c
                        control_bd.anadir_datos_depreciacion_lra(self.dat)

                    if self.valor_residual_opcional_var.get() != '': 
                        self.a = float(self.valor_equipo_var.get().replace(',','.'))
                        self.b = float(self.equipo_vida_util_var.get().replace(',','.'))
                        self.c = float(self.valor_residual_opcional_var.get().replace(',','.'))
                        print("d")  
                    
                        self.depreciacion_lra = (self.a/self.b)-self.c
                        print(self.depreciacion_lra)
                        self.dat = self.a, self.b, self.c, self.id_c
                        control_bd.anadir_datos_depreciacion_lra(self.dat)
                        print("d")
                
                print("e")
                self.datos = self.depreciacion_lra, self.id_c
                control_bd.anadir_depreciacion_lra(self.datos)
                self.mostrar_ca()
                self.wm_attributes("-topmost", False)
                messagebox.showinfo("REALIZADO","Material anadido")
                self.wm_attributes("-topmost", True)
                self.depreciacion_anual_var.set(self.depreciacion_lra)

            except:
                    self.wm_attributes("-topmost", False)
                    messagebox.showwarning("ADVERTENCIA","Ocurrió un error al anadir equipo")
                    self.wm_attributes("-topmost", True)
                    pass

        def busqueda(self):
            control_bd = bd()
            

            try:
                self.criterio1 = ''
                self.criterio = self.buscar_entry_var.get()
                print(self.criterio)
                self.criterio1 = "%s" % self.criterio +"%"
                self.datos = control_bd.busqueda_equipo_depreciacion(self.criterio1)
                print("Criterio1: ", self.criterio1)

                if self.criterio1 == '%':
                    messagebox.showwarning("ADVERTENCIA","Coloque criterio de busqueda")
                    
                elif self.criterio1 != '':
                    numeros = []
                    for row in self.datos:
                        numeros.append(row[0])
                        self.row_id = row[0]
                    self.tree3.selection
                    self.tree3.selection_set(self.tree3.tag_has(self.row_id))
                    self.tree3.selection_set(numeros) # move selection
                    self.tree3.focus(self.row_id) # move focus
                    self.tree3.see(self.row_id)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error de búsqueda")
                pass

#Ventana depreciacion por linea recta mensual

class VentanaDepreciacionLRM(tk.Toplevel):
        def __init__(self, *args, callback=None, **kwargs):
            super().__init__(*args, **kwargs)
            
            self.wm_attributes("-topmost", True)
            self.geometry("640x800")
            self.title("Tabla categorias")
            self.configure(background="#ecf0f6")

            self.frame_fondo_toplevel = tk.Frame(self)
            self.frame_fondo_toplevel.pack(expand=True)
            self.frame_fondo_toplevel.config(bg="#ecf0f6", width=900, height=400)

            #Label fondo
            self.label_a= tk.Label(self.frame_fondo_toplevel, bg="#ecf0f6", relief=tk.SUNKEN)
            self.label_a.place(x=15, y=10, width=610, height= 350)
        
            #Stringvar
            self.categoria_id_var = StringVar()   
            self.categoria_nombre_var = StringVar()
            
            self.valor_equipo_var = StringVar()
            self.equipo_vida_util_var = StringVar()
            self.valor_residual_opcional_var = StringVar()
            
            self.depreciacion_mensual_var = StringVar()


            self.buscar_entry_var = StringVar()

            #Labels
            self.agregar_categoria= tk.Label(self.frame_fondo_toplevel, text="Agregar categoria", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=20, y=1)

            self.id_equipo = tk.Label(self.frame_fondo_toplevel, text="ID Equipo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=20, y=60)  
            self.equipo = tk.Label(self.frame_fondo_toplevel, text="Equipo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=300, y=60)
            self.valor_equipo = tk.Label(self.frame_fondo_toplevel, text="Valor Equipo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=20, y=100)  
            self.equipo_vida_util= tk.Label(self.frame_fondo_toplevel, text="Equipo Vida Util (meses):", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=20, y=140)
            self.valor_residual_opcional = tk.Label(self.frame_fondo_toplevel, text="Valor Residual :", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=20, y=180)
            self.valor_residual_opcional = tk.Label(self.frame_fondo_toplevel, text="(Puede ser igual a cero)", font=("Arial",8), bg="#ecf0f6", fg="#303452" ).place(x=20, y=200)
            self.depreciacion_anual = tk.Label(self.frame_fondo_toplevel, text="Depreciacion mensual:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=20, y=260)

            self.id_equipo_ver = tk.Label(self.frame_fondo_toplevel, textvariable=self.categoria_id_var, relief=tk.SUNKEN, font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=130, y=60, width=150)
            self.equipo_ver = tk.Label(self.frame_fondo_toplevel, textvariable=self.categoria_nombre_var, relief=tk.SUNKEN, font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=390, y=60, width=220)
            self.depreciacion_ver = tk.Label(self.frame_fondo_toplevel, textvariable=self.depreciacion_mensual_var, relief=tk.SUNKEN, font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=300, y=260, width=220)


            #Entry
            self.buscar_entry_ca = tk.Entry(self.frame_fondo_toplevel, textvariable= self.buscar_entry_var).place(x=20, y=30, width=250)
            
            self.valor_equipo_entry = tk.Entry(self.frame_fondo_toplevel, textvariable= self.valor_equipo_var).place(x=280, y=100, width=250)
            self.equipo_vida_util_entry= tk.Entry(self.frame_fondo_toplevel, textvariable= self.equipo_vida_util_var).place(x=280, y=140, width=250)

            self.valor_residual_opcional_entry= tk.Entry(self.frame_fondo_toplevel, textvariable= self.valor_residual_opcional_var).place(x=280, y=180, width=250)

            #Buttom
            self.buscar_ca = tk.Button(self.frame_fondo_toplevel, text="Buscar", command= self.busqueda , bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=280, y=26) 

            self.calcular_boton = tk.Button(self.frame_fondo_toplevel, text="Calcular", command= self.calcular, bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 250, y = 220)
            
            # Frame del treeview
            self.frame_treeview4 = tk.Frame(self)
            self.frame_treeview4.pack(fill=tk.Y, side=tk.BOTTOM)
            self.frame_treeview4.config(bg="white", width=20, height=30)

            style2 = ttk.Style()
            style2.configure("mystyle.Treeview",
                background = "red",
                foreground = "#303452",
                rowheight = 30,
                fieldbackground = "white"
                )

                    # Set the treeview
            self.tree4 = ttk.Treeview(self.frame_treeview4, style="mystyle.Treeview", height=12)

            self.treexscroll4 = tk.Scrollbar(self.frame_treeview4, orient=tk.HORIZONTAL)
            self.treexscroll4.pack(fill=tk.X, side=tk.BOTTOM)
            # configurar scrollbar
            self.treexscroll4.config(command=self.tree4.xview)

            self.treeyscroll4 = tk.Scrollbar(self.frame_treeview4, orient=tk.VERTICAL)
            self.treeyscroll4.pack(fill=tk.Y, side=tk.RIGHT)
            # configurar scrollbar
            self.treeyscroll4.config(command=self.tree4.yview)

            # TREEVIEW
            self.tree4.config(xscrollcommand=self.treexscroll4.set, yscrollcommand=self.treeyscroll4.set, 
            columns=(
                    "col1", "col2", "col3", "col4", "col5"))

        
            self.tree4.column("#0", width=150, stretch= False)
            self.tree4.column("col1", width=150, stretch= False)
            self.tree4.column("col2", width=150, stretch= False)
            self.tree4.column("col3", width=190, stretch= False)
            self.tree4.column("col4", width=150, stretch= False)
            self.tree4.column("col5", width=250, stretch= False)
            
            
            self.tree4.heading("#0", text="ID equipo", anchor=tk.CENTER)
            self.tree4.heading("col1", text="equipo", anchor=tk.CENTER)
            self.tree4.heading("col2", text="Valor del activo", anchor=tk.CENTER)
            self.tree4.heading("col3", text="Vida util activo meses", anchor=tk.CENTER)
            self.tree4.heading("col4", text="Valor residual", anchor=tk.CENTER)
            self.tree4.heading("col5", text="Depreciacion linea recta mensual", anchor=tk.CENTER)
            
            
            self.tree4.pack()
            self.treeview4 = self.tree4
            
            self.id = 0
            self.iid = 0

            self.tree4.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick_4)
            self.tree4.bind('<<TreeviewSelect>>', self.bindings_4)

            self.mostrar_ca()

            

        def mostrar_ca(self): #Actualizar treeview luego de modificar
            
            control_bd = bd()
            datos_apt4 = control_bd.mostrar_equipo()
            
            registros4 = self.tree4.get_children()
            for elemento4 in registros4:
                self.tree4.delete(elemento4)
            try:
                self.indice= 1
                for row4 in datos_apt4:		
                    self.tree4.tag_configure("#ecf0f6", background="#ecf0f6")
                    self.tree4.tag_configure("white", background="white")
                    color = "white" if self.indice % 2 else "#ecf0f6"
                    id_cliente4 = row4[0]
                    
                    self.tree4.insert("",END, tag=('fuente', color), iid=id_cliente4, text = row4[0], values =( str(row4[2]).replace('.',','), str(row4[8]).replace('.',','), str(row4[10]).replace('.',','),str(row4[11]).replace('.',','),str(row4[15]).replace('.',',')))
                    self.indice= self.indice+1
                            
            except:
                self.wm_attributes("-topmost", False)
                print("ocurrio un error en mostrar_tabla_categoria")
                self.wm_attributes("-topmost", True)


        def seleccionarUsandoClick_4(self, event):
            control_bd = bd()

            item = self.tree4.identify('item', event.x, event.y)
            
            self.categoria_id_var.set(self.tree4.item(item, "text"))
            self.categoria_nombre_var.set(self.tree4.item(item, "values")[0])
            
            self.valor_equipo_var.set(str(self.tree4.item(item, "values")[1]).replace('.',','))
            self.equipo_vida_util_var.set(str(self.tree4.item(item, "values")[2]).replace('.',','))
            self.valor_residual_opcional_var.set(str(self.tree4.item(item, "values")[3]).replace('.',','))
            self.depreciacion_mensual_var.set(str(self.tree4.item(item, "values")[4]).replace('.',','))
            
            print("you clicked on", self.tree4.item(item,"text"))
            self.id_c = self.tree4.item(item,"text")
            print(self.id_c)
            #self.tree.selection_set('0')

        def bindings_4(self, event):
            self.tree4.bind("<Button-1>", self.seleccionarUsandoClick_4)


        def calcular(self):
            control_bd = bd()
            self.depreciacion_lrm = 0
            self.c =0

            
            print("a")
            try:
                if self.valor_equipo_var.get() == '' or self.equipo_vida_util_var.get()=='':
                    print("b")
                    self.wm_attributes("-topmost", False)
                    messagebox.showwarning("ADVERTENCIA","Debe introducir el valor del equipo y su vida util en meses")
                    self.wm_attributes("-topmost", True)
                if self.valor_equipo_var.get() != '' or self.equipo_vida_util_var.get()!='':
                    if self.valor_residual_opcional_var.get() == '' or self.valor_residual_opcional_var.get() == None:
                        self.a = float(self.valor_equipo_var.get().replace(',','.'))
                        self.a_r = round(self.a, 2)
                        self.b = float(self.equipo_vida_util_var.get().replace(',','.'))
                        self.b_r = round(self.b, 2)
                        print("c")
                        
                        self.depreciacion_lrm = (self.a/self.b)
                        self.depreciacion_lrm = round(self.depreciacion_lrm, 2)
                        self.dat = self.a, self.b, self.c, self.id_c
                        control_bd.anadir_datos_depreciacion_lrm(self.dat)

                    if self.valor_residual_opcional_var.get() != '': 
                        self.a = float(self.valor_equipo_var.get().replace(',','.'))
                        self.a_r = round(self.a, 2)
                        self.b = float(self.equipo_vida_util_var.get().replace(',','.'))
                        self.b_r = round(self.b, 2)
                        self.c = float(self.valor_residual_opcional_var.get().replace(',','.'))
                        self.c_r = round(self.c, 2)
                        print("d")  
                    
                        self.depreciacion_lrm = (self.a/self.b)-self.c
                        print(self.depreciacion_lrm)
                        self.depreciacion_lrm = round(self.depreciacion_lrm, 2)
                        self.dat = self.depreciacion_lrm, self.id_c
                        control_bd.anadir_depreciacion_lrm(self.dat)
                        print("d")
                
                print("e")
                self.datos = self.depreciacion_lrm, self.id_c
                control_bd.anadir_depreciacion_lra(self.datos)
                self.mostrar_ca()
                self.wm_attributes("-topmost", False)
                messagebox.showinfo("REALIZADO","Material anadido")
                self.wm_attributes("-topmost", True)
                self.depreciacion_mensual_var.set(str(self.depreciacion_lrm).replace('.',','))

            except:
                    self.wm_attributes("-topmost", False)
                    messagebox.showwarning("ADVERTENCIA","Ocurrió un error al anadir equipo")
                    self.wm_attributes("-topmost", True)
                    pass

        def busqueda(self):
            control_bd = bd()
            

            try:
                self.criterio1 = ''
                self.criterio = self.buscar_entry_var.get()
                print(self.criterio)
                self.criterio1 = "%s" % self.criterio +"%"
                self.datos = control_bd.busqueda_equipo_depreciacion(self.criterio1)
                print("Criterio1: ", self.criterio1)

                if self.criterio1 == '%':
                    messagebox.showwarning("ADVERTENCIA","Coloque criterio de busqueda")
                    
                elif self.criterio1 != '':
                    numeros = []
                    for row in self.datos:
                        numeros.append(row[0])
                        self.row_id = row[0]
                    self.tree4.selection
                    self.tree4.selection_set(self.tree4.tag_has(self.row_id))
                    self.tree4.selection_set(numeros) # move selection
                    self.tree4.focus(self.row_id) # move focus
                    self.tree4.see(self.row_id)
            except:
                messagebox.showwarning("ADVERTENCIA","Ocurrió un error de búsqueda")
                pass