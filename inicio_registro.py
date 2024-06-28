from tkinter import*
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk



def gracias():
            messagebox.showinfo("Aviso", "º||M||º Acuerdate º||M||º")

def insertar_datos():
    bd = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tienda")

    mcursor = bd.cursor()

    sql = "INSERT INTO login (cliente, contraseña) VALUES ('{0}','{1}')".format(texto_usuario.get(), texto_contraseña.get())

    try:
        mcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Valido", title="Aviso")

    except:
        bd.rollback()
        messagebox.showwarning(message="Registro No Valido", title="Aviso")

    bd.close()

root = Tk()
root.title("º||M||º Login")
root.geometry("700x500+100+50")
root.resizable(False,False)
root.config(highlightcolor="black", highlightthickness=1)

image = Image.open("logo_sesion.png")
image = image.resize((700,500))

photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.image = photo
label.place(x=0, y=0, relwidth=1, relheight=1)


frame_registro = Frame(root, bg = "pink",highlightcolor="black", highlightthickness=1)
frame_registro.place(x =20,y = 40,height=340,width=500)


titulo = Label(frame_registro, text = "Nuevos Usuarios", 
    font = ("Arial",25,"bold"),
    fg="black", bg="pink").place(x=125,y=10)
sesion = Label(frame_registro, text = "Area de Registro de sesion", 
    font = ("Arial",15,"bold"),
    fg="black", bg="pink").place(x=130,y=55)


usuario = Label(frame_registro, text = "Nombre de usuario: ", 
    font = ("Arial",15,"bold"),
    fg="black", bg="pink").place(x=130,y=85)
texto_usuario = Entry(frame_registro, font=("times new roman",15),
    bg="lightgray", cursor = "pencil")
texto_usuario.place(x=130,y=115,width=250,height=25)

contraseña_label = Label(frame_registro, text="Contraseña: ", 
                         font=("Arial", 15, "bold"),
                         fg="black", bg="pink")
contraseña_label.place(x=130, y=145)

texto_contraseña = Entry(frame_registro, font=("times new roman", 15),
                         bg="lightgray", cursor="pencil")  # Configurar show="•" para ocultar la contraseña
texto_contraseña.place(x=130, y=175, width=250, height=25)


alerta_bnt = Button(frame_registro, text="Contraseña olvidada papu?", 
    bd=1, font=("times new roman", 12,"bold"), cursor = "pencil", command=gracias).place(x=28,y=280)
registra_bnt = Button(root, text="Registrarse",width = 20, font = ('times new roman', 12,), 
    fg = "#DAD5D6", bg = "#BD152E", cursor = "pencil", command=insertar_datos).place(x=240,y=400)



root.mainloop()
