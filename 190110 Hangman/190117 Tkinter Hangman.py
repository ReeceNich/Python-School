import tkinter as tk
from tkinter import messagebox as tk_messagebox
from PIL import ImageTk, Image


def main_gui():
    root = tk.Tk()
    root.geometry("450x500")
    
    TITLE_TXT = "Hangman!"
    TITLE_FONT = ("Arial Bold", 16)
    ENTER_BTN_TXT = "Enter!"
    BTN_FONT = ("Arial", 10)
    HELP_BTN_TXT = "Help!"

    title_lbl = tk.Label(root, text=TITLE_TXT, font=TITLE_FONT)
    title_lbl.grid(row=0, column=0, columnspan=3, sticky="N")


    path = "welcome.png"
    default_img = ImageTk.PhotoImage(Image.open(path))
    hangman_img = tk.Label(root, image=default_img)
    hangman_img.grid(row=1, column=0, columnspan=3)


    letter_input = tk.Entry(root)
    letter_input.grid(row=2, column=0)

    enter_btn = tk.Button(root, text=ENTER_BTN_TXT, font=BTN_FONT, command=None)
    enter_btn.grid(row=2, column=1, sticky="W")

    help_btn = tk.Button(root, text=HELP_BTN_TXT, font=BTN_FONT, command=help_menu)
    help_btn.grid(row=2, column=2, sticky="E")

    
    


    root.mainloop()
    
def help_menu():
    tk_messagebox.showinfo("Help me daddy!", "YEEEEEEEEEEEEEEET")
    
main_gui()
