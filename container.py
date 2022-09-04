from operator import and_
from pickle import TRUE
import tkinter as tk
#import tkSimpleDialog
#import tkMessageBox
from tkinter import BOTH, DISABLED, END, RIGHT, Y, StringVar, ttk, Radiobutton
from tkinter import messagebox
from turtle import heading, width
from tkinter import ttk
import tkinter.font as font
from PIL import ImageTk, Image
import sqlite3

from datetime import datetime
from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
from openpyxl.styles import Font, Border, Side, Alignment
from fpdf import FPDF

#from clientes import Clase_clientes
from menu import Login1, Clase_menu, Clase_clientes, Clase_empleados, Clase_proveedores, Clase_material




LargeFont = ("Verdana", 12)

def options():
     '''\n**************************************************************
          Welcome to the GUI interface of the python program
**************************************************************'''


class PageContainer(tk.Tk):  

	def __init__(self, *args, **kwargs):  
		options()
		tk.Tk.__init__(self, *args, **kwargs) 

		container = tk.Frame(self)  
		tk.Tk.geometry(self,'1440x900')  #Tamano de la ventana
		container.pack(side='top', fill='both', expand = True )     
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frame = {}

		for F in (Login1, Clase_menu, Clase_clientes, Clase_empleados, Clase_proveedores, Clase_material):

			frame = F(container, self)

			self.frame[F] = frame

			frame.grid(row = 0, column = 0, sticky = "nsew") 

		self.show_frame(Clase_material)

	def show_frame(self, cont):

		frame = self.frame[cont]    
		frame.tkraise()    


