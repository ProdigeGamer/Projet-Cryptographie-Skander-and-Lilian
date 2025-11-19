import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import messagebox
import random


root = tk.Tk()
root.withdraw()  

vrais_clee_dacces = '123456789123'

nom_utilisateur = simpledialog.askstring("Nom d'utilisateur", "Entrez votre nom d'utilisateur :")
# cle_dacces = simpledialog.askstring("clé d'accès", "Veuillez rentrer votre clé d'accès", show='*')


# var_clé_dacces = "Clé d'accès : " + str(cle_dacces)
# print(var_clé_dacces)


def cree_messagerie():
    messagebox.showinfo("Info", "Voulez vous crée une messagerie priver ?") 
    clee_dacces= ''
    for i in range(12):
        clee_dacces += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789')
    messagebox.showinfo("Clé d'accès", f"Votre clé d'accès est : {clee_dacces}")

    popup_cle = tk.Toplevel()
    popup_cle.title("Clé d'accès")
    popup_cle.geometry("350x120")
    label = tk.Label(popup_cle, text="Votre clé d'accès :", font=("Arial", 12))
    label.pack(pady=10)
    
    def copier_cle():
        popup_cle.clipboard_clear()
        popup_cle.clipboard_append(clee_dacces)
        messagebox.showinfo("Copié", "Clé copiée dans le presse-papier !")

    bouton_copier = tk.Button(popup_cle, text="Copier la clé", command=copier_cle)
    bouton_copier.pack(pady=5)

    lancer_messagerie()
    popup.destroy()


def rejoindre_messagerie():
    messagebox.showinfo("Info", "Voulez vous rejoindre une messagerie priver ?")
    clee_dacces = simpledialog.askstring("Clé d'accès", "Veuillez entrer la clé d'accès de la messagerie privée :")
    if clee_dacces is None or clee_dacces.strip() == "":
        messagebox.showerror("Erreur", "Clé d'accès invalide. Veuillez réessayer.")
    if len(clee_dacces) != 12:
        messagebox.showerror("Erreur", "Clé d'accès invalide. Veuillez réessayer.")
    elif clee_dacces != vrais_clee_dacces:
        messagebox.showerror("Erreur", "Clé d'accès incorrecte. Veuillez réessayer.")
    else:
        messagebox.showinfo("Succès", "Vous avez rejoint la messagerie privée avec succès.")
        lancer_messagerie()
        popup.destroy()

def lancer_messagerie():
    root.deiconify()  
    root.title("Messagerie Privée")
    root.geometry('400x600')
    zone_messages = tk.Text(root, state="disabled", wrap="word")
    zone_messages.pack(fill="both", expand=True)
    entree = tk.Entry(root)
    entree.pack(fill="x")

def _envoie(event=None):
    message = entree.get().strip()
    if not message:
        return
    zone_messages.config(state="normal")
    zone_messages.insert("end", nom_utilisateur + " : " + message + "\n")
    zone_messages.config(state="disabled")
    zone_messages.see("end")
    entree.delete(0, "end")

    
entree = tk.Entry(root)
entree.pack(fill="x")

zone_messages = tk.Text(root, state="disabled", wrap="word")
zone_messages.pack(fill="both", expand=True)

popup = tk.Tk()
popup.title("Choix de la messagerie")
popup.geometry("300x150")

label = tk.Label(popup, text="Que voulez-vous faire ?", font=("Arial", 12))
label.pack(pady=20)

bouton_créer = tk.Button(popup, text="Créer une messagerie privée", command=cree_messagerie)
bouton_créer.pack(pady=5)

bouton_rejoindre = tk.Button(popup, text="Rejoindre une messagerie privée", command=rejoindre_messagerie)
bouton_rejoindre.pack(pady=5)


if not nom_utilisateur:
    nom_utilisateur = "Utilisateur"




def _envoie(event=None):
    message = entree.get().strip()
    if not message:
        return
    zone_messages.config(state="normal")
    zone_messages.insert("end", nom_utilisateur + " : " + message + "\n")
    zone_messages.config(state="disabled")
    zone_messages.see("end")
    entree.delete(0, "end")

bouton_envoyer = tk.Button(root, text="Envoyer", command=_envoie)
bouton_envoyer.pack()

entree.bind("<Return>", _envoie)

root.mainloop()
