from tkinter import Button, Entry, Frame, Label, LabelFrame, Tk, messagebox
import tkinter as tk
from tkinter import ttk
import psycopg2

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
            self.ventana.withdraw() 
            ventana_i = tk.Toplevel(self.ventana)
            VentanaI(ventana_i)
            
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
        bd = BaseDatos()
        conn = bd.conectar()
        # Creación de un cursor
        cur = conn.cursor()
           
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
            # Ejecución de una sentencia SQL para insertar datos en una tabla
            cur.execute("INSERT INTO master_user (usuario, pass) VALUES (%s, %s)", (self.username.get(), self.password.get()))
            bd.cerrar()

            print(self.username.get())
            print(self.password.get())
            print(self.password2.get())
            
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.password_entry2.delete(0, tk.END)
            self.username.set('')
            self.password.set('')
            self.password2.set('')
            self.ventana.destroy()
                     
            print("Registrar")

            

class VentanaI:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Administrador de contraseñas")
        self.ventana.geometry("450x300")

        self.Objetos_ventanaI()
    
    def Objetos_ventanaI(self):
        print ("ventana inicio")
        self.frame = tk.LabelFrame(self.ventana)
        self.frame.pack(padx=40, pady=40)
        self.frame1 = tk.LabelFrame(self.ventana)
        self.frame1.pack(padx=40, pady=40)

        self.elementos = ("Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5")

        # Crear el ComboBox y agregarlo a la ventana
        self.combo_box = ttk.Combobox(self.frame, state="readonly")
        self.combo_box.pack(padx=20, pady=10)

        # Llenar el ComboBox con los elementos de la tupla
        self.combo_box["values"] = self.elementos

        # Vincular el ComboBox a una variable de control
        self.seleccion = tk.StringVar()
        self.combo_box.config(textvariable=self.seleccion)
        self.combo_box.bind("<<ComboboxSelected>>", self.mostrar_elemento)
        
        # Crear la etiqueta donde se mostrará el elemento seleccionado
        self.label_elemento = tk.Label(self.frame, text="")
        self.label_elemento.pack(padx=20, pady=10)

        # Crear los botones
        mod_button = tk.Button(self.frame1, text="Modificar", command = self.Modificar)
        mod_button.grid(row=3, column=0)

    def mostrar_elemento(self, event):
        # Obtener el elemento seleccionado
        elemento = self.seleccion.get()

        # Mostrar el elemento seleccionado en la etiqueta
        self.label_elemento.config(text=f"Elemento seleccionado: {elemento}")

    def Modificar(self):
        print("Modificar") 
   
def main():       
    ventana = tk.Tk()
    # Crea la instancia de la clase VentanaPrincipal
    VentanaPrincipal(ventana)
    #bd = BaseDatos()
    #bd.conectar()
    #bd.cerrar()
    # Ejecuta la ventana
    ventana.mainloop()

    

if __name__ == "__main__":
    main()


