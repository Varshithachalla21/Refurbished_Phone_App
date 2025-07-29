import tkinter as tk
from tkinter import messagebox, ttk
from data import inventory
from utils import calculate_price, condition_mapping, is_profitable

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Refurbished Phone Seller App")
        self.root.geometry("900x600")
        self.login_screen()

    def login_screen(self):
        self.clear_window()
        
        frame = tk.Frame(self.root, bg="white")
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(frame, text="Login", font=("Arial", 24), bg="white").grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(frame, text="Username:", bg="white", font=("Arial", 14)).grid(row=1, column=0, sticky=tk.E, padx=10)
        self.username_entry = tk.Entry(frame, width=30)
        self.username_entry.grid(row=1, column=1, pady=10)

        tk.Label(frame, text="Password:", bg="white", font=("Arial", 14)).grid(row=2, column=0, sticky=tk.E, padx=10)
        self.password_entry = tk.Entry(frame, show='*', width=30)
        self.password_entry.grid(row=2, column=1, pady=10)

        tk.Button(frame, text="Login", font=("Arial", 14), command=self.verify_login).grid(row=3, column=0, columnspan=2, pady=20)

    def verify_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin123":
            self.dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def dashboard(self):
        self.clear_window()
        tk.Label(self.root, text="Available Phones for Sale", font=("Arial", 20, "bold")).pack(pady=10)

        columns = ("Model", "Condition", "Stock", "Platform", "Mapped Condition", "Selling Price")
        tree = ttk.Treeview(self.root, columns=columns, show='headings')
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=130)

        for phone in inventory:
            if phone.stock == 0:
                continue

            for platform in ["X", "Y", "Z"]:
                mapped = condition_mapping.get(phone.condition, {}).get(platform, "N/A")
                selling_price = calculate_price(platform, phone.base_price)
                if is_profitable(platform, phone.base_price, selling_price):
                    tree.insert("", tk.END, values=(
                        phone.model,
                        phone.condition,
                        phone.stock,
                        platform,
                        mapped,
                        f"${selling_price}"
                    ))

        tree.pack(expand=True, fill="both", pady=20)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
