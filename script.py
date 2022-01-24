import tkinter as tk
window = tk.Tk()
greeting = tk.Label(
        text="Hello", #text to display
        foreground="white", #set text color to white 
        background="black", #set background color to black
        width=10, #set width of the area
        height=10 #set height of the area
        )
button = tk.Button(
        text="Click Me",
        foreground="white",
        background="blue",
        width=10,
        height=5
        )
entry = tk.Entry(
        fg="yellow",
        bg="blue",
        width=50
        )
greeting.pack()
button.pack()
entry.pack()
window.mainloop()
