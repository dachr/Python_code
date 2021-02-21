from tkinter import *


def fermerlafenetre():
    windows3.quit()
    windows3.destroy()



windows3 = Tk()
windows3.geometry("1024x720")
windows3.config(background="#197de1")
w = Label(windows3, text ='Delectionner les logiciels que vous ne voulez pas  installer', font = "50",  bg=("white"), fg=("#ED7F46"))
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()
Checkbutton4 = IntVar()
Checkbutton5 = IntVar()
Checkbutton6 = IntVar()
Checkbutton7 = IntVar()
Checkbutton8 = IntVar()
Checkbutton9 = IntVar()
Checkbutton10 = IntVar()
###activation par defaut
Checkbutton1.set(1)
Checkbutton2.set(1)
Checkbutton3.set(1)
Checkbutton4.set(1)
Checkbutton5.set(1)
Checkbutton6.set(1)
Checkbutton7.set(1)
Checkbutton8.set(1)
Checkbutton9.set(1)
Checkbutton10.set(1)

Button1 = Checkbutton(windows3, text = "choco  install  adobereader",
                      variable = Checkbutton1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 50)

Button2 = Checkbutton(windows3, text = "choco install firefox",
                      variable = Checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 50)

Button3 = Checkbutton(windows3, text = "choco install googlechrome",
                      variable = Checkbutton3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 50)

Button4 = Checkbutton(windows3, text = "choco install openvpn-community",
                      variable = Checkbutton4,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 50)

Button5 = Checkbutton(windows3, text = "choco install javaruntime",
                      variable = Checkbutton5,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 50)

Button6 = Checkbutton(windows3, text = "choco install keepass",
                      variable = Checkbutton6,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 50)

Button7 = Checkbutton(windows3, text = "choco install 7zip.install",
                      variable = Checkbutton7,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 50)

Button8 = Checkbutton(windows3, text = "choco install naps2",
                      variable = Checkbutton8,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 50)

Button9 = Checkbutton(windows3, text = "choco install tightvnc",
                      variable = Checkbutton9,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 50)

Button10 = Checkbutton(windows3, text = "choco install libreoffice",
                      variable = Checkbutton10,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 50)


Button1.pack()
Button2.pack()
Button3.pack()
Button4.pack()
Button5.pack()
Button6.pack()
Button7.pack()
Button8.pack()
Button9.pack()
Button10.pack()

##on crée une frame pour gere la position de nos textes. on indique ou on l apositione , ici c'est windows
#Pour visualiser cette frame on peu ajouter les parametre :  bd=1, relief=SUNKEN
frame = Frame(windows3, bg=("#197de1"), bd=1, relief=SUNKEN)
# ajouter un premier bouton
Install_software = Button(frame, text="Cliquer pour Valider", font=("Courrier", 25), bg=("white"), fg=("#ED7F46"), command=fermerlafenetre)
##marge en y du bouton =>pady = 25 et remplssage en x => fill=X
Install_software.pack(pady=25, fill=X)
##ajout de frame
frame.pack(expand=YES)

mainloop()




meslogiciels = []
print(Checkbutton1.get())
print(Checkbutton2.get())
print(Checkbutton3.get())
if Checkbutton1.get() == 1:
    meslogiciels.append("choco install -y adobereader")
if Checkbutton2.get() == 1:
    meslogiciels.append("choco install firefox")
if Checkbutton3.get() == 1:
    meslogiciels.append("choco install googlechrome")
if Checkbutton4.get() == 1:
    meslogiciels.append("choco install openvpn-community")
if Checkbutton5.get() == 1:
    meslogiciels.append("choco install javaruntime")
if Checkbutton6.get() == 1:
    meslogiciels.append("choco install keepass")
if Checkbutton7.get() == 1:
    meslogiciels.append("choco install 7zip.install")
if Checkbutton8.get() == 1:
    meslogiciels.append("choco install naps2")
if Checkbutton9.get() == 1:
    meslogiciels.append("choco install tightvnc")
if Checkbutton10.get() == 1:
    meslogiciels.append("choco install libreoffice")



for value in meslogiciels:
    print(value)
