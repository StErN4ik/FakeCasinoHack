import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import time

def progress():
    for i in range(101):
        time.sleep(0.1)
        progress_bar['value'] = i
        percentage.set("Казино взломано на " + str(i) + "% \nВыкачанно: " + str(i*120000) + " руб.")
        window.update_idletasks()
        if i == 99:
            messagebox.showerror("Уведомление", "К тебе выехали, хуль.")
            return

def start():
    button.grid_forget()
    progress()

window = tk.Tk()
window.title("Взлом КАЗИНО")
window.iconbitmap(default="icon.ico")

progress_bar = ttk.Progressbar(window, orient='horizontal', mode='determinate', length=300)
progress_bar.grid(column=0, row=1, padx=10, pady=10)

percentage = tk.StringVar()
percentage.set("Казино взломано на 0%. \nВыкачано: 0 руб.")
text_label = tk.Label(window, textvariable=percentage)
text_label.grid(column=0, row=0)

button = ttk.Button(window, text="Начать", command=start)
button.grid(row=2, column=0, pady=10)
window.mainloop()
