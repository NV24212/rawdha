from tkinter import ttk
import tkinter as tk
import webbrowser

def autostart():
   btn1.enabled = True

def server():
   autostart()
   webbrowser.open_new_tab('http://127.0.0.1:5000')



window=tk.Tk()
window.geometry("300x300")
window.title("روضتي")


label1 = tk.Label(window, text="نظام الروضة", font=("Times new roman", 30))
label1.pack(padx=5, pady=5)


panel1 = ttk.Frame(window)
panel1.place(relx=0.5, rely=0.5, anchor='center')




btn1 = tk.Button(panel1, text="تشغيل السرفر", bg="pink", width=25, height=10, font=("Arial", 11, "bold"))
btn1.grid(column=0, row=0)
btn1.bind("<Button-1>")

server()


window.mainloop()