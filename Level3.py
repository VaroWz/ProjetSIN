from tkinter import *
# from tkinter import ttk

Matrice = \
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 7, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
     [1, 3, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
     [1, 1, 1, 0, 2, 6, 2, 0, 1, 1, 1, 1],
     [1, 1, 1, 0, 0, 5, 0, 0, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 5, 0, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
TempMatrice = \
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 7, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
     [1, 3, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
     [1, 1, 1, 0, 2, 6, 2, 0, 1, 1, 1, 1],
     [1, 1, 1, 0, 0, 5, 0, 0, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 5, 0, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
print(Matrice)

fen = Tk()
fen.title("Test")
fen.focus_force()
fen.attributes('-fullscreen', True)
fen.iconbitmap("caisses.gif")
can = Canvas(fen, width=510, height=510, bg='white', bd=8, relief="ridge")
can.grid(row=0, column=0, columnspan=2, padx=3, pady=3)

def Restart():

    for k in range(12):
        for i in range(12):
            Matrice[i][k] = TempMatrice[i][k]
    FullAffiche()

bouton_restart = Button(fen, text="Recommencer", command=Restart)
bouton_restart.grid(row=1, column=2, padx=2, pady=3, sticky=E)


def Precedent():
    fen.destroy()
    import Level2

##bouton_avant = Button(fen, text="Niveau précédent", command=Precedent)
##bouton_avant.grid(row=1, column=0, padx=2, pady=3, sticky=E)


def Suivant():
    fen.destroy()
    import Level4

bouton_suivant = Button(fen, text="Niveau suivant", command=Suivant)
bouton_suivant.grid(row=1, column=0, padx=3, pady=3, sticky=E)

bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row=1, column=1, padx=3, pady=3, sticky=E)

briques = PhotoImage(file="briques.gif")
sol = PhotoImage(file="sol.gif")
caisse = PhotoImage(file="caisses.gif")
caissesombre = PhotoImage(file="caisses_sombre.gif")
prisonnier = PhotoImage(file="prisionier.gif")
gardienbas = PhotoImage(file="gardien_bas.gif")
gardienhaut = PhotoImage(file="gardien_haut.gif")
gardiendroite = PhotoImage(file="gardien_droite.gif")
gardiengauche = PhotoImage(file="gardien_gauche.gif")
point = PhotoImage(file="point.gif")
porte = PhotoImage(file="porte.gif")
porteouverte = PhotoImage(file="porte_ouverte.gif")


def deplacement(event):
    ligne = 0
    colonne = 0

    for k in range(12):
        for i in range(12):
            if (Matrice[i][k] == 3) or (Matrice[i][k] == 8):
                ligne = i
                colonne = k

    ##fleche droite
    if event.keysym == "Right":
        if (Matrice[ligne][colonne+1] == 4):
            fen.destroy()
            import Level4
        if (Matrice[ligne][colonne] == 3):
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=gardiendroite)
        elif (Matrice[ligne][colonne] == 8):
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=gardiendroite)

        ##Dans la verif, faire pour la matrice 8, quand le perso se déplace alors qu'il est sur un point
        if (Matrice[ligne][colonne + 1] == 2) or (Matrice[ligne][colonne + 1] == 6):
            if (Matrice[ligne][colonne + 2] == 1) or (Matrice[ligne][colonne + 2] == 2) \
                    or (Matrice[ligne][colonne + 2] == 6):
                return
        if (Matrice[ligne][colonne + 1] == 1) or (Matrice[ligne][colonne + 1] == 7):
            return
        if (Matrice[ligne][colonne + 1] == 0) or (Matrice[ligne][colonne + 1] == 2) \
                and (Matrice[ligne][colonne + 2] == 0) or (Matrice[ligne][colonne + 2] == 5) \
                or (Matrice[ligne][colonne + 1] == 6) and (Matrice[ligne][colonne + 2] == 0) \
                or (Matrice[ligne][colonne + 1] == 5) or (Matrice[ligne][colonne] == 8) \
                and (Matrice[ligne][colonne + 1] == 6):

            ##à faire, dans les if, verif si c'est 8 ou si c'est 3
            ##Si c'est 8 afficher le pion seul sinon juste un sol
            if (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne + 1] == 6) and (
                    Matrice[ligne][colonne + 2] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 8
                can.create_image(50 + (40 * (colonne + 2)), 50 + (40 * ligne), image=caisse)
                Matrice[ligne][colonne + 2] = 2
                print("test1")

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne + 1] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 8
                print("test2")

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne + 1] == 6) and (
                    Matrice[ligne][colonne + 2] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 8
                can.create_image(50 + (40 * (colonne + 2)), 50 + (40 * ligne), image=caissesombre)
                Matrice[ligne][colonne + 2] = 6
                print("test3")

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne + 1] == 2) and (
                    Matrice[ligne][colonne + 2] == 0):
                print(Matrice)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 3
                can.create_image(50 + (40 * (colonne + 2)), 50 + (40 * ligne), image=caisse)
                Matrice[ligne][colonne + 2] = 2
                print("test4")

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne + 1] == 2) and (
                    Matrice[ligne][colonne + 2] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 3
                can.create_image(50 + (40 * (colonne + 2)), 50 + (40 * ligne), image=caissesombre)
                Matrice[ligne][colonne + 2] = 6
                print("test5")


            # Qaudn c'est une caisse sombre
            elif (Matrice[ligne][colonne + 1] == 6) and (Matrice[ligne][colonne + 2] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 8
                can.create_image(50 + (40 * (colonne + 2)), 50 + (40 * ligne), image=caisse)
                Matrice[ligne][colonne + 2] = 2
                print("test6")

            elif (Matrice[ligne][colonne + 1] == 6) and (Matrice[ligne][colonne + 2] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 8
                can.create_image(50 + (40 * (colonne + 2)), 50 + (40 * ligne), image=caissesombre)
                Matrice[ligne][colonne + 2] = 6
                print("test7")


            # Quand c'est du vide et à coté un point
            elif (Matrice[ligne][colonne + 1] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 8
                print("test8")


            # Qaund c'est une caisse
            elif (Matrice[ligne][colonne + 1] == 2) and (Matrice[ligne][colonne + 2] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 3
                can.create_image(50 + (40 * (colonne + 2)), 50 + (40 * ligne), image=caisse)
                Matrice[ligne][colonne + 2] = 2
                print("test9")

            elif (Matrice[ligne][colonne + 1] == 2) and (Matrice[ligne][colonne + 2] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 3
                can.create_image(50 + (40 * (colonne + 2)), 50 + (40 * ligne), image=caissesombre)
                Matrice[ligne][colonne + 2] = 6
                print("test10")

            ##Quand c'est vide mais qu'il est sur un point
            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne + 1] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 3
                print("test11")


            ##Quand c'est vide
            else:
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne + 1)), 50 + (40 * ligne), image=gardiendroite)
                Matrice[ligne][colonne + 1] = 3
                print("test12")

    if event.keysym == "Left":
        if (Matrice[ligne][colonne-1] == 4):
            fen.destroy()
            import Level4
        if (Matrice[ligne][colonne] == 3):
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=gardiengauche)
        elif (Matrice[ligne][colonne] == 8):
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=gardiengauche)

        # colonne - 1
        if (Matrice[ligne][colonne - 1] == 2) or (Matrice[ligne][colonne - 1] == 6):
            if (Matrice[ligne][colonne - 2] == 1) or (Matrice[ligne][colonne - 2] == 2) \
                    or (Matrice[ligne][colonne - 2] == 6):
                return
        if (Matrice[ligne][colonne - 1] == 1) or (Matrice[ligne][colonne - 1] == 7):
            return
        if (Matrice[ligne][colonne - 1] == 0) or (Matrice[ligne][colonne - 1] == 2) \
                and (Matrice[ligne][colonne - 2] == 0) or (Matrice[ligne][colonne - 2] == 5) \
                or (Matrice[ligne][colonne - 1] == 6) and (Matrice[ligne][colonne - 2] == 0) \
                or (Matrice[ligne][colonne - 1] == 5) or (Matrice[ligne][colonne] == 8) \
                and (Matrice[ligne][colonne - 1] == 6):

            ##à faire, dans les if, verif si c'est 8 ou si c'est 3
            ##Si c'est 8 afficher le pion seul sinon juste un sol
            if (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne - 1] == 6) and (
                    Matrice[ligne][colonne - 2] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 8
                can.create_image(50 + (40 * (colonne - 2)), 50 + (40 * ligne), image=caisse)
                Matrice[ligne][colonne - 2] = 2

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne - 1] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 8

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne - 1] == 6) and (
                    Matrice[ligne][colonne - 2] == 5):
                print("test")
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 8
                can.create_image(50 + (40 * (colonne - 2)), 50 + (40 * ligne), image=caissesombre)
                Matrice[ligne][colonne - 2] = 6

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne - 1] == 2) and (
                    Matrice[ligne][colonne - 2] == 0):
                print(Matrice)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 3
                can.create_image(50 + (40 * (colonne - 2)), 50 + (40 * ligne), image=caisse)
                Matrice[ligne][colonne - 2] = 2

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne - 1] == 2) and (
                    Matrice[ligne][colonne - 2] == 5):
                print("test")
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne - 1)), 50 - (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne - 1)), 50 - (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 3
                can.create_image(50 + (40 * (colonne - 2)), 50 - (40 * ligne), image=caissesombre)
                Matrice[ligne][colonne - 2] = 6


            # Qaudn c'est une caisse sombre
            elif (Matrice[ligne][colonne - 1] == 6) and (Matrice[ligne][colonne - 2] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 8
                can.create_image(50 + (40 * (colonne - 2)), 50 + (40 * ligne), image=caisse)
                Matrice[ligne][colonne - 2] = 2

            elif (Matrice[ligne][colonne - 1] == 6) and (Matrice[ligne][colonne - 2] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 8
                can.create_image(50 + (40 * (colonne - 2)), 50 + (40 * ligne), image=caissesombre)
                Matrice[ligne][colonne - 2] = 6


            # Quand c'est du vide et à coté un point
            elif (Matrice[ligne][colonne - 1] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=point)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 8


            # Qaund c'est une caisse
            elif (Matrice[ligne][colonne - 1] == 2) and (Matrice[ligne][colonne - 2] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 3
                can.create_image(50 + (40 * (colonne - 2)), 50 + (40 * ligne), image=caisse)
                Matrice[ligne][colonne - 2] = 2

            elif (Matrice[ligne][colonne - 1] == 2) and (Matrice[ligne][colonne - 2] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 3
                can.create_image(50 + (40 * (colonne - 2)), 50 + (40 * ligne), image=caissesombre)
                Matrice[ligne][colonne - 2] = 6

            ##Quand c'est vide mais qu'il est sur un point
            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne][colonne - 1] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 3

            ##Quand c'est vide
            else:
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne - 1)), 50 + (40 * ligne), image=gardiengauche)
                Matrice[ligne][colonne - 1] = 3

        print("gauche")
    if event.keysym == "Up":
        if (Matrice[ligne - 1][colonne] == 4):
            fen.destroy()
            import Level4
        if (Matrice[ligne][colonne] == 3):
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=gardienhaut)
        elif (Matrice[ligne][colonne] == 8):
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=gardienhaut)

        ##Ligne - 1
        if (Matrice[ligne - 1][colonne] == 2) or (Matrice[ligne - 1][colonne] == 6):
            if (Matrice[ligne - 2][colonne] == 1) or (Matrice[ligne - 2][colonne] == 2) \
                    or (Matrice[ligne - 2][colonne] == 6):
                return
        if (Matrice[ligne - 1][colonne] == 1) or (Matrice[ligne - 1][colonne] == 7):
            return
        if (Matrice[ligne - 1][colonne] == 0) or (Matrice[ligne - 1][colonne] == 2) \
                and (Matrice[ligne - 2][colonne] == 0) or (Matrice[ligne - 2][colonne] == 5) \
                or (Matrice[ligne - 1][colonne] == 6) and (Matrice[ligne - 2][colonne] == 0) \
                or (Matrice[ligne - 1][colonne] == 5) or (Matrice[ligne][colonne] == 8) \
                and (Matrice[ligne - 1][colonne] == 6):

            ##à faire, dans les if, verif si c'est 8 ou si c'est 3
            ##Si c'est 8 afficher le pion seul sinon juste un sol
            if (Matrice[ligne][colonne] == 8) and (Matrice[ligne - 1][colonne] == 6) and (
                    Matrice[ligne - 2][colonne] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=point)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 8
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 2)), image=caisse)
                Matrice[ligne - 2][colonne] = 2

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne - 1][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * colonne), 50 + (40 * (ligne - 1)), image=point)
                can.create_image(50 + (40 * colonne), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 8

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne - 1][colonne] == 6) and (
                    Matrice[ligne - 2][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=point)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 8
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 2)), image=caissesombre)
                Matrice[ligne - 2][colonne] = 6

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne - 1][colonne] == 2) and (
                    Matrice[ligne - 2][colonne] == 0):
                print(Matrice)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 3
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 2)), image=caisse)
                Matrice[ligne - 2][colonne] = 2

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne - 1][colonne] == 2) and (
                    Matrice[ligne - 2][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 3
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 2)), image=caissesombre)
                Matrice[ligne - 2][colonne] = 6


            # Qaudn c'est une caisse sombre
            elif (Matrice[ligne - 1][colonne] == 6) and (Matrice[ligne - 2][colonne] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=point)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 8
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 2)), image=caisse)
                Matrice[ligne - 2][colonne] = 2

            elif (Matrice[ligne - 1][colonne] == 6) and (Matrice[ligne - 2][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=point)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 8
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 2)), image=caissesombre)
                Matrice[ligne - 2][colonne] = 6


            # Quand c'est du vide et à coté un point
            elif (Matrice[ligne - 1][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=point)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 8


            # Qaund c'est une caisse
            elif (Matrice[ligne - 1][colonne] == 2) and (Matrice[ligne - 2][colonne] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 3
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 2)), image=caisse)
                Matrice[ligne - 2][colonne] = 2

            elif (Matrice[ligne - 1][colonne] == 2) and (Matrice[ligne - 2][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 3
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 2)), image=caissesombre)
                Matrice[ligne - 2][colonne] = 6

            ##Quand c'est vide mais qu'il est sur un point
            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne - 1][colonne] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * colonne), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 3

            ##Quand c'est vide
            else:
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne - 1)), image=gardienhaut)
                Matrice[ligne - 1][colonne] = 3

        print("haut")
    if event.keysym == "Down":
        if(Matrice[ligne+1][colonne] == 4):
            fen.destroy()
            import Level4
        if (Matrice[ligne][colonne] == 3):
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=gardienbas)
        elif (Matrice[ligne][colonne] == 8):
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
            can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=gardienbas)

        ##Ligne +1
        if (Matrice[ligne + 1][colonne] == 2) or (Matrice[ligne + 1][colonne] == 6):
            if (Matrice[ligne + 2][colonne] == 1) or (Matrice[ligne + 2][colonne] == 2) \
                    or (Matrice[ligne + 2][colonne] == 6):
                return
        if (Matrice[ligne + 1][colonne] == 1) or (Matrice[ligne + 1][colonne] == 7):
            return
        if (Matrice[ligne + 1][colonne] == 0) or (Matrice[ligne + 1][colonne] == 2) \
                and (Matrice[ligne + 2][colonne] == 0) or (Matrice[ligne + 2][colonne] == 5) \
                or (Matrice[ligne + 1][colonne] == 6) and (Matrice[ligne + 2][colonne] == 0) \
                or (Matrice[ligne + 1][colonne] == 5) or (Matrice[ligne][colonne] == 8) \
                and (Matrice[ligne + 1][colonne] == 6):

            ##à faire, dans les if, verif si c'est 8 ou si c'est 3
            ##Si c'est 8 afficher le pion seul sinon juste un sol
            if (Matrice[ligne][colonne] == 8) and (Matrice[ligne + 1][colonne] == 6) and (
                    Matrice[ligne + 2][colonne] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=point)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 8
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 2)), image=caisse)
                Matrice[ligne + 2][colonne] = 2

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne + 1][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * colonne), 50 + (40 * (ligne + 1)), image=point)
                can.create_image(50 + (40 * colonne), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 8

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne + 1][colonne] == 6) and (
                    Matrice[ligne + 2][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=point)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 8
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 2)), image=caissesombre)
                Matrice[ligne + 2][colonne] = 6

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne + 1][colonne] == 2) and (
                    Matrice[ligne + 2][colonne] == 0):
                print(Matrice)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 3
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 2)), image=caisse)
                Matrice[ligne + 2][colonne] = 2

            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne + 1][colonne] == 2) and (
                    Matrice[ligne + 2][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 3
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 2)), image=caissesombre)
                Matrice[ligne + 2][colonne] = 6


            # Qaudn c'est une caisse sombre
            elif (Matrice[ligne + 1][colonne] == 6) and (Matrice[ligne + 2][colonne] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=point)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 8
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 2)), image=caisse)
                Matrice[ligne + 2][colonne] = 2

            elif (Matrice[ligne + 1][colonne] == 6) and (Matrice[ligne + 2][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=point)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 8
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 2)), image=caissesombre)
                Matrice[ligne + 2][colonne] = 6


            # Quand c'est du vide et à coté un point
            elif (Matrice[ligne + 1][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=point)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 8

            ##Quand c'est vide mais qu'il est sur un point
            elif (Matrice[ligne][colonne] == 8) and (Matrice[ligne + 1][colonne] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=point)
                Matrice[ligne][colonne] = 5
                can.create_image(50 + (40 * colonne), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 3


            # Qaund c'est une caisse
            elif (Matrice[ligne + 1][colonne] == 2) and (Matrice[ligne + 2][colonne] == 0):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 3
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 2)), image=caisse)
                Matrice[ligne + 2][colonne] = 2

            elif (Matrice[ligne + 1][colonne] == 2) and (Matrice[ligne + 2][colonne] == 5):
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=sol)
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 3
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 2)), image=caissesombre)
                Matrice[ligne + 2][colonne] = 6

            ##Quand c'est vide
            else:
                can.create_image(50 + (40 * colonne), 50 + (40 * ligne), image=sol)
                Matrice[ligne][colonne] = 0
                can.create_image(50 + (40 * (colonne)), 50 + (40 * (ligne + 1)), image=gardienbas)
                Matrice[ligne + 1][colonne] = 3

        print("bas")

    x = 1
    y = 4
    if(Ouverture() == 0):
        if(Matrice[y][x] == 0 or Matrice[y][x] == 3 or Matrice[y+1][x] == 3 or Matrice[y-1][x] == 3
        or Matrice[y][x+1] == 3 or Matrice[y][x-1] == 3):
            return
        else:
            can.create_image(50 + (40 * x), 50 + (40 * y), image=sol)
            Matrice[y][x] = 0

    else:
        can.create_image(50 + (40 * x), 50 + (40 * y), image=porte)
        Matrice[y][x] = 7

