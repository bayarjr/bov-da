from tkinter import Button, Entry, Frame, Label, LabelFrame, Tk, messagebox
import tkinter as tk

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
        print(self.username.get())
        print(self.password.get())

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.username.set('')
        self.password.set('')

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
        print(self.username.get())
        print(self.password.get())
        print(self.password2.get())

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
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.password_entry2.delete(0, tk.END)
            self.username.set('')
            self.password.set('')
            self.password2.set('')
            self.ventana.destroy()
            print("Registrar")
  
        
    
    
def main():

    ventana = tk.Tk()
    # Crea la instancia de la clase VentanaPrincipal
    VentanaPrincipal(ventana)
    # Ejecuta la ventana
    ventana.mainloop()

if __name__ == "__main__":
    main()
