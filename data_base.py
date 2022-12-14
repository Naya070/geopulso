import mysql.connector


class bd:

    def __init__(self):
        
        try:
            self.connection = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'tupropiarana',
                db = 'geopulso'
            )
            
        except Exception as ex:
            print(ex)


    #Funciones de login_inicio

    def buscar_usuario(self, entry_usuario_var):
        s=0
        id_del_usuario=0
        cursor = self.connection.cursor()
        cursor.execute("SELECT id_acceso FROM geopulso.acceso WHERE usuario='%s'" % (entry_usuario_var))
        #Busca si el usuario escrito existe en base de datos y de existir devuelve su id
        #Si el usuario no existe devuelve 0
        self.rows = cursor.fetchall()
        for self.row in self.rows: 
            if self.row[0]:
                id_del_usuario= self.row[0] #id del usuario
                print("buscar_usuario.id_del_usuario:", id_del_usuario)
            else:
                id_del_usuario= 0
        
        return id_del_usuario

    def comprobar_usuario(self, id_del_usuario):
        cursor= self.connection.cursor()
        cursor.execute("SELECT usuario, password FROM geopulso.acceso WHERE id_acceso= '%s'" % (id_del_usuario))
        #Busca usuario y password segun el id del usuario existente
        usuario_contrasenna = cursor.fetchall()
        return usuario_contrasenna

    def colocar_id_usuariologin(self, id_usuario):
        cursor= self.connection.cursor()
        cursor.execute("UPDATE geopulso.datos_extra SET id_usuario_acceso = '%s' WHERE datos_extra_id = 1" % (id_usuario))
        # Sobreescribir id del usuario que acaba de hacer Login
        self.connection.commit()
        #cursor.execute("SELECT id_usuario_acceso FROM geopulso.datos_extra WHERE datos_extra_id=1")
        #Tomar id del usuario que acaba de hacer Login
        #fi = cursor.fetchall()
        #print("Aqui estas")
        #return fi

    def colocar_usuario_escrito(self, usuario):
        cursor= self.connection.cursor()
        cursor.execute("UPDATE geopulso.datos_extra SET usuario_escrito = '%s' WHERE datos_extra_id =1" % (usuario))
        #Subir a la base de datos el nombre ingresado del usuario escrito al hacer login
        self.connection.commit()

    def seleccion_usuario(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT usuario_escrito FROM geopulso.datos_extra WHERE datos_extra_id=1")
        #Seleccionar nombre de usuario del usuario que hizo login
        self.id_usuario = cursor.fetchall()
        for self.row in self.id_usuario:
            id_usuarioLogin = self.row[0]
        return id_usuarioLogin

    def obtener_log(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT pass_acceso FROM geopulso.datos_extra WHERE datos_extra_id =1")
        rows = cursor.fetchall()
        return rows

    def crear_nuevo_usuario(self, nombres, apellidos, nombre_usuario, correo, clave):
        cursor= self.connection.cursor()
        cursor.execute("INSERT INTO geopulso.acceso VALUES (NULL,'%s','%s','%s','%s','%s')" % (nombres, apellidos, nombre_usuario, correo, clave))
        self.connection.commit()
	
    
    #Funciones de menu

    def seleccion_id(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT id_usuario_acceso FROM geopulso.datos_extra WHERE datos_extra_id=1")
        #Seleccionar id del usuario que hizo login
        id_usuario = cursor.fetchall()
        for self.row in id_usuario:
            id_usuarioLogin= self.row[0]

        return id_usuarioLogin

    def tomar_datos_usuario(self, id_usuario):
        cursor= self.connection.cursor()
        cursor.execute("SELECT nombres, apellidos, usuario FROM geopulso.acceso WHERE id_acceso='%s'" % (id_usuario))
        #Tomar los datos del usuario que hizo Login a partir de su id
        datos_usuario_login = cursor.fetchall()
        for nom_apell_us in datos_usuario_login:
            pass
        
        return nom_apell_us


        # FUNCIONES CLIENTES

    def mostrar_clientes(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT * FROM clientes")
        datos_apt = cursor.fetchall()
        return datos_apt

    def busqueda_clientes(self, criterio1):
        cursor= self.connection.cursor()
        cursor.execute("SELECT id_clientes FROM geopulso.clientes WHERE nombres LIKE '%s' OR apellidos LIKE '%s'" % (criterio1, criterio1))
        self.datos = cursor.fetchall()
        return self.datos

    def anadir_cli_bd(self, datos):
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO `geopulso`.`clientes` (`nombres`, `apellidos`,
                `cedula`, `telefono`, `correo`, `direccion_vivienda`, `empresa`, `direccion_empresa`, `comentarios`) 
                VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""  % (datos) )
        self.connection.commit()

    def actualizar_cliente(self, datos_actualizar):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`clientes` SET `nombres` = '%s', `apellidos`='%s', `cedula`='%s', `telefono`='%s', `correo`='%s', `direccion_vivienda`='%s', `empresa`='%s', `direccion_empresa`='%s', `comentarios`='%s'  WHERE (`id_clientes` = '%s')" % (datos_actualizar))
        self.connection.commit()

    def borrar_cliente(self, id_c):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM `geopulso`.`clientes` WHERE (`id_clientes` = '%s')" % (id_c))
        self.connection.commit()






# FUNCIONES EMPLEADOS

    def mostrar_empleados(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT * FROM empleados")
        datos_apt = cursor.fetchall()
        return datos_apt

    def busqueda_empleados(self, criterio1):
        cursor= self.connection.cursor()
        cursor.execute("SELECT id_empleados FROM geopulso.empleados WHERE nombres LIKE '%s' OR apellidos LIKE '%s'" % (criterio1, criterio1))
        self.datos = cursor.fetchall()
        return self.datos

    def anadir_empl_bd(self, datos):
        print(datos)
        cursor = self.connection.cursor()
        print(1)
        #cursor.execute("INSERT INTO `geopulso`.`empleados` (`id_empleados`, `nombres`, `apellidos`, `cargo`, `cedula`, `telefono`, `correo`, `direccion`, `comentarios`) VALUES ('2', 'Maribel', 'Landaeta', 'Secretaria', '10243556', '04164552298', 'landaMar@gmail.com', 'En su casa', 'Hola')")
        
        cursor.execute("INSERT INTO `geopulso`.`empleados` (`nombres`, `apellidos`, `cargo`, `cedula`, `telefono`, `correo`, `direccion`, `comentarios`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (datos) )
        print(2)
        self.connection.commit()
        print(3)

    def actualizar_empleados(self, datos_actualizar):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`empleados` SET `nombres` = '%s', `apellidos`='%s', `cargo`='%s', `cedula`='%s', `telefono`='%s', `correo`='%s', `direccion`='%s', `comentarios`='%s'  WHERE (`id_empleados` = '%s')" % (datos_actualizar))
        self.connection.commit()

    def borrar_empleados(self, id_c):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM `geopulso`.`empleados` WHERE (`id_empleados` = '%s')" % (id_c))
        self.connection.commit()



# FUNCIONES PROVEEDORES

    def mostrar_proveedores(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT * FROM proveedores")
        datos_apt = cursor.fetchall()
        return datos_apt

    def busqueda_proveedores(self, criterio1):
        cursor= self.connection.cursor()
        cursor.execute("SELECT id_proveedores FROM geopulso.proveedores WHERE nombre_empresa LIKE '%s' OR nombre_contacto LIKE '%s'" % (criterio1, criterio1))
        self.datos = cursor.fetchall()
        return self.datos

    def anadir_pro_bd(self, datos):
        print(datos)
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO geopulso.proveedores (`nombre_empresa`, `producto_servicio`, `nombre_contacto`, `cargo_contacto`, `telefono`, `correo`, `rif`, `sitio_web`, `comentarios`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (datos) )
        self.connection.commit()

    def actualizar_proveedores(self, datos_actualizar):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`proveedores` SET `nombre_empresa` = '%s', `producto_servicio`='%s', `nombre_contacto`='%s', `cargo_contacto`='%s', `telefono`='%s', `correo`='%s', `rif`='%s', `sitio_web`='%s', `comentarios`='%s'  WHERE (`id_proveedores` = '%s')" % (datos_actualizar))
        self.connection.commit()

    def borrar_proveedores(self, id_c):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM geopulso.proveedores WHERE (`id_proveedores` = '%s')" % (id_c))
        self.connection.commit()





# FUNCIONES MATERIAL


    #GESTION DE PRODUCTOS FUNCIONES
    def mostrar_proveedores_para_material(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT `id_proveedores`, `nombre_empresa` FROM proveedores")
        datos_apt = cursor.fetchall()
        return datos_apt

    def mostrar_categoria_material(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT * FROM geopulso.categoria_material")
        datos_apt = cursor.fetchall()
        return datos_apt

    def mostrar_categoria_material_segun_Id(self, id_c):
        cursor= self.connection.cursor()
        cursor.execute("SELECT * FROM geopulso.categoria_material WHERE (`id_categoria_material` = '%s')" % (id_c))
        datos_apt = cursor.fetchall()
        return datos_apt
    
    def mostrar_material(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT * FROM geopulso.material")
        datos_apt = cursor.fetchall()
        return datos_apt

    def busqueda_material(self, criterio1):
        cursor= self.connection.cursor()
        cursor.execute("SELECT id_material FROM geopulso.material WHERE producto LIKE '%s' OR descripcion LIKE '%s'" % (criterio1, criterio1))
        self.datos = cursor.fetchall()
        return self.datos

    def busqueda_material_ca(self, criterio1):
        cursor= self.connection.cursor()
        cursor.execute("SELECT id_categoria_material FROM geopulso.categoria_material WHERE categoria_material_nombre LIKE '%s'" % (criterio1))
        self.datos = cursor.fetchall()
        return self.datos

    def anadir_mat_bd(self, datos):
        print(datos)
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO `geopulso`.`material` (`id_material`, `categoria`, `producto`, `descripcion`, `marca`, `modelo`, `proveedor_id`, `cantidad`, `precio`, `ultima_entrada`, `comentarios`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (datos) )
        self.connection.commit()

    def anadir_mat_ca_bd(self, datos):
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO `geopulso`.`categoria_material` (`id_categoria_material`, `categoria_material_nombre`) VALUES ('%s', '%s')""" % (datos) )
        self.connection.commit()

    def actualizar_material(self, datos_actualizar):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`material` SET `id_material` = '%s', `categoria`='%s', `producto`='%s', `descripcion`='%s', `marca`='%s', `modelo`='%s', `proveedor_id`='%s', `cantidad`='%s', `precio`='%s', `ultima_entrada`='%s', `comentarios`='%s'  WHERE (`id_material` = '%s')" % (datos_actualizar))
        self.connection.commit()

    def actualizar_material_ca(self, datos_actualizar):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`categoria_material` SET `id_categoria_material` = '%s', `categoria_material_nombre`='%s' WHERE (`id_categoria_material` = '%s')" % (datos_actualizar))
        self.connection.commit()

    def borrar_material(self, id_c):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM geopulso.material WHERE (`id_material` = '%s')" % (id_c))
        self.connection.commit()

    def borrar_material_ca(self, id_c):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM geopulso.categoria_material WHERE (`id_categoria_material` = '%s')" % (id_c))
        self.connection.commit()



    

    # FUNCIONES EQUIPO


    #GESTION DE EQUIPO FUNCIONES
    def mostrar_proveedores_para_equipo(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT `id_proveedores`, `nombre_empresa` FROM proveedores")
        datos_apt = cursor.fetchall()
        return datos_apt

    def mostrar_categoria_equipo(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT * FROM geopulso.categoria_equipo")
        datos_apt = cursor.fetchall()
        return datos_apt

    def mostrar_categoria_equipo_segun_Id(self, id_c):
        cursor= self.connection.cursor()
        cursor.execute("SELECT * FROM geopulso.categoria_equipo WHERE (`id_categoria_equipo` = '%s')" % (id_c))
        datos_apt = cursor.fetchall()
        return datos_apt
    
    def mostrar_equipo(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT * FROM geopulso.equipo")
        datos_apt = cursor.fetchall()
        return datos_apt

    def busqueda_equipo(self, criterio1):
        cursor= self.connection.cursor()
        cursor.execute("SELECT id_equipo FROM geopulso.equipo WHERE equipo LIKE '%s' OR descripcion LIKE '%s'" % (criterio1, criterio1))
        self.datos = cursor.fetchall()
        return self.datos

    def busqueda_equipo_ca(self, criterio1):
        cursor= self.connection.cursor()
        cursor.execute("SELECT id_categoria_equipo FROM geopulso.categoria_equipo WHERE categoria_equipo_nombre LIKE '%s'" % (criterio1))
        self.datos = cursor.fetchall()
        return self.datos

    def anadir_eq_bd(self, datos):
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO `geopulso`.`equipo` (`id_equipo`, `categoria`, `equipo`, `descripcion`, `marca`, `modelo`, `proveedor_id`, `comentarios`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (datos) )
        self.connection.commit()

    def anadir_eq_ca_bd(self, datos):
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO `geopulso`.`categoria_equipo` (`id_categoria_equipo`, `categoria_equipo_nombre`) VALUES ('%s', '%s')""" % (datos) )
        self.connection.commit()

    def actualizar_equipo(self, datos_actualizar):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`equipo` SET `id_equipo` = '%s', `categoria`='%s', `equipo`='%s', `descripcion`='%s', `marca`='%s', `modelo`='%s', `proveedor_id`='%s', `comentarios`='%s'  WHERE (`id_equipo` = '%s')" % (datos_actualizar))
        self.connection.commit()

    def actualizar_equipo_ca(self, datos_actualizar):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`categoria_equipo` SET `id_categoria_equipo` = '%s', `categoria_equipo_nombre`='%s' WHERE (`id_categoria_equipo` = '%s')" % (datos_actualizar))
        self.connection.commit()

    def borrar_equipo(self, id_c):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM geopulso.equipo WHERE (`id_equipo` = '%s')" % (id_c))
        self.connection.commit()

    def borrar_equipo_ca(self, id_c):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM geopulso.categoria_equipo WHERE (`id_categoria_equipo` = '%s')" % (id_c))
        self.connection.commit()
        
    def anadir_datos_depreciacion_lra(self, datos):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`equipo` SET `valor_activo` = '%s', `vida_util_activo_annos` = '%s', `valor_residual` = '%s' WHERE (`id_equipo` = '%s')" % (datos))
        self.connection.commit()
    
    def anadir_depreciacion_lra(self, datos):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`equipo` SET `d_linea_recta_anual` = '%s' WHERE (`id_equipo` = '%s')" % (datos))
        self.connection.commit()

    def anadir_datos_depreciacion_lrm(self, datos):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`equipo` SET `valor_activo` = '%s', `vida_util_activo_meses` = '%s', `valor_residual` = '%s' WHERE (`id_equipo` = '%s')" % (datos))
        self.connection.commit()
    
    def anadir_depreciacion_lrm(self, datos):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`equipo` SET `d_linea_recta_mensual` = '%s' WHERE (`id_equipo` = '%s')" % (datos))
        self.connection.commit()

    def busqueda_equipo_depreciacion(self, criterio1):
        cursor= self.connection.cursor()
        cursor.execute("SELECT id_equipo FROM geopulso.equipo WHERE equipo LIKE '%s'" % (criterio1))
        self.datos = cursor.fetchall()
        return self.datos

    def detectar_depreciacion(self, id_actual):
        cursor= self.connection.cursor()
        cursor.execute("SELECT d_linea_recta_anual, d_linea_recta_mensual, d_suma_digitos_anuales, d_reduccion_datos FROM geopulso.equipo WHERE (`id_equipo` = '%s')" % (id_actual))
        self.datos = cursor.fetchall()
        return self.datos

    def poner_id_equipo(self, id_actual):
        cursor= self.connection.cursor()
        cursor.execute("UPDATE `geopulso`.`equipo_id` SET `id` = '%s' WHERE (`equipo_id` = 1)" % (id_actual))
        self.connection.commit()

    def tomar_id_equipo(self):
        cursor= self.connection.cursor()
        cursor.execute("SELECT id FROM geopulso.equipo_id WHERE (`equipo_id` = 1)")
        self.datos = cursor.fetchall()
        return self.datos
