from tkinter import*
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Tk, Label
from tienda_usuarios import Usuario_Tienda
from admin_ventana import Admin_Tienda



def insertar_datos():
    bd = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tienda"
    )

    mcursor = bd.cursor()

    sql = "SELECT * FROM login WHERE cliente = %s AND contraseña = %s"
    
    mcursor.execute(sql, (texto_usuario.get(), texto_contraseña.get()))
    conexion = mcursor.fetchone()

    if conexion:
        if texto_usuario.get() == "admin" and texto_contraseña.get() == "admin":
            messagebox.showinfo(message="Bienvenido Administrador", title="Aviso")
            Admin_Tienda(root)
        
        else:
            messagebox.showinfo(message="Usuario Encontrado - Iniciando...", title="Aviso")
            Usuario_Tienda(root)
        
    else:
        messagebox.showwarning(message="Usuario No Encontrado - Registro Necesario...", title="Aviso")

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


titulo = Label(frame_registro, text = "Usuario", 
font = ("Arial",25,"bold"),
fg="black", bg="pink").place(x=175,y=10)
sesion = Label(frame_registro, text = "Area de inicio de sesion", 
font = ("Arial",15,"bold"),
fg="black", bg="pink").place(x=130,y=55)


usuario = Label(frame_registro, text = "Nombre de usuario: ", 
font = ("Arial",15,"bold"),
fg="black", bg="pink").place(x=130,y=85)
texto_usuario = Entry(frame_registro, font=("times new roman",15),
bg="lightgray", cursor = "pencil")
texto_usuario.place(x=130,y=115,width=250,height=25)

contraseña = Label(frame_registro, text = "Contraseña: ", 
font = ("Arial",15,"bold"),
fg="black", bg="pink").place(x=130,y=145)
texto_contraseña = Entry(frame_registro, font=("times new roman",15),
bg="lightgray", cursor = "pencil", show="•")
texto_contraseña.place(x=130,y=175,width=250,height=25)

registra_bnt = Button(root, text="Iniciar",width = 20, font = ('times new roman', 12,), 
fg = "#DAD5D6", bg = "#BD152E", cursor = "pencil", command=insertar_datos).place(x=240,y=400)


root.mainloop()