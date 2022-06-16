import tkinter
import tkinter.messagebox
import customtkinter
import project_she_hulk
from tkinter import filedialog

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("700x540")
app.title("INNOVATIIVE DATA PROTECTION")

def change_mode(switch_2):
        if switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")


def UploadAction1(event=None):
    filename = filedialog.askopenfilename()
    entry1.delete(0,"end")
    entry1.insert(0, filename)
def UploadAction2(event=None):
    filename = filedialog.askopenfilename()
    entry2.delete(0,"end")
    entry2.insert(0, filename)


switch_2 = customtkinter.CTkSwitch(master=app,text="Dark Mode",command=lambda :change_mode(switch_2))
label1 = customtkinter.CTkLabel(master =app,text="Enter the first image ")
label2 = customtkinter.CTkLabel(master =app,text="Enter the second image ")

entry1 = customtkinter.CTkEntry(master = app)
entry2 = customtkinter.CTkEntry(master = app)

label1.grid(row=1, column=0, pady=10, padx=20, sticky="w")
label2.grid(row=2, column=0, pady=10, padx=20, sticky="w")

entry1.grid(row=1, column=1, pady=10, padx=20, sticky="w")
entry2.grid(row=2, column=1, pady=10, padx=20, sticky="w")

button1 = customtkinter.CTkButton(master=app,text="Choose File",command = UploadAction1)
button2 = customtkinter.CTkButton(master=app,text="Choose File",command = UploadAction2)

button3 = customtkinter.CTkButton(master=app,text="Encode",command = lambda : project_she_hulk.encrypt(entry1.get(),entry2.get()))
button4 = customtkinter.CTkButton(master=app,text="Decode",command = lambda : project_she_hulk.decrypt("final.png"))



button1.grid(row=1, column=2, pady=10, padx=20, sticky="w")
button2.grid(row=2, column=2, pady=10, padx=20, sticky="w")
button3.grid(row=3, column=2, pady=10, padx=20, sticky="w")
button4.grid(row=4, column=2, pady=10, padx=20, sticky="w")





switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")


app.mainloop()