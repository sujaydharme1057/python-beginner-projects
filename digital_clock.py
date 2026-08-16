import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")


def time():
    string = strftime("%H:%M:%S %p\n%d/%m/%Y")
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(
    root,
    font=("DS-Digital", 70),
    background="black",
    foreground="purple"
)

label.pack(padx=30,pady=30)
time()
root.mainloop()