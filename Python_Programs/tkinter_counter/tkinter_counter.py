import tkinter as tk

# Define the main application window
def create_app():
    # Create the main window
    root = tk.Tk()
    root.title("Counter App")
    root.geometry("300x200")  # Set window size

    # Counter variable
    counter = tk.IntVar(value=0)  # Create an integer variable

    # Define functions to handle button actions
    def increment():
        counter.set(counter.get() + 1)

    def reset():
        counter.set(0)

    # Create and arrange widgets in the window
    label = tk.Label(root, text="Counter:", font=("Arial", 16))
    label.pack(pady=10)

    counter_label = tk.Label(root, textvariable=counter, font=("Arial", 24), fg="blue")
    counter_label.pack(pady=10)

    increment_button = tk.Button(root, text="Increment", command=increment, bg="green", fg="white")
    increment_button.pack(side="left", padx=20, pady=20)

    reset_button = tk.Button(root, text="Reset", command=reset, bg="red", fg="white")
    reset_button.pack(side="right", padx=20, pady=20)

    # Run the application
    root.mainloop()

# Run the app
if __name__ == "__main__":
    create_app()
