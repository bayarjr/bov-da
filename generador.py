import random
import string
import pyperclip
import tkinter as tk


class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Generador de contraseñas")

        self.label = tk.Label(master, text="Nivel de complejidad:")
        self.label.pack()

        self.level = tk.StringVar()
        self.level.set("Bajo")
        self.level_choices = ["Bajo", "Medio", "Alto", "Muy alto"]
        self.level_dropdown = tk.OptionMenu(master, self.level, *self.level_choices)
        self.level_dropdown.pack()

        self.generate_button = tk.Button(master, text="Generar contraseña", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="")
        self.password_label.pack()

        self.copy_button = tk.Button(master, text="Copiar al portapapeles", command=self.copy_password)
        self.copy_button.pack()

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
        

root = tk.Tk()
my_password_generator = PasswordGenerator(root)
root.mainloop()
