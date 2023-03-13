from tkinter import Button, Entry, Frame, Label, LabelFrame, Tk, messagebox
import tkinter as tk
from tkinter import ttk
import psycopg2
import hashlib
import random
import string
import pyperclip

class BaseDatos:
    def __init__(self):
        self.conn = None
    
    def conectar(self):
        self.conn = psycopg2.connect(host="localhost", database="Boveda", user="postgres", password="j088058495r")
        #print("BD abierta")
        return self.conn
    
    def cerrar(self):
        if self.conn is not None:
            # Confirmar la transacción
            self.conn.commit()
            self.conn.close()
           #print("BD Cerrada")

class Encriptar:
    def __init__(self, passw):
        self.passw = passw

    def contrasena(self):
        """Función que encripta una contraseña utilizando SHA-256"""
        # Codifica la contraseña en bytes
        contraseña_bytes = self.passw.encode('utf-8')
        # Crea un objeto de hash SHA-256
        hash_obj = hashlib.sha256()
        # Actualiza el objeto de hash con los bytes de la contraseña
        hash_obj.update(contraseña_bytes)
        # Genera el hash de la contraseña en formato hexadecimal
        hash_hex = hash_obj.hexdigest()
        # Devuelve el hash de la contraseña
        return hash_hex

class VentanaPrincipal:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Bóveda de contraseñas")
        self.ventana.geometry("450x300")

        self.Objetos_ventana()

    def Objetos_ventana(self):
        # Crea frame para entradas
        self.frame = tk.LabelFrame(self.ventana)
        self.frame.pack(padx=40, pady=40)

        # Crear las etiquetas y las entradas de texto
        username_label = tk.Label(self.frame, text="Nombre de usuario")
        self.username_entry = tk.Entry(self.frame)

        password_label = tk.Label(self.frame, text="Contraseña")
        self.password_entry = tk.Entry(self.frame, show="*")

        # Crea las variables de instancia para guardar los valores de las entradas
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Asigna las variables de instancia a las cuadros de entrada de texto
        self.username_entry.config(textvariable = self.username)
        self.password_entry.config(textvariable = self.password)
       
                    
        # Crear los botones
        login_button = tk.Button(self.frame, text="Iniciar sesión", command = self.IniciarSesion)
        new_user_button = tk.Button(self.frame, text="Nuevo usuario", command = self.NuevoUsuario)

        # Ubicar los widgets en la ventana
        username_label.grid(row=0, column=0)
        self.username_entry.grid(row=0, column=1)

        password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)

        login_button.grid(row=3, column=0)
        new_user_button.grid(row=3, column=1)

    def IniciarSesion(self):
        if self.username.get() == "":
            messagebox.showerror("Error en crear usuario", "No ingreso el nombre de usuario")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.username.set('')
            self.password.set('')
        elif self.password.get() == "":
            messagebox.showerror("Error en crear usuario", "No ingreso la contraseña")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.username.set('')
            self.password.set('')
        else:
            bd = BaseDatos()
            conn = bd.conectar()
            # Creación de un cursor
            cur = conn.cursor()
            cur.execute("SELECT pass FROM master_user WHERE usuario = %s", (self.username.get(),))
            resultado = cur.fetchone()
            bd.cerrar()

            if resultado is not None:
                contrasena_bd = resultado[0]
                pE = Encriptar(self.password.get())
                passEncriptado = pE.contrasena()
                if contrasena_bd == passEncriptado:
                    self.ventana.withdraw() # Este método oculta la ventana actual, sin destruirla, para que no sea visible al usuario
                    ventana_i = tk.Toplevel(self.ventana)
                    VentanaI(ventana_i, self.username.get())
                else:
                    messagebox.showerror("Error", "Contraseña Incorrecta")
            else:
                messagebox.showerror("Error", "No se encontro el usuario")
        
            #print(self.username.get())
            #print(self.password.get())
            #print("iniciar sesión")
 
    def NuevoUsuario(self):
        ventana_nu = tk.Toplevel(self.ventana)
        VentanaNu(ventana_nu)
        #print("boton nuevo usuario")

