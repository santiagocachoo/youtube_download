import tkinter
import customtkinter
from pytube import YouTube

# funcion de descargar
def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link)
        video = yt_object.streams.get_highest_resolution()
        video.download()
    except Exception as e:
        print(f'Error : {e}')
        

# configuración de sistema
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# ventana de app
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# añadir elementos visuales
title = customtkinter.CTkLabel(app, text='Inserta un link de YouTube')
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# boton de descargar
download = customtkinter.CTkButton(app, text='Descargar', command=start_download)
download.pack(padx=10, pady=10)


# correr aplicación
app.mainloop()