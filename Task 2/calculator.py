import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dark Calculator")
        self.root.geometry("340x500")
        self.root.config(bg="#121212")  # Dark background

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 30),
            bd=0,
            relief="flat",
            justify="right",
            bg="#1e1e1e",
            fg="white",
            insertbackground="white"
        )
        self.display.pack(fill="both", ipady=20, pady=15, padx=15)

        # Button layout
        buttons = [
            ["C", "⌫", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["0", ".", "="],
        ]

        for row in buttons:
            frame = tk.Frame(root, bg="#121212")
            frame.pack(expand=True, fill="both")
            for btn in row:
                color = self.get_btn_color(btn)

                tk.Button(
                    frame,
                    text=btn,
                    font=("Arial", 22, "bold"),
                    bg=color,
                    fg="white",
                    activebackground="#333333",
                    activeforeground="white",
                    relief="flat",
                    borderwidth=0,
                    command=lambda x=btn: self.on_click(x)
                ).pack(side="left", expand=True, fill="both", padx=8, pady=8)

    # Modern button colors
    def get_btn_color(self, btn):
        if btn in ["C", "⌫"]:
            return "#d63031"  # Soft red
        if btn == "=":
            return "#00b894"  # Neon green
        if btn in ["+", "−", "×", "÷"]:
            return "#0984e3"  # Modern blue
        return "#2d3436"     # Dark grey for numbers

    # Handle button clicks
    def on_click(self, char):
        if char == "C":
            self.expression = ""
            self.update_display()

        elif char == "⌫":
            self.expression = self.expression[:-1]
            self.update_display()

        elif char == "=":
            try:
                expr = self.expression.replace("×", "*").replace("÷", "/").replace("−", "-")
                result = str(eval(expr))
                self.expression = result
                self.update_display()
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""

        else:
            self.expression += char
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

root = tk.Tk()
Calculator(root)
root.mainloop()
