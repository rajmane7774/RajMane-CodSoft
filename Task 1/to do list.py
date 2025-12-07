import tkinter as tk
from tkinter import ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("470x670")
        self.root.configure(bg="#FFFFFF")

        self.tasks = []

        # Title
        title = tk.Label(
            root, text="To-Do List", font=("Poppins", 30, "bold"),
            bg="#FFFFFF", fg="#2C3E50"
        )
        title.pack(pady=15)

        # Entry area
        entry_frame = tk.Frame(root, bg="#FFFFFF")
        entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(
            entry_frame, font=("Poppins", 16), width=22,
            relief="solid", bd=1, bg="#F2F4F7"
        )
        self.task_entry.grid(row=0, column=0, padx=5)

        add_btn = tk.Button(
            entry_frame, text="Add +", font=("Poppins", 14, "bold"),
            bg="#2980B9", fg="white", width=7,
            command=self.add_task, relief="flat"
        )
        add_btn.grid(row=0, column=1)

        # Scroll container
        container = tk.Frame(root)
        container.pack(fill="both", expand=True, pady=10)

        canvas = tk.Canvas(container, bg="#FFFFFF", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.task_frame = tk.Frame(canvas, bg="#FFFFFF")

        self.task_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bottom buttons
        control_frame = tk.Frame(root, bg="#FFFFFF")
        control_frame.pack(pady=15)

        clear_btn = tk.Button(
            control_frame, text="Clear All", font=("Poppins", 15, "bold"),
            bg="#E67E22", fg="white", width=10,
            relief="flat", command=self.clear_all
        )
        clear_btn.grid(row=0, column=0, padx=10)

        exit_btn = tk.Button(
            control_frame, text="Exit", font=("Poppins", 15, "bold"),
            bg="#C0392B", fg="white", width=10,
            relief="flat", command=self.root.quit
        )
        exit_btn.grid(row=0, column=1, padx=10)

    # Add Task
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text == "":
            return

        frame = tk.Frame(self.task_frame, bg="#FFFFFF", bd=1, relief="solid")
        frame.pack(fill="x", padx=10, pady=8)

        # Modern checkmark ✓
        tick_var = tk.StringVar(value="○")

        tick_btn = tk.Button(
            frame, textvariable=tick_var, font=("Arial", 20, "bold"),
            bg="#FFFFFF", fg="#3498DB", bd=0,
            command=lambda v=tick_var, f=frame: self.toggle_done(v, f)
        )
        tick_btn.pack(side="left", padx=10)

        label = tk.Label(
            frame, text=task_text, font=("Poppins", 17),
            bg="#FFFFFF", fg="#2C3E50"
        )
        label.pack(side="left", padx=5)

        del_btn = tk.Button(
            frame, text="✕", font=("Arial", 16, "bold"),
            bg="#EC7063", fg="white", width=3, relief="flat",
            command=lambda f=frame: self.delete_task(f)
        )
        del_btn.pack(side="right", padx=10)

        self.tasks.append((frame, label, tick_var))
        self.task_entry.delete(0, tk.END)

    # Toggle Done / Not Done
    def toggle_done(self, var, frame):
        for child in frame.winfo_children():
            if isinstance(child, tk.Label):
                if var.get() == "○":
                    var.set("✓")
                    child.config(fg="#95A5A6", font=("Poppins", 17, "overstrike"))
                else:
                    var.set("○")
                    child.config(fg="#2C3E50", font=("Poppins", 17))

    # Delete Task
    def delete_task(self, frame):
        frame.destroy()

    # Clear All
    def clear_all(self):
        for task in self.tasks:
            task[0].destroy()
        self.tasks.clear()


# Run app
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
