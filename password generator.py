import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("420x430")
        
        # Dark Blue Background
        self.root.configure(bg="#0A1A2F")

        # Title
        title = tk.Label(
            root,
            text="Password Generator",
            font=("Arial", 24, "bold"),
            bg="#0A1A2F",
            fg="#4CC9F0"
        )
        title.pack(pady=20)

        # Password Length Input
        tk.Label(
            root,
            text="Password Length:",
            font=("Arial", 15),
            bg="#0A1A2F",
            fg="white"
        ).pack()
        
        self.length_entry = tk.Entry(
            root,
            font=("Arial", 15),
            width=10,
            bd=2,
            relief="solid"
        )
        self.length_entry.pack(pady=8)

        # Checkboxes Frame
        options = tk.Frame(root, bg="#0A1A2F")
        options.pack()

        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.num_var = tk.BooleanVar(value=True)
        self.sym_var = tk.BooleanVar(value=True)

        tk.Checkbutton(options, text="Uppercase (A-Z)", font=("Arial", 13),
                       variable=self.upper_var, bg="#0A1A2F", fg="white",
                       activebackground="#0A1A2F", selectcolor="#14243D").grid(row=0, column=0, sticky="w")
        
        tk.Checkbutton(options, text="Lowercase (a-z)", font=("Arial", 13),
                       variable=self.lower_var, bg="#0A1A2F", fg="white",
                       activebackground="#0A1A2F", selectcolor="#14243D").grid(row=1, column=0, sticky="w")
        
        tk.Checkbutton(options, text="Numbers (0-9)", font=("Arial", 13),
                       variable=self.num_var, bg="#0A1A2F", fg="white",
                       activebackground="#0A1A2F", selectcolor="#14243D").grid(row=2, column=0, sticky="w")
        
        tk.Checkbutton(options, text="Symbols (!@#$%)", font=("Arial", 13),
                       variable=self.sym_var, bg="#0A1A2F", fg="white",
                       activebackground="#0A1A2F", selectcolor="#14243D").grid(row=3, column=0, sticky="w")

        # Generate Button
        generate_btn = tk.Button(
            root, text="Generate Password",
            font=("Arial", 16, "bold"),
            bg="#4CC9F0",
            fg="black",
            activebackground="#3AB5DB",
            width=18,
            command=self.generate_password
        )
        generate_btn.pack(pady=15)

        # Output Field
        self.output = tk.Entry(
            root,
            font=("Arial", 18),
            bd=2,
            justify="center",
            relief="solid"
        )
        self.output.pack(pady=10, padx=20, fill="x")

        # Copy Button
        copy_btn = tk.Button(
            root, text="Copy to Clipboard",
            font=("Arial", 14, "bold"),
            bg="#3A86FF",
            fg="white",
            activebackground="#2667D1",
            width=16,
            command=self.copy_password
        )
        copy_btn.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except:
            messagebox.showerror("Error", "Enter a valid number!")
            return

        chars = ""
        if self.upper_var.get(): chars += string.ascii_uppercase
        if self.lower_var.get(): chars += string.ascii_lowercase
        if self.num_var.get(): chars += string.digits
        if self.sym_var.get(): chars += "!@#$%^&*()_+-=[]{}"

        if chars == "":
            messagebox.showwarning("Warning", "Select at least one option!")
            return

        password = "".join(random.choice(chars) for _ in range(length))

        self.output.delete(0, tk.END)
        self.output.insert(0, password)

    def copy_password(self):
        pwd = self.output.get()
        if pwd:
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
PasswordGenerator(root)
root.mainloop() 