class VentanaNu:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Nuevo Usuario")
        self.ventana.geometry("450x300")

        self.Objetos_ventanaNu()
    
    def Objetos_ventanaNu(self):
        # Crea frame para entradas
        self.frame = tk.LabelFrame(self.ventana)
        self.frame.pack(padx=40, pady=40)

        # Crear las etiquetas y las entradas de texto
        username_label = tk.Label(self.frame, text="Nombre de usuario")
        self.username_entry = tk.Entry(self.frame)

        password_label = tk.Label(self.frame, text="Contraseña")
        self.password_entry = tk.Entry(self.frame)

        password_label2 = tk.Label(self.frame, text="Repetir Contraseña")
        self.password_entry2 = tk.Entry(self.frame)

        # Crea las variables de instancia para guardar los valores de las entradas
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.password2 = tk.StringVar()

        # Asigna las variables de instancia a las cuadros de entrada de texto
        self.username_entry.config(textvariable = self.username)
        self.password_entry.config(textvariable = self.password)
        self.password_entry2.config(textvariable = self.password2)
       
                    
        # Crear los botones
        login_button = tk.Button(self.frame, text="Registrar", command = self.Registrar)
        
        # Ubicar los widgets en la ventana
        username_label.grid(row=0, column=0)
        self.username_entry.grid(row=0, column=1)

        password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)

        password_label2.grid(row=2, column=0)
        self.password_entry2.grid(row=2, column=1)

        login_button.grid(row=3, column=0)
       
    def Registrar(self):
                 
        if self.username.get() == "":
            messagebox.showerror("Error en crear usuario", "No ingreso el nombre de usuario")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.password_entry2.delete(0, tk.END)
            self.username.set('')
            self.password.set('')
            self.password2.set('')

        elif self.password.get() == "":
            messagebox.showerror("Error en crear usuario", "No ingreso la contraseña")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.password_entry2.delete(0, tk.END)
            self.username.set('')
            self.password.set('')
            self.password2.set('')

        elif self.password2.get() == "":
            messagebox.showerror("Error en crear usuario", "No ingreso la confirmación de contraseña")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.password_entry2.delete(0, tk.END)
            self.username.set('')
            self.password.set('')
            self.password2.set('')

        elif self.password.get() != self.password2.get():
            messagebox.showerror("Error en crear usuario", "Las contraseñas no son iguales")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.password_entry2.delete(0, tk.END)
            self.username.set('')
            self.password.set('')
            self.password2.set('')

        else: 
            pE= Encriptar(self.password.get())
            passEncriptado = pE.contrasena()
            bd = BaseDatos()
            conn = bd.conectar()
            # Creación de un cursor
            cur = conn.cursor()
            cur.execute("INSERT INTO master_user (usuario, pass) VALUES (%s, %s)", (str(self.username.get()), passEncriptado))
            #cur.execute("INSERT INTO credenciales (usuario_c) VALUES (%s)", (str(self.username.get()),))
            bd.cerrar()

            print(self.username.get())
            print(self.password.get())
            print(self.password2.get())
            print(passEncriptado)
            
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.password_entry2.delete(0, tk.END)
            self.username.set('')
            self.password.set('')
            self.password2.set('')
            self.ventana.withdraw()
                     
            #print("Registrar")
  
