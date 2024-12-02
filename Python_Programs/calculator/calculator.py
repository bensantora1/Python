import tkinter as tk

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x400")  # Adjusted window size for better fit

# Entry widget for display
display = tk.Entry(root, font=("Arial", 24), justify="right", bd=8)
display.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="we")

# Button click function
def on_button_click(value):
    if value == "C":
        display.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, value)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create buttons
row, col = 1, 0
for button in buttons:
    tk.Button(
        root, text=button, font=("Arial", 18),
        command=lambda b=button: on_button_click(b)
    ).grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Make columns expand proportionally
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Make rows expand proportionally
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
