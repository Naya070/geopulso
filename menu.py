from re import X
import tkinter as tk
from tkinter import BOTH, BOTTOM, DISABLED, END, LEFT, RIGHT, TOP, Y, X, StringVar, ttk
from tkinter import messagebox
from turtle import bgcolor, heading, left, right, width
from tkinter import ttk
from webbrowser import get
from PIL import ImageTk, Image


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

        def salir():
            self.master.destroy()
            self.master.quit()
            
        """def entrada_clientes():
            controller.show_frame(Clase_clientes) # Entrar a la ventana principal
            controller.protocol("WM_DELETE_WINDOW", salir)"""
			

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
            
        self.button_material= tk.Button(self.frame_fondo, text="Material", width=20, height=2, bg='#303452', fg='white', font=("Cambria", 12, "bold")).pack()
        self.label_espacio = tk.Label(self.frame_fondo, text="\n", bg='#ecf0f6').pack()

        self.button_equipo = tk.Button(self.frame_fondo, text="Equipo", width=20, height=2, bg='#303452', fg='white', font=("Cambria", 12, "bold")).pack()
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
        self.button_material = tk.Button(self, text="Material", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 340, y = 0) 
        self.button_equipo = tk.Button(self, text="Equipo", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20,height=1).place(x=510, y=0)
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
        
        def salir():
            self.master.destroy()
            self.master.quit()
        

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
        self.button_material = tk.Button(self, text="Material", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 340, y = 0) 
        self.button_equipo = tk.Button(self, text="Equipo", command = lambda:controller.show_frame(mientras),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=510, y=0)
        self.button_empleados = tk.Button(self, text="Clientes", command = lambda:controller.show_frame(Clase_clientes), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20,height=1).place(x=680, y=0)
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
        #self.direccion_empresa = tk.Label(self, text="Direccion de la empresa:", font=("Arial"), bg="#ecf0f6" ).place(x=370, y=220)
            
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
        self.button_proveedores = tk.Button(self, text="Clientes", command = lambda:controller.show_frame(Clase_clientes), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 170, y = 0)     
        self.button_material = tk.Button(self, text="Material", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 340, y = 0) 
        self.button_equipo = tk.Button(self, text="Equipo", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20,height=1).place(x=510, y=0)
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
        #self.comentarios_var = StringVar()
            

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

