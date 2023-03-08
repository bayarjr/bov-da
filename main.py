from tkinter import Button, Entry, Frame, Label, LabelFrame, Tk, messagebox
import tkinter as tk
from tkinter import ttk
import psycopg2
import hashlib

class BaseDatos:
    def __init__(self):
        self.conn = None
    
    def conectar(self):
        self.conn = psycopg2.connect(host="localhost", database="Boveda", user="postgres", password="j088058495r")
        print("BD abierta")
        return self.conn
    
    def cerrar(self):
        if self.conn is not None:
            # Confirmar la transacción
            self.conn.commit()
            self.conn.close()
            print("BD Cerrada")

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

            
            print(self.username.get())
            print(self.password.get())
            print("iniciar sesión")
 
    def NuevoUsuario(self):
        ventana_nu = tk.Toplevel(self.ventana)
        VentanaNu(ventana_nu)
        print("boton nuevo usuario")

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
            cur.execute("INSERT INTO credenciales (usuario_c) VALUES (%s)", (str(self.username.get()),))
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
            self.ventana.destroy()
                     
            print("Registrar")
  
class VentanaI:

    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.ventana.title("Administrador de contraseñas")
        self.ventana.geometry("450x300")
        self.Objetos_ventanaI()
    
    def Objetos_ventanaI(self):
        print ("ventana inicio")
        frame = tk.LabelFrame(self.ventana)
        frame.pack(padx=40, pady=10)
        frame1 = tk.LabelFrame(self.ventana)
        frame1.pack(padx=40, pady=10)

        self.elementos = ("Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5")

        # Crear el ComboBox y agregarlo a la ventana
        combo_box = ttk.Combobox(frame, state="readonly")
        combo_box.grid(row=0, column=0)
        
        # Llenar el ComboBox con los elementos de la tupla
        combo_box["values"] = self.elementos

        # Vincular el ComboBox a una variable de control
        self.seleccion = tk.StringVar()
        combo_box.config(textvariable=self.seleccion)
        combo_box.bind("<<ComboboxSelected>>", self.mostrar_elemento)
        
        # Crear la etiqueta donde se mostrará el elemento seleccionado
        self.entry = tk.Entry(frame)
        self.entry.grid(row=1, column=0)

        # Crear los botones
        mod_button = tk.Button(frame1, text="Modificar", command = self.Modificar)
        #mod_button.grid(row=0, column=0)
        mod_button.grid(row=0, column=0)
        new_button = tk.Button(frame1, text="Nuevo", command = self.NuevoCredencial)
        #new_button.grid(row=0, column=1)
        new_button.grid(row=0, column=1)

    def mostrar_elemento(self, event):
        # Obtener el elemento seleccionado
        elemento = self.seleccion.get()
        self.entry.insert(0, elemento)
        # Configurar el widget Entry como de solo lectura
        self.entry.config(state="readonly")
       
    def Modificar(self):
        print("Modificar") 
        self.entry.config(state="normal")

    def NuevoCredencial(self):
        ventana_nu_cre = tk.Toplevel(self.ventana)
        VentanaNuCre(ventana_nu_cre)
        print("boton nuevo credencial")

class VentanaNuCre:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Nuevo Credencial")
        self.ventana.geometry("450x300")

        self.Objetos_ventanaNuCre()
    
    def Objetos_ventanaNuCre(self):
        
        # Crea frame para entradas
        self.frame = tk.LabelFrame(self.ventana)
        self.frame.pack(padx=40, pady=10)

        self.frame1 = tk.LabelFrame(self.ventana)
        self.frame1.pack(padx=40, pady=10)

        # Crea labels y entry
        labelNombre = tk.Label(self.frame, text="(Nombre del servicio digital:")
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
        
        btn_cancelar = tk.Button(self.frame1, text="Generar Contraseñas", command = self.GenerarContra)
        btn_cancelar.grid(row=5, column=1)
    
    def Guardar():
        print("B Guardar")

    def GenerarContra():
        print("B Generar Contra")


def main():       
    ventana = tk.Tk()
    # Crea la instancia de la clase VentanaPrincipal
    VentanaPrincipal(ventana)
    # Ejecuta la ventana
    ventana.mainloop()

if __name__ == "__main__":
    main()
