import tkinter as tk
import customtkinter as ctk

def press_button(char):
    if char == "C":
        entry.delete(0, ctk.END)
    elif char == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, ctk.END)
            entry.insert(ctk.END, str(result))
        except:
            entry.configure(state="normal")
            entry.delete(0, ctk.END)
            entry.insert(ctk.END, "Ошибка")
            entry.configure(state="disabled")
    else:
        if entry.cget("state") == "disabled":
            return
        entry.insert(ctk.END, char)

def clear_screen():
    entry.configure(state="normal")
    entry.delete(0, "end")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Calculator_v1.1")
root.geometry("340x540")
root.resizable(width=False, height=False)
root.configure(fg_color="#1e1e1e")

author_label = ctk.CTkLabel(
    root, 
    text="Author: Shilov Boris 7B", 
    font=("Segoe UI", 12, "italic"), 
    text_color="#888888"
)

endlabel = ctk.CTkLabel(
    root,
    text='© 2026 Boris Shilov. All rights reserved.',
    font=("Segoe UI", 9, "italic"), 
    text_color="#888888"
)

author_label.grid(row=0, column=0, columnspan=4, pady=(15, 0))



entry = ctk.CTkEntry(
    root, 
    font=("Segoe UI", 26), 
    justify="right", 
    border_width=0, 
    fg_color="#2d2d2d", 
    text_color="#ffffff",
    corner_radius=10
)
entry.grid(row=1, column=0, columnspan=4, padx=15, pady=15, ipady=12, sticky="nsew")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(2, 6): 
    root.rowconfigure(i, weight=1)

button_index = 0
for row in range(2, 6): 
    for col in range(4):
        char = buttons[button_index]
        
        if char in ['/', '*', '-', '+', '=']:
            btn_color = "#ff9f0a"
            hover_color = "#ffb347"
            text_color = "#ffffff"
        elif char == 'C':
            btn_color = "#a5a5a5"
            hover_color = "#c5c5c5"
            text_color = "#000000"
            
        else:
            btn_color = "#333333"
            hover_color = "#444444"
            text_color = "#ffffff"
        btn = ctk.CTkButton(
            root, 
            text=char, 
            font=("Segoe UI", 18, "bold"), 
            fg_color=btn_color, 
            hover_color=hover_color,
            text_color=text_color,
            corner_radius=12,
            command=lambda c=char: clear_screen() if c == 'C' else press_button(c)
        )
        btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
        button_index += 1

endlabel.grid(row=6, column=0, columnspan=4, pady=(15, 0))
root.mainloop()