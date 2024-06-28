from tkinter import ttk
from tkinter import*
from tkinter import messagebox
import pymysql
import tkinter as tk



class Admin_Tienda:
    


            def __init__(self, root):
                self.wind = root
                self.wind.title("º||M||º Admin")
                self.wind.geometry("940x580")
                self.wind.config(bg="teal")

            

        #Frame zona
                frame1 = LabelFrame(self.wind, text="Datos de los Productos",
                    font = ("times new roman",17,"bold"))
                frame2 = LabelFrame(self.wind, text="Informacion de los Productos",
                    font=("times new roman",17,"bold"))

                frame1.pack(fill="both", expand="no", padx=20, pady=20)
                frame2.pack(fill="both", expand="no", padx=20, pady=20)



                def Guardar():
                    bd = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db="tienda")

                    mcursor = bd.cursor()

                    sql = "INSERT INTO articulos (nombre, marca, tamaño, precio) VALUES ('{0}','{1}','{2}','{3}')".format(self.entry1.get(),
                    self.entry2.get(), self.entry3.get(), self.entry4.get())

                    try:
                        mcursor.execute(sql)
                        bd.commit()
                        messagebox.showinfo(message="Registro Valido", title="Aviso")

                        Mostrar()
                        Limpiar()

                    except:
                        bd.rollback()
                        messagebox.showwarning(message="Registro No Valido", title="Aviso")
                        
                        bd.close()
                        Mostrar()
                        Limpiar()
                        

                def Actualizar():
                    nombre_articulo = self.entry1.get()  # Obtener el valor del campo entry1
                    nuevo_precio = self.entry2.get()  # Obtener el valor del campo entry2

                    bd = pymysql.connect(
                        host="localhost",
                        user="root",
                        password="",
                        db="tienda")

                    mcursor = bd.cursor()

                    mcursor.execute("UPDATE articulos SET precio=%s WHERE nombre=%s", (nuevo_precio, nombre_articulo))
                    bd.commit()
                    if mcursor.rowcount > 0:  # Verificar si se actualizó algún registro
                        messagebox.showinfo(message="Registro Actualizado", title="Aviso")
                    else:
                        messagebox.showinfo(message="No se encontró ningún registro para actualizar", title="Aviso")

                    bd.close()
                    Mostrar()
                    Limpiar()



                def Eliminar():
            
                    nombre_articulo = self.entry1.get()  # Obtener el valor del campo entry1
                    bd = pymysql.connect(
                        host="localhost",
                        user="root",
                        password="",
                        db="tienda")

                    mcursor = bd.cursor()
                    
                    mcursor.execute("DELETE FROM articulos WHERE nombre=%s", (nombre_articulo,))
                    bd.commit()
                    if mcursor.rowcount > 0:  # Verificar si se eliminó algún registro
                            messagebox.showinfo(message="Registro Eliminado", title="Aviso")
                    else:
                            messagebox.showinfo(message="No se encontró ningún registro para eliminar", title="Aviso")

                    bd.close()
                    Mostrar()
                    Limpiar()



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

                def Limpiar():
                    self.entry1.delete(0, END)
                    self.entry2.delete(0, END)
                    self.entry3.delete(0, END)
                    self.entry4.delete(0, END)

                

        #Label zona
                label1 = Label(frame1, text="Nombre", width=10, 
                font = ("Arial",10,"bold"))
                label1.grid(row=0, column=0, padx=5, pady=5)
                self.entry1 = Entry(frame1)
                self.entry1.grid(row=0, column=1, padx=5, pady=3)

                label2 = Label(frame1, text="Marca", width=20, 
                font = ("Arial",10,"bold"))
                label2.grid(row=1, column=0, padx=5, pady=3)
                self.entry2 = Entry(frame1)
                self.entry2.grid(row=1, column=1, padx=5, pady=3)

                label3 = Label(frame1, text="Tamaño", width=20, 
                font = ("Arial",10,"bold"))
                label3.grid(row=2, column=0, padx=5, pady=3)
                self.entry3 = Entry(frame1)
                self.entry3.grid(row=2, column=1, padx=5, pady=3)

                label4 = Label(frame1, text="Precio", width=20, 
                font = ("Arial",10,"bold"))
                label4.grid(row=3, column=0, padx=5, pady=3)
                self.entry4 = Entry(frame1)
                self.entry4.grid(row=3, column=1, padx=5, pady=3)

        #Boton zona
                boton1 = Button(frame1, text = "Nuevo +",width = 12, height=2,font = ('Arial', 12), 
                    fg = "#DAD5D6", bg = "#158645", cursor = "pencil", 
                    activebackground = "#35BD6F", command=Limpiar)
                boton1.grid(row=5, column=0, padx=10, pady=10)

                boton2 = Button(frame1, text = "Guardar ",width = 12, height=2,font = ('Arial', 12), 
                    fg = "#DAD5D6", bg = "blue", cursor = "pencil", 
                    activebackground = "blue", command=Guardar)
                boton2.grid(row=5, column=1, padx=10, pady=10)

                boton3 = Button(frame1, text = "Eliminar",width = 12, height=2,font = ('Arial', 12), 
                    fg = "#DAD5D6", bg = "#BD152E", cursor = "pencil", 
                    activebackground = "#E15370", command=Eliminar)
                boton3.grid(row=5, column=3, padx=10, pady=10)

                boton4 = Button(frame1, text = "Lista",width = 12, height=2,font = ('Arial', 12), 
                    fg = "#DAD5D6", bg = "purple", cursor = "pencil", 
                    activebackground = "purple", command=Mostrar)
                boton4.grid(row=5, column=4, padx=10, pady=10)

                boton5 = Button(frame1, text = "Actualizar",width = 12, height=2,font = ('Arial', 12), 
                    fg = "black", bg = "#FFD700", cursor = "pencil", 
                    activebackground = "#FFECB3", command=Actualizar)
                boton5.grid(row=5, column=5, padx=10, pady=10)

            
                self.trv = ttk.Treeview(frame2, columns=(0,1,2,3,4), show="headings",
                height="15")
                self.trv.pack()

                self.trv.column(0, width=50)
                self.trv.column(1, width=250)
                self.trv.column(2, width=250)
                self.trv.column(3, width=250)
                self.trv.column(4, width=80)

                

                self.trv.heading(0, text = "ID")
                self.trv.heading(1, text = "Nombre")
                self.trv.heading(2, text = "Marca")
                self.trv.heading(3, text = "Tamaño")
                self.trv.heading(4, text = "Precio")
                
        

       

        


if __name__== '__main__':
    root = Tk()
    Admin_Tienda = Admin_Tienda(root)
    root.mainloop()