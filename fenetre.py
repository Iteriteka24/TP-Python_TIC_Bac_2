import tkinter as tk
fenetre= tk.Tk()

def afficher_texte():
    nom_saisie= champ_saisie.get()
    message_saisie= zone_texte.get("1.0",tk.END)
    print(f"Nom : {nom_saisie}")
    print(f"Message : {message_saisie}")
    messagebox.showinfo("Information",f"Nom : {nom_saisie}\nMessage : {message_saisie}")
fenetre.title("Saisie de texte ")
fenetre.geometry("500x400")
label_nom= tk.Label(fenetre, text="Entrez votre nom :")
label_nom.pack(pady=5)
champ_saisie = tk.Entry(fenetre, width=40)
champ_saisie.pack()
label_message = tk.Label(fenetre, text="Entrez votre message :")
label_message.pack(pady=5)
zone_texte = tk.Text(fenetre,width=40,height=5)
zone_texte.pack()
bouton_afficher = tk.Button(fenetre, text="Afficher :")
bouton_afficher.pack(pady=10)

fenetre.mainloop()