from tkinter import *
from function import *







#créer une fenetre
windows = Tk()

#personaliser la fenetre
windows.title("Software installation by David Bertrand : The best administrator of the universe")
windows.geometry("1024x720")
windows.minsize(480, 360)
### changer l image de la fenetre "chercher dans google png to ico"
windows.iconbitmap("windows.ico")
###chercher un code couleur "https://htmlcolorcodes.com/fr/   ùettre un # devant le code"
windows.config(background="#197de1")


###ajuster un premier texte :  avec font on regle la police, avec bg, on règle la couleur du fond et fg la couleur du texte
label_title = Label(windows, text="Welcom to David Bertrand's wonderful application ", font=('Courrier', 30), bg=("#197de1"), fg=("black"))
#droite, gauche , en bas avec  label_title.pack(side=CENTER)
#avec expand=YES, si l on reduite la fenetre, c'est tjrs au centre
label_title.pack()

###ajuster un premier texte :  avec font on regle la police, avec bg, on règle la couleur du fond et fg la couleur du texte
label_title = Label(windows, text="First: install chocolatey ", font=('Courrier', 30), bg=("#197de1"), fg=("black"))
#droite, gauche , en bas avec  label_title.pack(side=CENTER)
#avec expand=YES, si l on reduite la fenetre, c'est tjrs au centre
label_title.pack()
###ajuster un premier texte :  avec font on regle la police, avec bg, on règle la couleur du fond et fg la couleur du texte
label_title = Label(windows, text="Second: Install software ", font=('Courrier', 30), bg=("#197de1"), fg=("black"))
#droite, gauche , en bas avec  label_title.pack(side=CENTER)
#avec expand=YES, si l on reduite la fenetre, c'est tjrs au centre
label_title.pack()
###ajuster un premier texte :  avec font on regle la police, avec bg, on règle la couleur du fond et fg la couleur du texte
label_title = Label(windows, text="After your Clic, wait until the buton's color text return to orange", font=('Courrier', 20), bg=("#197de1"), fg=("black"))
#droite, gauche , en bas avec  label_title.pack(side=CENTER)
#avec expand=YES, si l on reduite la fenetre, c'est tjrs au centre
label_title.pack()






###on crée une frame pour gere la position de nos textes. on indique ou on l apositione , ici c'est windows
#Pour visualiser cette frame on peu ajouter les parametre :  bd=1, relief=SUNKEN
frame = Frame(windows, bg=("#197de1"), bd=1, relief=SUNKEN)
# ajouter un premier bouton
Install_choco = Button(frame, text="Cliquer pour installer chocolatey", font=("Courrier", 25), bg=("white"), fg=("#ED7F46"), command=install_chocolatey)
##marge en y du bouton =>pady = 25 et remplssage en x => fill=X
Install_choco.pack(pady=25, fill=X)
##ajout de frame
frame.pack(expand=YES)







###on crée une frame pour gere la position de nos textes. on indique ou on l apositione , ici c'est windows
#Pour visualiser cette frame on peu ajouter les parametre :  bd=1, relief=SUNKEN
frame = Frame(windows, bg=("#197de1"), bd=1, relief=SUNKEN)
# ajouter un premier bouton
Install_software = Button(frame, text="Cliquer pour installer les logiciels", font=("Courrier", 25), bg=("white"), fg=("#ED7F46"), command=install_software)
##marge en y du bouton =>pady = 25 et remplssage en x => fill=X
Install_software.pack(pady=25, fill=X)
##ajout de frame
frame.pack(expand=YES)




#afficher la fenetre
windows.mainloop()






