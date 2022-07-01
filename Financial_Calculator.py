from tkinter import *
import numpy as np
import pandas as pd

#conversão de taxa
def data_con(): 
    window2 = Tk()
    Label(window2,text="Período da taxa atual").grid(row=1)
    Label(window2,text="Período da taxa que você quer").grid(row=2)
    Label(window2,text="Taxa (i)").grid(row=3)
    p_at = Entry(window2)
    p_at.grid(row=1,column=1)

    p_qr = Entry(window2)
    p_qr.grid(row=2,column=1)

    i = Entry(window2)
    i.grid(row=3,column=1)

    def aux():
        p_at2 = float(p_at.get())
        p_qr2 = float(p_qr.get())
        i2 = float(i.get())
        result = (np.power((1+(i2/100)),(p_qr2/p_at2))-1)*100
        Label(window2,bg="yellow", text="Taxa a cada "+str(int(p_qr2))+" dias: "+str(round(result,7))+"%").grid(row=4,column=1)
        return(str(round(result,7)))

    Button(window2,text="Calcular",command =aux).grid(row=4,column=0,sticky=W)
    def aux2():
        x= aux()
        copied=pd.DataFrame([x.replace(',','.')])
        copied.to_clipboard(index=False,header=False)
        Label(window2,bg="green",text="Copiado!").grid(row=5,column=1)
    Button(window2,text="Copy",command =aux2).grid(row=5,column=0,sticky=W)

    window2.mainloop()

    return()
#--------------------------------------------------#
#Capitalização por juros compostos
def cap_jc():
    if len(Pv.get())==0: 
        Fv2= float(Fv.get())
        i2= float(i.get())
        n2= float(n.get())
        x = Fv2/(np.power((1+(i2/100)),n2))   

    if len(Fv.get()) == 0:
        Pv2= float(Pv.get())
        i2= float(i.get())
        n2= float(n.get())
        x = Pv2*np.power((1+(i2/100)),n2)

    if len(i.get()) == 0:
        Pv2= float(Pv.get())
        Fv2= float(Fv.get())
        n2= float(n.get())
        x = (np.power((Fv2/Pv2),(1/n2))-1)*100

    if len(n.get()) == 0:
        Pv2= float(Pv.get())
        Fv2= float(Fv.get())
        i2= float(i.get())
        x = (np.log(Fv2/Pv2)/np.log(1+(i2/100)))

    Label(window,bg="yellow",text=str(round(x,2))).grid(row=5,column=1)
    return()
#--------------------------------------------------#
#Capitalização por juros simples
def cap_js():
    x=0
    if len(Pv.get())==0: 
        Fv2= float(Fv.get())
        i2= float(i.get())
        n2= int(n.get())
        x = Fv2/(1+(i2/100)*n2)

    if len(Fv.get()) == 0:
        Pv2= float(Pv.get())
        i2= float(i.get())
        n2= float(n.get())
        x = Pv2*(1+(i2/100)*n2)

    if len(i.get()) == 0:
        Pv2= float(Pv.get())
        Fv2= float(Fv.get())
        n2= float(n.get())
        x = (((Fv2/Pv2)-1)/n2)*100

    if len(n.get()) == 0:
        Pv2= float(Pv.get())
        Fv2= float(Fv.get())
        i2= float(i.get())
        x = (((Fv2/Pv2)-1)/(i2/100))

    Label(window,bg="yellow",text=str(round(x,2))).grid(row=5,column=1)
    #return(print(x))
    
#Main -------------------------------------------------------------------------------
window = Tk()

Label(window,text="Pv").grid(row=0)
Label(window,text="FV").grid(row=1)
Label(window,text="i").grid(row=2)
Label(window,text="n").grid(row=3)

Pv = Entry(window)
Pv.grid(row=0,column=1)

Fv = Entry(window)
Fv.grid(row=1,column=1)

i = Entry(window)
i.grid(row=2,column=1)

n = Entry(window)
n.grid(row=3,column=1)


Button(window,text="Juros Simples",command = cap_js).grid(row=5,sticky=W)
Button(window,text="Juros Compostos",command = cap_jc).grid(row=6,column=0,sticky=W)
Button(window,text="Conversão de taxa",bd=10,command =data_con).grid(row=8,column=2,sticky=W)

window.mainloop()






