#If you don't understand this just go to w3schools in your browser and read about python :|

import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("Application")
root.configure(bg="lightblue")

#Title:

title = tk.Label(root, text="Form", font=("Arial", 18), bg="lightblue")
title.pack()

#Inputs and labels:

labeUsername = tk.Label(root, text="Username: ", padx=56, pady=50, bg="lightblue")
labeUsername.place(relx = 0.48, rely = 0.2, anchor="e")

entry = tk.Entry(root)
entry.place(rely = 0.18, relx = 0.46)

#Pwd

labePassword = tk.Label(root, text="Password: ", padx=56, pady=50, bg="lightblue")
labePassword.place(relx = 0.48, rely = 0.35, anchor="e")

entryPwd = tk.Entry(root)
entryPwd.place(rely = 0.33, relx = 0.46)

def clicked():
    executeSomeText = tk.Label(root, text="Loading()", bg="lightblue")
    executeSomeText.place(rely = 0.53, relx = 0.46)

#Button

btn = tk.Button(root, padx=3, pady=3, text="Submit", background="lightgreen", command=clicked)
btn.place(rely = 0.43, relx = 0.46)
root.mainloop()

#destroy