class VentanaI:
    

    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.ventana.title("Administrador de contraseñas")
        self.ventana.geometry("450x300")
        self.Objetos_ventanaI()
    
    def Objetos_ventanaI(self):
        #print ("ventana inicio")
        frame = tk.LabelFrame(self.ventana)
        frame.pack(padx=40, pady=40)
        frame1 = tk.LabelFrame(self.ventana)
        frame1.pack(padx=40, pady=40)

        bd = BaseDatos()
        conn = bd.conectar()
        # Creación de un cursor
        cur = conn.cursor()
        cur.execute("SELECT nombre_i FROM credenciales WHERE usuario_c = %s",(self.usuario, ))
        el = cur.fetchall()
        self.elementos = tuple(zip(*el))[0]
        bd.cerrar()

        print("seleccion objetos combo_box  :" + str(self.elementos))

        # Crear el ComboBox y agregarlo a la ventana
        labelNombre = tk.Label(frame, text="Nombre del servicio digital:")
        labelNombre.grid(row=0, column=0)
        self.combo_box = ttk.Combobox(frame, state="readonly")
        self.combo_box.grid(row=0, column=1)
        # Llenar el ComboBox con los elementos de la tupla
        self.combo_box["values"] = self.elementos
        # Vincular el ComboBox a una variable de control
        self.seleccion2 = tk.StringVar()
        self.combo_box.config(textvariable=self.seleccion2)
        self.combo_box.bind("<<ComboboxSelected>>", self.mostrar_elemento)

        #print("seleccion"+ self.seleccion2.get())
        
        # Crear la etiqueta donde se mostrará el elemento seleccionado
        labelUsuario = tk.Label(frame, text="Usuario:")
        labelUsuario.grid(row=1, column=0)
        self.entryU = tk.Entry(frame)
        self.entryU.grid(row=1, column=1)
        self.entryU.insert(0, " ")

        labelContra = tk.Label(frame, text="Contraseña:")
        labelContra.grid(row=2, column=0)
        self.entryC = tk.Entry(frame)
        self.entryC.grid(row=2, column=1)

        labelUrl = tk.Label(frame, text="URL:")
        labelUrl.grid(row=3, column=0)
        self.entryUr = tk.Entry(frame)
        self.entryUr.grid(row=3, column=1)
        
        labelNota = tk.Label(frame, text="Nota:")
        labelNota.grid(row=4, column=0)
        self.entryN = tk.Entry(frame)
        self.entryN.grid(row=4, column=1)
         
        # Crear los botones
        mod_button = tk.Button(frame1, text="Modificar", command = self.Modificar)
        mod_button.grid(row=0, column=0)
        new_button = tk.Button(frame1, text="Nuevo", command = self.NuevoCredencial)
        new_button.grid(row=0, column=1)
        salir_button = tk.Button(frame1, text="Salir", command = self.Salir)
        salir_button.grid(row=0, column=2)

    def mostrar_elemento(self, event):

        self.entryU.delete(0, "end")
        self.entryC.delete(0, "end")
        self.entryUr.delete(0, "end")
        self.entryN.delete(0, "end")
                      
        bd = BaseDatos()
        conn = bd.conectar()
        # Creación de un cursor
        cur = conn.cursor()
        cur.execute("SELECT usuario_i, contrasena_i, url_i, notas_i FROM credenciales WHERE usuario_c = %s AND nombre_i =%s",(self.usuario, self.seleccion2.get(), ))
        ele = cur.fetchall()
        bd.cerrar() 
        self.elementos1 = tuple(zip(*ele))

        # Obtener el elemento seleccionado
        print("elementos seleccionados" + str(self.elementos1))
        #print("elementos seleccionados2 " + str(self.elementos1[2][0]))

        self.entryU.insert(0, str(self.elementos1[0][0]))
        #self.entryU.config(state="disable")
        self.entryC.insert(0, str(self.elementos1[1][0]))
        #self.entryC.config(state="readonly")
        self.entryUr.insert(0, str(self.elementos1[2][0]))
        #self.entryUr.config(state="readonly")
        self.entryN.insert(0, str(self.elementos1[3][0]))
        #self.entryN.config(state="readonly")
     
    def Modificar(self):
        
        #print("Modificar")
        ventana_mod = tk.Toplevel(self.ventana)
        VentanaMod(ventana_mod, self.seleccion2.get(), self.usuario) 

    def NuevoCredencial(self):
        ventana_nu_cre = tk.Toplevel(self.ventana)
        VentanaNuCre(ventana_nu_cre, self.usuario)
        #print("boton nuevo credencial")

    def Salir(self):
        ventana_P = tk.Toplevel(self.ventana)
        VentanaPrincipal(ventana_P)
        self.ventana.withdraw()
      
