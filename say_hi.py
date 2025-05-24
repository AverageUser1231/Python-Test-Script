import tkinter as tk

def say_hi():
    print("Hi!")

window = tk.Tk()
window.title("Say Hi App")
window.geometry("200x100")

button = tk.Button(window, text="Press me!", command=say_hi)
button.pack(pady=20)

window.mainloop()
