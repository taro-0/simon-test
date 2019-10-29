import tkinter as tk

colors = ["#009dd6", "#ed3c36", "#ffee00", "#ffffff"]

# Creates a new window
main = tk.Tk()
main.title("Simon")
main.configure(bg="#0b0c0e")
main.minsize(300, 450)
main.resizable(False, False)

# Configures grid rows
tk.Grid.rowconfigure(main, 0, weight=1)
tk.Grid.rowconfigure(main, 1, weight=1)

# Configures grid columns
tk.Grid.columnconfigure(main, 0, weight=1)
tk.Grid.columnconfigure(main, 1, weight=1)

# Creates labels and layout
blueLabel = tk.Label(text="blue").grid(row=0, column=0, sticky= tk.N + tk.S + tk.E + tk.W)
redLabel = tk.Label(text="red").grid(row=0, column=1, sticky= tk.N + tk.S + tk.E + tk.W)
greenLabel = tk.Label(text="green").grid(row=1, column=0, sticky= tk.N + tk.S + tk.E + tk.W)
yellowLabel = tk.Label(text="yellow").grid(row=1, column=1, sticky= tk.N + tk.S + tk.E + tk.W)


# Starts
main.mainloop()
