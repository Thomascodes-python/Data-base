


# customtkinter.set_appearance_mode("light")
# customtkinter.set_default_color_theme("green")

# def parentframes():
#     global fatherframe
#     fatherframe = customtkinter.CTkFrame(master=root,corner_radius=12,fg_color="white")
#     fatherframe.pack(padx=10,pady=10,fill="both",expand=True)   

#     childrenframes()


# def search():
#     search = searchentry.get()
#     print(search)



# def childrenframes():
#     global searchentry
#     searchentry = customtkinter.CTkEntry(master=fatherframe,width=680,placeholder_text="ENTER SEARCH")
#     searchentry.pack(padx=30,pady=10)
    
#     searchbutton = customtkinter.CTkButton(master=searchentry,command=search,text="SEARCH",font=("Roboto",12),width=10)
#     searchbutton.place(x=620,y=0)


# if __name__=="__main__":
#     root = customtkinter.CTk()
#     root.geometry("800x600+300+50")
#     root.title("WEB BROSWER")

#     parentframes()
#     root.mainloop()

import webview
import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
  
root.geometry("800x450")
  


webview.create_window('web browser', 'https://google.com')
webview.start()