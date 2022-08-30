from sqlite3 import connect
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

        
        