class Clase_material(tk.Frame): 
    
    def __init__(self, parent, controller):
		
        tk.Frame.__init__(self, parent) 
        control_bd = bd()
        
        print("CLASE_MATERIAL") 


        def mientras():
            pass
        
        def salir():
            self.master.destroy()
            self.master.quit()
        

        self.config(bg="#ecf0f6", width=2440, height=300)

        self.frame_fondo = tk.Frame(self)
        self.frame_fondo.pack(expand=True)
        self.frame_fondo.config(bg="blue", width=1440, height=500)
            

        #self.fondo = ImageTk.PhotoImage(Image.open("img/fondo_azul.jpg"))
        
        self.frame_0 = tk.Frame(self.frame_fondo)
        self.frame_0.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.frame_0.config(bg="salmon", width=500, height=100)
        
        #self.frame_1 = tk.Frame(self.frame_fondo)
        #self.frame_1.pack( side=tk.LEFT, expand=True)
        #self.frame_1.config(bg="green", width=50, height=70)

        self.frame_2 = tk.Frame(self.frame_fondo)
        self.frame_2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        self.frame_2.config(bg="yellow", width=400, height=700)

        #self.frame_3 = tk.Frame(self.frame_1)
        #self.frame_3.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        #self.frame_3.config(bg="white", width=20, height=20)

        """self.label_a= tk.Label(self.frame_1, bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_a.place(x=10, y=90, width=350, height= 300)

        self.label_b= tk.Label(self.frame_1, bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_b.place(x=365,y=90, width=290, height= 300)

        self.label_c= tk.Label(self.frame_1, bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_c.place(x=660,y=90, width=355, height= 300)"""

                #Buttons
        self.button_proyectos = tk.Button(self, text="Proyectos", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20, height=1 ).place(x = 0, y = 0)      
        self.button_proveedores = tk.Button(self, text="Clientes", command = lambda:controller.show_frame(Clase_clientes), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 170, y = 0)     
        self.button_material = tk.Button(self, text="Proveedores", command = lambda:controller.show_frame(Clase_proveedores), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20, height=1).place(x = 340, y = 0) 
        self.button_equipo = tk.Button(self, text="Equipo", command = lambda:controller.show_frame(mientras), bg='#72729a', fg='white', font=("Arial",10,"bold"),width=20,height=1).place(x=510, y=0)
        self.button_empleados = tk.Button(self, text="Empleados", command = lambda:controller.show_frame(Clase_empleados),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=680, y=0)
        self.button_menu = tk.Button(self, text="Menu", command = lambda:controller.show_frame(Clase_menu),bg='#72729a', fg='white', font=("Arial",10,"bold"), width=20,height=1).place(x=850, y=0)

        self.anadir = tk.Button(self, text="Añadir proveedor",  bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 680, y = 590) 
        self.actualizar_b = tk.Button(self, text="Actualizar", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 865, y = 590)
        self.eliminar = tk.Button(self, text="Eliminar proveedor", bg='#72729a', fg='white', font=("Arial",10,"bold"),width=15, height=2).place(x = 680, y = 650) 
        self.limpiar = tk.Button(self, text="Limpiar campos", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 865, y = 650)  
        
        self.anadir_ca= tk.Button(self, text="Agregar",  bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 15, y = 250) 
        self.actualizar_ca = tk.Button(self, text="Actualizar", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 170, y = 250)
        self.eliminar_ca = tk.Button(self, text="Borrar", bg='#72729a', fg='white', font=("Arial",10,"bold"),width=15, height=2).place(x = 325, y = 250) 
        self.limpiar_ca = tk.Button(self, text="Limpiar campos", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=2).place(x = 480, y = 250)  

        self.buscar = tk.Button(self, text="Buscar", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=920, y=140) 

        self.buscar_ca = tk.Button(self, text="Buscar", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=530, y=140) 


                #Labels
        self.agregar_categoria= tk.Label(self, text="Agregar categoria", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=15, y=80)   
        self.gestion_producto= tk.Label(self, text="Gestion de producto", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=650, y=80) 
            
        self.categoria_id = tk.Label(self, text="ID de la Categoria:", font=("Arial"), bg="#f6fbff", fg="#303452" ).place(x=13, y=145)  
        self.categoria_nombre = tk.Label(self, text="Nombre de la categoria:", font=("Arial"), bg="#f6fbff", fg="#303452" ).place(x=13, y=195)
        
        
        
        self.id_producto = tk.Label(self, text="ID producto:", font=("Arial"), bg="#f6fbff", fg="#303452" ).place(x=640, y=190)
        self.telefono = tk.Label(self, text="Categoria:", font=("Arial"), bg="#f5fafe", fg="#303452" ).place(x=640, y=230)
        self.telefono = tk.Label(self, text="Producto:", font=("Arial"), bg="#f5fafe", fg="#303452" ).place(x=640, y=270)
        #self.correo= tk.Label(self, text="Telefono:", font=("Arial"), bg="#f3fbfe", fg="#303452" ).place(x=13, y=320) 

        #self.direccion_vivienda = tk.Label(self, text="Correo:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=120)
        #self.empresa = tk.Label(self, text="RIF:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=170)
        #self.direccion_empresa = tk.Label(self, text="Sitio web:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=220)
            
        #self.comentarios= tk.Label(self, text="Comentarios:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=370, y=270)
            
                #Entry
            
            
            
        self.nombre_empresa_var = StringVar()
        self.producto_servicio_var = StringVar()
        self.nombre_contacto_var = StringVar()
        self.cargo_contacto_var = StringVar()
        self.telefono_var = StringVar()
        self.correo_var = StringVar()
        self.rif_var = StringVar()
        self.sitio_web_var = StringVar()
        #self.comentarios_var = StringVar()
            

        self.buscar_entry_var = StringVar()
            



            
        self.categoria_id_entry = tk.Entry(self, textvariable= self.nombre_empresa_var).place(x=270, y=145, width=250)
        self.categoria_nombre_entry= tk.Entry(self, textvariable= self.producto_servicio_var).place(x=270, y=195, width=250)
        #self.nombre_contacto_entry = tk.Entry(self, textvariable= self.cargo_contacto_var).place(x=15, y=245, width=250)
        #self.cargo_contacto_entry = tk.Entry(self, textvariable= self.telefono_var).place(x=15, y=295, width=250)
        #self.telefono_entry = tk.Entry(self, textvariable= self.telefono_var).place(x=15, y=345, width=250)

        #self.correo_entry= tk.Entry(self, textvariable= self.correo_var).place(x=370, y=145, width=250)
        #self.rif_entry = tk.Entry(self, textvariable= self.rif_var).place(x=370, y=195, width=250)
        #self.sitio_web_entry = tk.Entry(self, textvariable= self.sitio_web_var).place(x=370, y=245, width=250)

        #Comentarios
        #self.textBox=tk.Text(self, height=6, width=35) 
        #self.textBox.place(x=370, y=295)
        #self.textBox.get('1.0','end')
            
            
            
        self.buscar = tk.Label(self, text="Buscar", font=("Arial"),
                                bg="#f9fdff", fg="#303452", width=6, height=1).place(x=640, y=120)

        self.buscar_entry = tk.Entry(self, textvariable= self.buscar_entry_var).place(x=640, y=145, width=250)

            # Frame del treeview
        self.frame_treeview = tk.Frame(self.frame_fondo)
        self.frame_treeview.pack(fill=tk.Y, side=tk.BOTTOM)
        self.frame_treeview.config(bg="white", width=20, height=30)

        style = ttk.Style()
        style.configure("mystyle.Treeview",
            background = "red",
            foreground = "#303452",
            rowheight = 30,
            fieldbackground = "white"
        )

                    # Set the treeview
        self.tree = ttk.Treeview(self.frame_treeview, style="mystyle.Treeview", height=12)

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

        #self.mostrar()
            
            
        #self.tree.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick)
        #self.tree.bind('<<TreeviewSelect>>', self.bindings)




    