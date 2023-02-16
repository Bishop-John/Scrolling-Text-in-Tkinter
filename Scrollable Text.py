import tkinter as tk

root = tk.Tk()
delay = 100
svar = tk.StringVar()
label = tk.Label(root, textvariable=svar, height=10 )

def scroll():
    scroll.msg = scroll.msg[1:] + scroll.msg[0]
    svar.set(scroll.msg)
    root.after(delay, scroll)

scroll.msg = "Replace me with funny text |  "
scroll()
label.pack()
root.mainloop()