def Ouverture():
    for k in range(12):
        for i in range(12):
            if(Matrice[i][k] == 2):
                return 1
    return 0

def FullAffiche():
    for k in range(12):
        for i in range(12):
            so = can.create_image(50 + (40 * k), 50 + (40 * i), image=sol)
            if (Matrice[i][k] == 1):
                bri = can.create_image(50 + (40 * k), 50 + (40 * i), image=briques)
            if (Matrice[i][k] == 2):
                cais = can.create_image(50 + (40 * k), 50 + (40 * i), image=caisse)
            if (Matrice[i][k] == 3):
                gard = can.create_image(50 + (40 * k), 50 + (40 * i), image=gardienbas)
            if (Matrice[i][k] == 4):
                pris = can.create_image(50 + (40 * k), 50 + (40 * i), image=prisonnier)
            if (Matrice[i][k] == 5):
                pointt = can.create_image(50 + (40 * k), 50 + (40 * i), image=point)
            if (Matrice[i][k] == 6):
                caissesombr = can.create_image(50 + (40 * k), 50 + (40 * i), image=caissesombre)
            if (Matrice[i][k] == 7):
                portee = can.create_image(50 + (40 * k), 50 + (40 * i), image=porte)

FullAffiche()
can.bind_all("<Key>", deplacement)
fen.mainloop()
