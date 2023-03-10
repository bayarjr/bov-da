import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Generador de contraseñas", font=("Arial", 18))
        self.title_label.pack(pady=10)

        self.level_label = tk.Label(self, text="Nivel de complejidad:")
        self.level_label.pack()

        self.level_var = tk.StringVar()
        self.level_var.set("1")
        self.level_radio1 = tk.Radiobutton(self, text="Bajo (sólo letras minúsculas)", variable=self.level_var, value="1")
        self.level_radio1.pack(anchor="w")
        self.level_radio2 = tk.Radiobutton(self, text="Medio (letras minúsculas y números)", variable=self.level_var, value="2")
        self.level_radio2.pack(anchor="w")
        self.level_radio3 = tk.Radiobutton(self, text="Alto (letras mayúsculas, minúsculas y números)", variable=self.level_var, value="3")
        self.level_radio3.pack(anchor="w")
        self.level_radio4 = tk.Radiobutton(self, text="Muy alto (letras mayúsculas, minúsculas, números y símbolos)", variable=self.level_var, value="4")
        self.level_radio4.pack(anchor="w")
        self.level_radio5 = tk.Radiobutton(self, text="Personalizado", variable=self.level_var, value="5")
        self.level_radio5.pack(anchor="w")

        self.custom_label = tk.Label(self, text="Caracteres permitidos (separados por comas):", state="disabled")
        self.custom_label.pack(pady=5)
        self.custom_entry = tk.Entry(self, state="Disable")
        self.custom_entry.pack()

        if self.level_var!=5:
            self.var = tk.StringVar
            self.custom_entry.config(state="active", textvariable = self.var)
        else:
            self.custom_entry.config(state="disabled")
            
            
        

        self.generate_button = tk.Button(self, text="Generar contraseña", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self, font=("Arial", 14), wraplength=350)
        self.password_label.pack()

    def generate_password(self):
        level = self.level_var.get()

        if level == "1":
            chars = "abcdefghijklmnopqrstuvwxyz"
        elif level == "2":
            chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        elif level == "3":
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        elif level == "4":
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
        elif level == "5":
            chars = self.var
        else:
            custom_chars = self.custom_entry.get()
            chars = "".join(set(custom_chars))

        password = "".join(random.choice(chars) for _ in range(10))
        self.password_label.configure(text=password)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
