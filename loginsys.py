import customtkinter
import sqlite3

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

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

    loginframe = customtkinter.CTkButton(master=mother,command=savedetails,text="LOGIN",font=("Roboto", 14))
    loginframe.pack(padx=8,pady=20)

    getdetails()

def getdetails():
    name = usernamentry.get()
    password = passwordentry.get()
    savedetails(name, password)
    print(name,"\t",password)

def savedetails(name, password):
    connection = sqlite3.connect("login database.db")
    cursor = connection.cursor()

    createquery= """CREATE TABLE IF NOT EXISTS details
                    (NAME text,PASSWORD text)"""
    
    connection.execute(createquery)

    insert_query = """INSERT INTO details
                    (name,password)VALUES (?,?)"""
    
    insert_details = (name,password)

    cursor.execute(insert_query,insert_details )
    
    connection.commit()
    # connection.close()



if __name__=="__main__":
    root = customtkinter.CTk()
    root.geometry("600x500")
    root.title("LOGIN SYSTEM")
    # root.config(bg="#4D4D4D") 
    motherframe()
    
    root.mainloop()


# name = ("emmanule",12)
# print(type(name))