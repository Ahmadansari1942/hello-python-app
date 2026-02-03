print("Hello World from Python")

name = input("Enter your name: ")
print(f"Hello {name}, welcome to Python!")


import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Hello Python App")
window.geometry("300x150")

# Function to run when button is clicked
def say_hello():
    label.config(text="Hello World from Python!")

# Label
label = tk.Label(window, text="", font=("Arial", 12))
label.pack(pady=20)

# Button
button = tk.Button(window, text="Click Me!", command=say_hello)
button.pack()

# Run the app
window.mainloop()


