import customtkinter


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

from app import *

def motherframe():
    global mother
    mother = customtkinter.CTkFrame(master=root)
    mother.pack(padx=50,pady=20,fill="both",expand=True)

    childrenframe()

def childrenframe():
    global usernamentry,passwordentry
    frame = customtkinter.CTkLabel(master=mother,text="LOGIN PAGE",font=("Roboto", 26 ))
    frame.pack(padx=16,pady=14)

    
    usernamentry = customtkinter.CTkEntry(master=mother,width=240,placeholder_text="USERNAME")
    usernamentry.pack(padx=8,pady=20)

    passwordentry = customtkinter.CTkEntry(master=mother,width=240,show="*",placeholder_text="PASSWORD")
    passwordentry.pack(padx=8,pady=20)

    # genderframe = customtkinter.CTkLabel(master=mother,text="GENDER",font=("Arial", 16))
    # genderframe.pack(padx=2,pady=20)

    loginframe = customtkinter.CTkButton(master=mother, command= lambda: clicked('clicked'), text="LOGIN",font=("Roboto", 14))
    loginframe.pack(padx=8,pady=20)






if __name__=="__main__":
    global usernamentry,passwordentry
    root = customtkinter.CTk()
    root.geometry("600x500")
    root.title("LOGIN SYSTEM")
    # root.config(bg="#4D4D4D") 
   
    motherframe()

    get_entries(usernamentry.get(), passwordentry.get())
    root.mainloop()

    






