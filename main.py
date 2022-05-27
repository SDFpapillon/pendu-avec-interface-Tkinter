import csv
import random as rd
import tkinter as tk

compteur = 7


def liste_mot():
    """
    génère une liste contenant un des mots aléatoirement

    input :
    return : mot_to_find (type : str)

    écrit par :*.******** avec la participation de : L. Jourdan
    vérifier par : L. Jourdan

    """

    data = open(r"liste_mots.csv")  # ouvre un fichier CSV en lectur seul
    data = csv.reader(data)
    data = list(data)  # on doit transformé le fichier CSV en liste pour pouvoir le traité

    mot = []
    mot_to_find = list(rd.choice(data))  # envoye une des listes aléatoires afin de simuler la génération d'un mot

    for lettre in mot_to_find:  # transforme la liste en liste de caractère
        mot += lettre

    mot_to_find = mot

    return mot_to_find


def list_to_string(liste):
    """
    transforme une liste de caractère en un string

    input : liste (type : list) /!\ ne doit contenir que des caractère /!\
    return : mot (type : string)

    écrit par : L. Jourdan avec la participation de : *.********
    vérifier par : *.********
    """
    mot = ""

    for lettre in liste:
        mot += lettre + " "  # on ajoute les espaces pour que les lettres corespondent aux tirets

    return mot


def generer_tiret(n):
    """
    génère un mot de n tiret, base du pendu

    input : n (type : int)
    return : mot (type : string)

    écrit par : L. Jourdan avec la participation de : *.********
    vérifier par : *.******** avec la participation de : L. Jourdan
    """

    mot = []

    for i in range(n):
        mot += ["_" + " "]  # on met des espaces afin de diferancier facilement les differents tirets

    return mot


def frame_du_jeu():
    """
    la boucle du jeu, elle contient

    input : lettre_need_to_win (type : int) /!\ ne contient pas les lettres demander mais leur nombre /!\
    return : not

    écrit par : L. Jourdan avec la participation de : *.********
    vérifier par : *.******** avec la participation de : L. Jourdan
    """
    global compteur
    global lettre_need_to_win
    global mot_to_find
    global mot
    global zone_saisi
    global texte_jeu
    global texte_info

    texte_jeu['text'] = list_to_string(mot)

    lettre = zone_saisi.get().upper()

    if lettre in mot_to_find and not lettre in mot:

        for i in range(mot_to_find.count(lettre)):
            lettre_need_to_win -= 1
            mot[mot_to_find.index(lettre)] = lettre
            mot_to_find[mot_to_find.index(lettre)] = 0

        texte_jeu['text'] = list_to_string(mot)
        texte_info['text'] = "Bien trouver"

    else:

        if lettre in mot:
            texte_info['text'] = "tu as déjà utiliser cette lettre"

        else:
            compteur -= 1
            texte_info['text'] = "domage, la lettre " + lettre + " n'apparait pas dans le mot a trouver"
            dessin_pendue.create_image(200, 200, image=liste_image[7 - compteur])

            if compteur == 0:
                texte_info['text'] = "Vous êtes mort \U0000B2620"

            else:
                text_info = "Nombre de vie: "

                for i in range(compteur):
                    text_info += "\U00002665 "
                for i in range(7 - compteur):
                    text_info += "\U00002661 "
                texte_info['text'] = text_info

    if lettre_need_to_win == 0:
        texte_info['text'] = "bravo"


mot_to_find = liste_mot()

lettre_need_to_win = len(mot_to_find)

mot = generer_tiret(lettre_need_to_win)

ma_fenettre = tk.Tk()
ma_fenettre.title("Jeu du pendu")
ma_fenettre.geometry("640x480")

zone_saisi = tk.Entry(ma_fenettre)

zone_saisi.pack()

texte_info = tk.Label(
    ma_fenettre,
    text="test"
)

texte_info.pack()

texte_jeu = tk.Label(
    ma_fenettre,
    text=list_to_string(mot)
)
texte_jeu.pack()

bouton_entre = tk.Button(
    ma_fenettre,
    text="entré",
    command=frame_du_jeu
)

bouton_entre.pack()

dessin_pendue = tk.Canvas(ma_fenettre, width=300, height=300, bg="Grey")

liste_image = [tk.PhotoImage(file=r"pendu_0.gif", master=ma_fenettre),
               tk.PhotoImage(file=r"pendu_1.gif", master=ma_fenettre),
               tk.PhotoImage(file=r"pendu_2.gif", master=ma_fenettre),
               tk.PhotoImage(file=r"pendu_3.gif", master=ma_fenettre),
               tk.PhotoImage(file=r"pendu_4.gif", master=ma_fenettre),
               tk.PhotoImage(file=r"pendu_5.gif", master=ma_fenettre),
               tk.PhotoImage(file=r"pendu_6.gif", master=ma_fenettre),
               tk.PhotoImage(file=r"pendu_7.gif", master=ma_fenettre)]

dessin_pendue.pack()

dessin_pendue.create_image(200, 200, image=liste_image[0])

ma_fenettre.mainloop()