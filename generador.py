from tkinter import Button, Entry, Frame, Label, LabelFrame,Scrollbar, Tk, messagebox
import string
import random
import tkinter as tk
from tkinter import ttk

class Generador: 
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Generador de contraseñas")
        self.ventana.geometry("450x300")
        
        # Label Frame
        self.label_frame = LabelFrame(self.ventana, text="¿Que tan segura será tu contraseña?")
        self.label_frame.pack(pady=1)
        #Variable para nivel de complejidad
        complejidad=tk.StringVar()
        #Botones de radio para cada nivel
        opcion1 = tk.Radiobutton(self.label_frame, text="Muy Bajo", variable=complejidad, value=6)
        opcion2 = tk.Radiobutton(self.label_frame, text="Bajo", variable=complejidad, value=8)
        opcion3 = tk.Radiobutton(self.label_frame, text="Normal", variable=complejidad, value=10)
        opcion4 = tk.Radiobutton(self.label_frame, text="Dificil", variable=complejidad, value=12)
        opcion5 = tk.Radiobutton(self.label_frame, text="Muy Dificil", variable=complejidad, value=16)

        # Colocar los botones de radio en la ventana
        opcion1.grid(row=0, column=0)
        opcion2.grid(row=1, column=0)
        opcion3.grid(row=2, column=0)
        opcion4.grid(row=3, column=0)
        opcion5.grid(row=4, column=0)
        
        print(complejidad)
        # Crear una etiqueta para mostrar la contraseña generada
        self.etiqueta_contrasena = tk.Label(self.ventana, text="")
        self.etiqueta_contrasena.pack()




    
        

def main():

    ventana = tk.Tk()
    Generador(ventana)
    ventana.mainloop()
    


if __name__ == "__main__":
    main()