import tkinter as tk
window = tk.Tk()
frame = tk.Frame()
greeting = tk.Label(
        master=frame,
        text="Hello", #text to display
        foreground="white", #set text color to white 
        background="black", #set background color to black
        width=10, #set width of the area
        height=10 #set height of the area
        )
button = tk.Button(
        master=frame,
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
frame.pack()
entry.pack()
window.mainloop()
