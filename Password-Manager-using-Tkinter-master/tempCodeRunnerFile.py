from tkinter import Button, Entry, Frame, Label, LabelFrame, Tk
import string
from secrets import choice
from tkinter.constants import END

UPPERCASE = list(string.ascii_uppercase)
LOWERCASE = list(string.ascii_lowercase)
NUMBER = list(string.digits)
SYMBOLS = ['@', '#', '$', '%', '&', '_']


class PasswordGenerator:

    def __init__(self):
        self.window = Tk()
        self.window.title("Password Generator")
        self.window.geometry("450x300")
