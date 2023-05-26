from tkinter import *
import os
import bancoconexao

def gravarDados():
    if tb_nome.get() !="":
        vnome=tb_nome.get()
        vfone=tb_fone.get()
        vemail=tb_email.get()
        vquery="INSERT INTO tb_contatos(T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) VALUES ('"+vnome+"','"+vfone+"','"+vemail+"') "
        bancoconexao.dml(vquery)
        tb_nome.delete(0,END)
        tb_fone.delete(0,END)
        tb_email.delete(0,END)
        print("Dados Gravados")
    else:
        print("Erro")

app=Tk()
app.title("Add")
app.geometry("400x300")
app.configure(background="#fff")

text=Label(app,text="Lista telefônica",background="#2196F3",foreground="#fff")
text.place(x=150,y=10,width=100,height=30)

Label(app,text="Nome",background="#fff", foreground="#000",anchor=W).place(x=10,y=60,width=100,height=20)
tb_nome=Entry(app)
tb_nome.place(x=10,y=80,width=200,height=20)

Label(app,text="Telefone",background="#fff", foreground="#000",anchor=W).place(x=10,y=130,width=100,height=20)
tb_fone=Entry(app)
tb_fone.place(x=10,y=150,width=100,height=20)

Label(app,text="E-Mail",background="#fff", foreground="#000",anchor=W).place(x=10,y=190,width=100,height=20)
tb_email=Entry(app)
tb_email.place(x=10,y=220,width=300,height=20)

Button(app,text="Gravar", bg="#4CAF50",command=gravarDados).place(x=10,y=250,width=90,height=30)
app.mainloop()

