"""self.ventana_nueva1 = tk.Toplevel()
        self.ventana_nueva1.geometry("700x700")
        self.ventana_nueva1.title("Tabla categorias")
        self.ventana_nueva1.configure(background="#ecf0f6")

        self.frame_fondo_toplevel = tk.Frame(self.ventana_nueva1)
        self.frame_fondo_toplevel.pack(expand=True)
        self.frame_fondo_toplevel.config(bg="#ecf0f6", width=900, height=300)
        
        #Label fondo
        self.label_a= tk.Label(self.frame_fondo_toplevel, bg="#ecf0f6", relief=tk.SUNKEN)
        self.label_a.place(x=10, y=90, width=610, height= 225)
        
        #Stringvar
        self.categoria_id_var = StringVar()   
        self.categoria_nombre_var = StringVar() 

        #Labels
        self.agregar_categoria= tk.Label(self.frame_fondo_toplevel, text="Agregar categoria", font=("Arial"), bg="#ecf0f6", fg='#72729a' ).place(x=15, y=80)

        self.categoria_id = tk.Label(self.frame_fondo_toplevel, text="ID de la Categoria:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=150)  
        self.categoria_nombre = tk.Label(self.frame_fondo_toplevel, text="Nombre de la categoria:", font=("Arial"), bg="#ecf0f6", fg="#303452" ).place(x=13, y=190)
        
        #Entry
        self.buscar_entry_ca = tk.Entry(self.frame_fondo_toplevel, textvariable= self.buscar_entry_pro_var).place(x=15, y=120, width=250)
        self.categoria_id_entry = tk.Entry(self.frame_fondo_toplevel, textvariable= self.categoria_id_var).place(x=260, y=150, width=250)
        self.categoria_nombre_entry= tk.Entry(self.frame_fondo_toplevel, textvariable= self.categoria_nombre_var).place(x=260, y=190, width=250)

        #Buttom
        self.buscar_ca = tk.Button(self.frame_fondo_toplevel, text="Buscar", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=8, height=1).place(x=280, y=115) 

        self.anadir_ca= tk.Button(self.frame_fondo_toplevel, text="Agregar",  bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 15, y = 240) 
        self.actualizar_ca = tk.Button(self.frame_fondo_toplevel, text="Actualizar", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 160, y = 240)
        self.eliminar_ca = tk.Button(self.frame_fondo_toplevel, text="Borrar", bg='#72729a', fg='white', font=("Arial",10,"bold"),width=15, height=1).place(x = 310, y = 240) 
        self.limpiar_ca = tk.Button(self.frame_fondo_toplevel, text="Limpiar campos", bg='#72729a', fg='white', font=("Arial",10,"bold"), width=15, height=1).place(x = 460, y = 240) 

        # Frame del treeview
        self.frame_treeview2 = tk.Frame(self.ventana_nueva1)
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

        self.tree.bind('<<TreeviewSelect>>', self.seleccionarUsandoClick_ca)
        self.tree.bind('<<TreeviewSelect>>', self.bindings_ca)

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
            print("ocurrio un error en mostrar_tabla_categoria")"""