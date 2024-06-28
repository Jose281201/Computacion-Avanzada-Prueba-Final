from tkinter import ttk
from tkinter import*
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk
import tkinter as tk


class Usuario_Tienda:
    def __init__(self, root):
        self.wind = root
        self.wind.title("º||M||º Tienda")
        self.wind.geometry("900x560")
        self.wind.config(bg="teal")

#Frame zona
        frame1 = LabelFrame(self.wind, text="Datos de los Productos",
            font = ("times new roman",17,"bold"))
        frame2 = LabelFrame(self.wind, text="Informacion de los Productos",
            font=("times new roman",17,"bold"))

        frame1.pack(fill="both", expand="no", padx=20, pady=20)
        frame2.pack(fill="both", expand="yes", padx=20, pady=20)

        def Limpiar():
            self.entry0.delete(0, END)
            self.entry1.delete(0, END)
            self.entry2.delete(0, END)
            self.entry3.delete(0, END)
            self.entry4.delete(0, END)

        def Mostrar():
            bd = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="tienda")
            
            mcursor = bd.cursor()
            mcursor.execute("SELECT * FROM articulos")
            result = mcursor.fetchall()
            if len(result) != 0:
                self.trv.delete(*self.trv.get_children())
                for row in result:
                    self.trv.insert('', END, values = row)
            bd.commit()
            bd.close()
        label_imagen  = None

        def Mostrar_Imagen():
            global label_imagen

            valor = int(self.entry0.get())
            if valor >= valor <= 5:
                imagen_path = f"{valor}.png"
            else:
                pass

            imagen = Image.open(imagen_path)
            imagen = imagen.resize((350,350), imagen.LANZCOS)
            imagen_tk = ImageTk.PhotoImage(imagen)

            if label_imagen and label_imagen.winfo_exists():
                label_imagen.config(image = imagen_tk)
                label_imagen.image = imagen_tk

            else:
                label_imagen = tk.Label(frame1, imagen = imagen_tk)
                label_imagen.image = imagen_tk
                label_imagen.place(x=560, y=130)

        def Buscar():
            bd = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    db="tienda")

            mcursor = bd.cursor()
            id = self.entry0.get()
            sql = f"SELECT * FROM articulos WHERE id = '{id}'"
            mcursor.execute(sql)
            result = mcursor.fetchall()
            for i in result:
                nombre = i[1]
                marca = i[2]
                tamaño = i[3]
                precio = i[4]

            

                
                

            entry_width = 25
            self.entry0.config(width=entry_width)
            self.entry1.config(width=entry_width)
            self.entry2.config(width=entry_width)
            self.entry3.config(width=entry_width)
            self.entry4.config(width=entry_width)

            self.entry1.insert(0, nombre[:entry_width])
            self.entry2.insert(0, marca[:entry_width])
            self.entry3.insert(0, tamaño[:entry_width])
            self.entry4.insert(0, precio[:entry_width])

            
            Mostrar_Imagen()
            bd.commit()
            bd.close()

        def gracias():
            messagebox.showinfo("Mensaje de agradecimiento", "º||M||º Gracias por comprar en nuestra tienda º||M||º")
        
        




        label0 = Label(frame1, text="ID", width=10, 
        font = ("Arial",10,"bold"))
        label0.grid(row=0, column=0, padx=5, pady=5)
        self.entry0 = Entry(frame1)
        self.entry0.grid(row=0, column=1, padx=5, pady=3)

        label1 = Label(frame1, text="Nombre", width=10, 
        font = ("Arial",10,"bold"))
        label1.grid(row=1, column=0, padx=5, pady=5)
        self.entry1 = Entry(frame1)
        self.entry1.grid(row=1, column=1, padx=5, pady=3)

        label2 = Label(frame1, text="Marca", width=20, 
        font = ("Arial",10,"bold"))
        label2.grid(row=2, column=0, padx=5, pady=3)
        self.entry2 = Entry(frame1)
        self.entry2.grid(row=2, column=1, padx=5, pady=3)

        label3 = Label(frame1, text="Tamaño", width=20, 
        font = ("Arial",10,"bold"))
        label3.grid(row=3, column=0, padx=5, pady=3)
        self.entry3 = Entry(frame1)
        self.entry3.grid(row=3, column=1, padx=5, pady=3)

        label4 = Label(frame1, text="Precio", width=20, 
        font = ("Arial",10,"bold"))
        label4.grid(row=4, column=0, padx=5, pady=3)
        self.entry4 = Entry(frame1)
        self.entry4.grid(row=4, column=1, padx=5, pady=3)

        


        #Boton zona
        boton1 = Button(frame1, text = "Buscar +",width = 12, height=2,font = ('Arial', 12), 
            fg = "#DAD5D6", bg = "#158645", cursor = "pencil", 
            activebackground = "#35BD6F", command= Buscar)
        boton1.grid(row=5, column=0, padx=10, pady=10)

        boton2 = Button(frame1, text = "Limpiar x",width = 12, height=2,font = ('Arial', 12), 
            fg = "#DAD5D6", bg = "#BD152E", cursor = "pencil", 
            activebackground = "#E15370", command= Limpiar)
        boton2.grid(row=5, column=1, padx=10, pady=10)

        boton3 = Button(frame1, text = "Lista",width = 12, height=2,font = ('Arial', 12), 
            fg = "#DAD5D6", bg = "purple", cursor = "pencil", 
            activebackground = "purple", command=Mostrar)
        boton3.grid(row=5, column=4, padx=10, pady=10)

        boton4 = Button(frame1, text = "Comprar",width = 12, height=2,font = ('Arial', 12), 
            fg = "#DAD5D6", bg = "blue", cursor = "pencil", 
            activebackground = "blue", command=gracias)
        boton4.grid(row=5, column=8, padx=140, pady=10)



        self.trv = ttk.Treeview(frame2, columns=(0,1,2,3,4), show="headings",
        height="15")
        self.trv.pack()

        self.trv.column(0, width=50)
        self.trv.column(1, width=230)
        self.trv.column(2, width=230)
        self.trv.column(3, width=230)
        self.trv.column(4, width=90)

        

        self.trv.heading(0, text = "ID")
        self.trv.heading(1, text = "Nombre")
        self.trv.heading(2, text = "Marca")
        self.trv.heading(3, text = "Tamaño")
        self.trv.heading(4, text = "Precio")



if __name__== '__main__':
    root = Tk()
    Usuario_Tienda = Usuario_Tienda(root)
    root.mainloop()