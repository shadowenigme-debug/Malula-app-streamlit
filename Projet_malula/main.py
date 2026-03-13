from tkinter import *

window = Tk()
#Personnaliser la fenetre
window.title("CARDINAL MALULA")
window.geometry("720x480")
window.minsize(450, 360)

window.iconbitmap("Logos1.ico")
window.config(background="#008080")

#Creer la boite (frame)
frame = Frame(window, bg="#008080")

#ajouter un premier texte
label_title = Label(frame, text="Bienvenue dans l'application du complexe scolaire cardinal malula", font=("Arial", 16), bg="#008080", fg="white")
label_title.pack()

#ajouter un premier texte
label_subtitle = Label(frame, text="Hey ! salut a tous c'est shadow", font=("courrier", 15), bg="#008080", fg="white")
label_subtitle.pack()

# Ajouter un bouton
yt_bouton = Button(frame, text="DECOUVRIR LE CARDINAL", font=("courrier", 15), bg="white", fg="#008080", )
yt_bouton.pack(pady=25, fill=X)

#ajouter la boite
frame.pack(expand=YES)

#AFFICHER
window.mainloop()
