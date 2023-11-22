from tkinter import *
import tkinter as tk
from tkinter import ttk


window=Tk()
window.state("zoomed")
window.title("Commune Urbaine")



details=LabelFrame(window,text="*** YASSINE HADDAD",font=("Merriweather",12),bg="#528B8B",fg="white",relief=GROOVE,bd=10)
details.place(x=0,y=0,relwidth=1)
cust_name=Label(details,text="2023",font=(" Merriweather",14),bg="#528B8B",fg="white").grid(row=0,column=1,padx=50)

#==============================================================
billarea=Frame(window,bd=10,relief=GROOVE,bg="#528B8B")
billarea.place(x=900,y=188,width=330,height=472)
        
bill_title=Label(billarea,text="Ticket",font=("Arial Black",17),bd=7,relief=GROOVE,bg="#528B8B",fg="black").pack(fill=X)
scrol_y=Scrollbar(billarea,orient=VERTICAL)
txtarea=Text(billarea,yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=txtarea.yview)
txtarea.pack(fill=BOTH,expand=1)


def calculer():
         tb=float(entryt.get())*float(entryb.get())
         l1["text"]=tb

         tm=(float(entryb.get())*float(entrym.get()))/100
         l2["text"]=tm

         tot=float(tb)+float(tm)
         l3["text"]=(tot,"DH")
         txtarea.delete(1.0,END)
         txtarea.insert(END,"\tCommune Guercif\n\t      2022")
         txtarea.insert(END,f"\nTremestres : {entryt.get()}")
         txtarea.insert(END,f"\nLa base : {entryb.get()}")
         txtarea.insert(END,f"\nLa majoration : {entrym.get()} %")
         txtarea.insert(END,"\n====================================\n")
         txtarea.insert(END,"\nT x B\t\tB x M   \tTotal\n")
         txtarea.insert(END,"\n====================================\n")
         txtarea.insert(END,f"\n{tb}      ")
         txtarea.insert(END,f"\t{tm}       ")
         txtarea.insert(END,f"\t{tot} DH")

def delete():
    entryt.delete(0, END)
    entryb.delete(0, END)
    entrym.delete(0, END)
    #l1.destroy()
    #l2.destroy()
    #l3.destroy() 

def print():
    tb=float(entryt.get())*float(entryb.get())
    l1["text"]=tb
    tm=(float(entryt.get())*float(entrym.get()))/100
    l2["text"]=tm
    tot=float(tb)+float(tm)
    l3["text"]=(tot,"DH")
    
    f=open("Commune.txt","a")
    f.write(str("T x BASE : " ))
    f.write(str(tb) + "\n")
    f.write(str("BASE x MAJORATION "))
    f.write(str(tm) + "\n")
    f.write(str("TOTAL EST : "))
    f.write(str(tot) + "\n")
    f.close()


l1=Label(text="")
l2=Label(text="")
l3=Label(text="")

tb=Label(window,text="Tremestre * la base est :",font=("Merriweather",10),fg="black",relief=FLAT,bd=5)
bm=Label(window,text="La base * La majoration est :",font=("Merriweather",10),fg="black",relief=FLAT,bd=5)
tot=Label(window,text="Total à payer est :",font=("Merriweather",10),fg="black",relief=FLAT,bd=5)

tb.place(x=320,y=250)
bm.place(x=320,y=300)
tot.place(x=320,y=350)

tremestre=Label(window,text="Tremestres",font=("Merriweather",10),fg="black",relief=FLAT,bd=5)
entryt=Entry(window)

base=Label(window,text="La base",font=("Merriweather",10),fg="black",relief=FLAT,bd=5)
entryb=Entry(window)

majoration=Label(window,text="La majoration",font=("Merriweather",10),fg="black",relief=FLAT,bd=5)
entrym=Entry(window)
 
 
buttoncalculer=Button(window,text="Calculer le prix :",font=("Cairo",10),bg="#DEDEDE",fg="black",relief=GROOVE,bd=10,command=calculer)
buttoncalculer.place(x=300,y=400)

buttonasup=Button(window,text="Supprimer",font=("Cairo",10),bg="#DEDEDE",fg="black",relief=GROOVE,bd=10,command=delete)
buttonasup.place(x=500,y=400)

buttonimprimer=Button(window,text="Imprimer",font=("Cairo",10),bg="#DEDEDE",fg="black",relief=GROOVE,bd=10,command=print)
buttonimprimer.place(x=700,y=400)


tremestre.place(x=300,y=100)
entryt.place(x=390,y=105)

base.place(x=300,y=150)
entryb.place(x=390,y=155)

majoration.place(x=300,y=200)
entrym.place(x=390,y=210)

l1.place(x=500,y=253)
l2.place(x=500,y=303)
l3.place(x=500,y=353)

window.mainloop()