class VentanaNuCre:

    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuarioC = usuario
        self.ventana.title("Nuevo Credencial")
        self.ventana.geometry("450x400")

        self.Objetos_ventanaNuCre()
    
    def Objetos_ventanaNuCre(self):
        
        # Crea frame para entradas
        self.frame = tk.Frame(self.ventana)
        self.frame.pack(padx=40, pady=10)

        self.frame1 = tk.Frame(self.ventana)
        self.frame1.pack(padx=40, pady=10)

        self.FrameGc = tk.LabelFrame(self.ventana, text="Generador de contraseñas")
        self.FrameGc.pack(padx=40, pady=10)

        # Crea labels y entry
        labelNombre = tk.Label(self.frame, text="Nombre del servicio digital:")
        labelNombre.grid(row=0, column=0)
        entryNombre = tk.Entry(self.frame)
        entryNombre.grid(row=0, column=1)
        
        labelUsuario = tk.Label(self.frame, text="Usuario:")
        labelUsuario.grid(row=1, column=0)
        entryUsuario = tk.Entry(self.frame)
        entryUsuario.grid(row=1, column=1)
        
        labelContrasena = tk.Label(self.frame, text="Contraseña:")
        labelContrasena.grid(row=2, column=0)
        entryContrasena = tk.Entry(self.frame)
        entryContrasena.grid(row=2, column=1)
        
        labelUrl = tk.Label(self.frame, text="URL:")
        labelUrl.grid(row=3, column=0)
        entryUrl = tk.Entry(self.frame)
        entryUrl.grid(row=3, column=1)
        
        labelNotas = tk.Label(self.frame, text="Notas:")
        labelNotas.grid(row=4, column=0)
        entryNotas = tk.Entry(self.frame)
        entryNotas.grid(row=4, column=1)

        # Generador de contraseñas 
        self.level = tk.StringVar()
        self.level.set("Bajo")
        self.level_choices = ["Bajo", "Medio", "Alto", "Muy alto"]
        self.level_dropdown = tk.OptionMenu(self.FrameGc, self.level, *self.level_choices)
        self.level_dropdown.pack()

        self.generate_button = tk.Button(self.FrameGc, text="Generar contraseña", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(self.FrameGc, text="")
        self.password_label.pack()

        self.copy_button = tk.Button(self.FrameGc, text="Copiar al portapapeles", command=self.copy_password)
        self.copy_button.pack()
  
        # Crea las variables de instancia para guardar los valores de las entradas
        self.nombre = tk.StringVar()
        self.usuario = tk.StringVar()
        self.contrasena = tk.StringVar()
        self.url = tk.StringVar()
        self.notas = tk.StringVar()

        # Asigna las variables de instancia a las cuadros de entrada de texto
        entryNombre.config(textvariable = self.nombre)
        entryUsuario.config(textvariable = self.usuario)
        entryContrasena.config(textvariable = self.contrasena)
        entryUrl.config(textvariable = self.url)
        entryNotas.config(textvariable = self.notas)
                
        # Crear botones
        btn_guardar = tk.Button(self.frame1, text="Guardar", command = self.Guardar)
        btn_guardar.grid(row=5, column=0)
        
    def Guardar(self):
        print("B Guardar")
        if self.nombre.get() == "":
            messagebox.showerror("Error", "No ingreso el nombre del sitio")
            
        elif self.usuario.get() == "":
            messagebox.showerror("Error", "No ingreso el usuario")
            
        elif self.contrasena.get() == "":
            messagebox.showerror("Error", "No ingreso la contraseña")
            
        elif self.url.get() == "":
            messagebox.showerror("Error", "No ingreso la URL")
          
        else: 
            bd = BaseDatos()
            conn = bd.conectar()
            # Creación de un cursor
            cur = conn.cursor()
            cur.execute("INSERT INTO credenciales (usuario_c, nombre_i, usuario_i, contrasena_i, url_i, notas_i) VALUES (%s, %s, %s, %s, %s, %s )", (str(self.usuarioC), str(self.nombre.get()), str(self.usuario.get()), str(self.contrasena.get()), str(self.url.get()), str(self.notas.get()),))
            bd.cerrar()

            #ventana_I = tk.Toplevel(self.ventana)
                  
            self.ventana.withdraw()
            VentanaI(self.ventana) 
                     
            #print("Se guardo en Bd")

    def generate_password(self):
        length = {"Bajo": 8, "Medio": 12, "Alto": 16, "Muy alto": 20}
        level = self.level.get()

        if level == "Bajo":
            chars = string.ascii_lowercase + string.digits
        elif level == "Medio":
            chars = string.ascii_letters + string.digits
        elif level == "Alto":
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            chars = string.ascii_letters + string.digits + string.punctuation + "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿"

        password = "".join(random.choice(chars) for _ in range(length[level]))
        self.password_label.configure(text=password)
        self.copy_button.config(text="Copiar al portapapeles",command=self.copy_password)

    def copy_password(self):
        password = self.password_label.cget("text")
        pyperclip.copy(password)
        self.copy_button.configure(text="¡Copiado!")

class VentanaMod:
    def __init__(self, ventana, SelNombre, usuario):
        self.ventana = ventana
        self.SelNombre = SelNombre
        self.usuario = usuario
        self.ventana.title("Modificar credenciales")
        self.ventana.geometry("450x300")

        self.Objetos_ventanaMod()

    def Objetos_ventanaMod(self):
        # Crea frame para entradas
        self.frame = tk.LabelFrame(self.ventana)
        self.frame.pack(padx=40, pady=10)
        
        self.frame1 = tk.LabelFrame(self.ventana)
        self.frame1.pack(padx=40, pady=10)
             
        labelUsuario = tk.Label(self.frame, text="Usuario:")
        labelUsuario.grid(row=1, column=0)
        self.entryUsuario = tk.Entry(self.frame)
        self.entryUsuario.grid(row=1, column=1)
        
        labelContrasena = tk.Label(self.frame, text="Contraseña:")
        labelContrasena.grid(row=2, column=0)
        self.entryContrasena = tk.Entry(self.frame)
        self.entryContrasena.grid(row=2, column=1)
        
        labelUrl = tk.Label(self.frame, text="URL:")
        labelUrl.grid(row=3, column=0)
        self.entryUrl = tk.Entry(self.frame)
        self.entryUrl.grid(row=3, column=1)
        
        labelNotas = tk.Label(self.frame, text="Notas:")
        labelNotas.grid(row=4, column=0)
        self.entryNotas = tk.Entry(self.frame)
        self.entryNotas.grid(row=4, column=1)

        mod_button = tk.Button(self.frame, text="Modificar", command = self.ModCe)
        mod_button.grid(row=5, column=1)

        # Conexión BD
        bd = BaseDatos()
        conn = bd.conectar()
        # Creación de un cursor
        cur = conn.cursor()
        cur.execute("SELECT usuario_i, contrasena_i, url_i, notas_i FROM credenciales WHERE usuario_c = %s AND nombre_i = %s", (self.usuario, self.SelNombre,))
        el = cur.fetchall()
        self.elementos = tuple(zip(*el))
        bd.cerrar()
        print("seleccion modificar "+ str(self.elementos))
        
        self.VaMoUs = tk.StringVar()
        self.VaMoCo = tk.StringVar()
        self.VaMoUr = tk.StringVar()
        self.VaMoNo = tk.StringVar()

        self.entryUsuario.insert(0, str(self.elementos[0][0]))
        
        self.entryContrasena.insert(0, str(self.elementos[1][0]))
        
        self.entryUrl.insert(0, str(self.elementos[2][0]))
        
        self.entryNotas.insert(0, str(self.elementos[3][0]))

    def ModCe(self):
        #self.entryUsuario.config(textvariable=self.VaMoUs)
        #self.entryContrasena.config(textvariable=self.VaMoCo)
        #self.entryUrl.config(textvariable=self.VaMoUr)
       # self.entryNotas.config(textvariable=self.VaMoNo)

        #print("sdfasd  "+str(self.VaMoUs.get()))
        #bd = BaseDatos()
        #conn = bd.conectar()
        # Creación de un cursor
        #cur = conn.cursor()
        #sentencia_sql = " UPDATE credenciales SET usuario_i = %s, contrasena_i = %s, url_i = %s, notas_i = %s WHERE  usuario_c = %s AND nombre_i = %s"
        #datos = (self.VaMoUs, self.VaMoCo, self.VaMoUr, self.VaMoNo, self.usuario, self.SelNombre)
        #cur.execute(sentencia_sql, datos)
        #cur.execute(" UPDATE credenciales SET usuario_i = %s, contrasena_i = %s, url_i = %s, notas_i = %s WHERE  usuario_c = %s AND nombre_i = %s", (str(self.VaMoUs.get()), str(self.VaMoCo.get()), str(self.VaMoUr.get()), str(self.VaMoNo.get()), str(self.usuario), str(self.SelNombre)))
       # bd.cerrar()
               
        self.ventana.destroy()
 
def main():       
    ventana = tk.Tk()
    # Crea la instancia de la clase VentanaPrincipal
    VentanaPrincipal(ventana)
    # Ejecuta la ventana
    ventana.mainloop()

if __name__ == "__main__":
    main()
