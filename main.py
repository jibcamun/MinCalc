import customtkinter as ctk
from tkinter import messagebox, filedialog

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("MinCalc")
app.geometry("400x600")
app.resizable(False, False)

def solve():
    calc_box.insert("end", "=")
    expression = calc_box.get("0.0", "end").strip()
    expression = expression.replace("x", "*")
    expression = expression.replace("=", "")
    try:
        result = eval(expression)
        calc_box.delete("0.0", "end")
        calc_box.insert("end", str(result))
    except Exception:
        messagebox.showerror("Error", "Invalid expression!")
        calc_box.delete("0.0", "end")
        calc_box.insert("end", "Error")

def save_to_file():
    content = calc_box.get("0.0", "end").strip()
    if content:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Success", "Calculation saved successfully!")
    else:
        messagebox.showwarning("Warning", "No calculation to save!")

calc_box = ctk.CTkTextbox(app, height=50, font=("Arial", 22), corner_radius=10)
calc_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("x", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, r, c) in buttons:
    if text == "=":
        btn = ctk.CTkButton(app, text=text, command=solve, font=("Arial", 14))
    elif text == "C":
        btn = ctk.CTkButton(app, text=text, command=lambda: calc_box.delete("0.0", "end"), font=("Arial", 22))
    else:
        btn = ctk.CTkButton(app, text=text, command=lambda val=text: calc_box.insert("end", val), font=("Arial", 22))
    btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

save_btn = ctk.CTkButton(app, text="Save", command=save_to_file, font=("Arial", 22))
save_btn.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

for i in range(6):
    app.grid_rowconfigure(i, weight=1)
for i in range(4):
    app.grid_columnconfigure(i, weight=1)

app.mainloop()
