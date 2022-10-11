import tkinter as tk
from menu import Login1, Clase_menu, Clase_clientes, Clase_empleados, Clase_proveedores, Clase_material, Clase_equipo

LargeFont = ("Verdana", 12)

class PageContainer(tk.Tk):  

	def __init__(self, *args, **kwargs):  
		tk.Tk.__init__(self, *args, **kwargs) 

		container = tk.Frame(self)  
		tk.Tk.geometry(self,'1440x900')  #Tamano de la ventana
		container.pack(side='top', fill='both', expand = True )     
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frame = {}

		for F in (Login1, Clase_menu, Clase_clientes, Clase_empleados,
		Clase_proveedores, Clase_material, Clase_equipo):

			frame = F(container, self)

			self.frame[F] = frame

			frame.grid(row = 0, column = 0, sticky = "nsew") 

		self.show_frame(Login1)

	def show_frame(self, cont):

		frame = self.frame[cont]    
		frame.tkraise()    


