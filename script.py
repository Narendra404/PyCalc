import tkinter as tk
window = tk.Tk()
frame = tk.Frame()
greeting = tk.Label(
        master=frame,
        relief=tk.RAISED,
        text="Hello", #text to display
        foreground="black", #set text color to white 
        background="white", #set background color to black
        width=5, #set width of the area
        height=1 #set height of the area
        )
button = tk.Button(
        master=frame,
        relief=tk.RAISED,
        text="Click Me",
        foreground="black",
        background="white",
        width=9,
        height=1
        )
greeting.pack()
button.pack()
frame.pack(side=tk.LEFT)
window.mainloop()
