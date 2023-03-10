import random
import string
import tkinter as tk


class PasswordGenerator:
    def __init__(self, window):
        # create a label for the complexity level selection
        level_label = tk.Label(window, text="Select password complexity level:")
        level_label.pack()

        # create a dropdown menu for the complexity level selection
        self.selected_level = tk.StringVar()
        level_dropdown = tk.OptionMenu(window, self.selected_level, "1", "2", "3", "4", "5")
        level_dropdown.pack()

        # create a button to generate the password
        generate_button = tk.Button(window, text="Generate Password", command=self.generate)
        generate_button.pack()

        # create a label to display the generated password
        self.password_label = tk.Label(window, text="")
        self.password_label.pack()

    def generate_password(self, level):
        """Generates a password of varying complexity based on the level chosen."""
        if level == 1:
            # level 1: only lowercase letters
            password = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        elif level == 2:
            # level 2: lowercase and uppercase letters
            password = ''.join(random.choice(string.ascii_letters) for i in range(8))
        elif level == 3:
            # level 3: letters and digits
            password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(12))
        elif level == 4:
            # level 4: letters, digits, and special characters
            password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(16))
        elif level == 5:
            # level 5: secure password with uppercase, lowercase, digits, and special characters
            uppercase = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
            lowercase = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
            digits = ''.join(random.choice(string.digits) for i in range(2))
            special_chars = ''.join(random.choice(string.punctuation) for i in range(2))
            password = uppercase + lowercase + digits + special_chars
            password += ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(12))
        return password

    def generate(self):
        """Generates and displays a password based on the selected complexity level."""
        level = int(self.selected_level.get())
        password = self.generate_password(level)
        self.password_label.config(text=password)


# create the tkinter window
window = tk.Tk()
window.title("Password Generator")

# create an instance of the PasswordGenerator class
password_generator = PasswordGenerator(window)

# start the tkinter event loop
window.mainloop()