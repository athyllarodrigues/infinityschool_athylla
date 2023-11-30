import tkinter as tk

def press_key(key):
    current = entry_var.get()
    entry_var.set(current + str(key))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Erro")


window = tk.Tk()
window.title("Calculadora")


entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, justify="right", font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, command=lambda key=button: press_key(key) if key != '=' else calculate(), font=("Arial", 14)).grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


tk.Button(window, text="C", command=clear_entry, font=("Arial", 14)).grid(row=row_val, column=col_val, sticky="nsew", columnspan=2)


for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)


window.mainloop()
