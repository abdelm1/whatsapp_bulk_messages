import tkinter as tk
import tkinter.font as font
from core import *

app=tk.Tk()
app.title("AutoWZ | Whatsapp Automation")
app.iconbitmap("logo.ico")
app.geometry('845x445')
app.resizable(False, False)

##FUNCTIONS FOR TKINTER BUTTONS #####
def msgbox():
    global msg
    msg=tk.Toplevel(app)
    msg.title("AutoWZ | Write your message!")
    msg.iconbitmap("logo.ico")
    msg.geometry('433x440')
    msg.resizable(False, False)
    labeltxt=tk.Label(master=msg,text='Remarque : Ici, où vous pouvez personnaliser\nvotre message à envoyer, vous pouvez utiliser\n{nom} pour insérer le nom de chaque personne,\naussi {note} pour les notes.')
    labeltxt.config(font =("Courier", 11))
    labeltxt.pack()
    global text_box
    text_box = tk.Text(
    msg,
    height=12,
    width=50
    )
    text_box.pack()
    text_box.config()
    msg.attributes('-topmost',True)
    msg.after_idle(msg.attributes,'-topmost',False)

    
def sendmsgbutton():
    msgbox()
    tk.Button(msg, text= "Okay",width= 40,bg='#2fa572',activebackground='#106a43',command=cmd_msg).pack(pady=20)

def sendimagebutton():
    msgbox()
    tk.Button(msg,text="Upload Your Image here!",width=30,bg="#2fa572",pady=20,command=loadimage).pack(pady=20)
    tk.Button(msg, text= "Okay",width= 24,bg='#2fa572',activebackground='#106a43',command=cmd_img).pack(pady=3)
def filebutton():
    msgbox()
    tk.Button(msg,text="Upload Your File here!",width=30,bg="#2fa572",pady=20).pack(pady=20)
    tk.Button(msg, text= "Okay",width= 40,bg='#2fa572',activebackground='#106a43',command=cmd_file).pack(pady=20)

def cmd_msg():
    logs.insert(1,"Messages envoyés avec succès")
    send_msg(text_box.get(1.0, "end-1c"))
    
def cmd_img():
    logs.insert(1,"Images envoyés avec succès")
    send_img(text_box.get(1.0, "end-1c"))
def cmd_file():
    logs.insert(1,"Fichiers envoyés avec succès")
    send_doc(text_box.get(1.0, "end-1c"),path)

#background setup hada
bg = tk.PhotoImage(file = r"pattern.png")
label1 = tk.Label( app, image = bg)
label1.place(x = 0, y = 0)
app['background']='black'

#menu hada
menubar = tk.Menu(app)
menubar.add_cascade(label="Load",command=loaddata)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command='cc')
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_separator()
helpmenu.add_command(label="Exit", command=app.quit)

menubar.add_cascade(label="About",command=aboutus)

app.config(menu=menubar)

lf=tk.Frame(app)
lf.grid(row=0,column=0,padx=80,pady=120)

font=font.Font(weight="bold",size=18,family='Century Gothic')


btn=tk.Button(lf,text='Send a message',bg='#2fa572',activebackground='#106a43',width=16,command=sendmsgbutton)
btn['font']=font
btn.grid(row=1,column=0)

btn1=tk.Button(lf,text='Send an image',bg='#2fa572',activebackground='#106a43',width=16,command=sendimagebutton)
btn1['font']=font
btn1.grid(row=2,column=0)

btn2=tk.Button(lf,text='Send a File',bg='#2fa572',activebackground='#106a43',width=16,command=filebutton)
btn2['font']=font
btn2.grid(row=3,column=0)

logs=tk.Listbox(app,height=15,width=60,bg='#cecece')
logs.insert(0,"----------------------------Logs System-----------------------------")
logs.grid(row=0,column=1,padx=23,pady=20)

copyrights=tk.Label(text="Made with ♥ by @Abdu & @Smail",bg="black",fg="white",font=('Century Gothic', 12))
copyrights.grid(row=4,column=1,)



app.mainloop()

