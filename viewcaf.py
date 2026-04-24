""" Module viewcaf.py pour la Classe Vue de l'application CAF"""


import tkinter as tk

class ViewCaf:

    def __init__(self):
        #
        # creer une fenêtre
        #
        win = tk.Tk()
        self.win = win
        #
        # mettre un titre
        #
        win.title("Calcul de votre allocation familiale")
        self.win.geometry("800x600") # Ou une autre taille

        # Elles permettent à la colonne 0 et à la ligne 0 de s'étirer
        self.win.columnconfigure(0, weight=1)
        self.win.rowconfigure(0, weight=1)
        #
        # remplir la vue avec des widgets
        #
        self.make_widgets()
    
    def make_widgets(self):
        #
        # mettre un label "Votre salaire"
        #self.win.columnconfigure(0, weight=1)
        self.win.rowconfigure(0, weight=1)

        #   2. Créer un conteneur (Frame) qui sera au milieu
        center_frame = tk.Frame(self.win)
        center_frame.grid(row=0, column=0)
        label_salaire = tk.Label(center_frame, text="Votre salaire")
        label_salaire.grid(row=1, column=1)
        #
        # Mettre un champ de saisie pour le salaire
        #
        self.entry_salaire = tk.Entry(center_frame)
        self.entry_salaire.grid(row=1, column=2)
        #
        # mettre un label " Votre allocation"
        #
        label_allocation = tk.Label(center_frame, text="Votre allocation")
        label_allocation.grid(row=2, column=1)
        #
        # mettre un champ d'affichage pour l'allocation
        #
        self.label_valeur = tk.Label(center_frame, text="0.00")
        self.label_valeur.grid(row=2, column=2)
        #
        # mettre un bouton Calcul
        #
        self.button_calcul = tk.Button(center_frame, text="Calcul",bg="green",fg="white")
        self.button_calcul.grid(row=6, column=1)
        #
        # mettre un bouton RAZ
        # 
        button_raz = tk.Button(center_frame, text="RAZ",command=self.raz)
        button_raz.grid(row=6, column=2)
        #
        # mettre un bouton Quitter
        #
        button_quitter = tk.Button(center_frame, text="Quitter", bg="red",fg="white", command=self.win.destroy)
        button_quitter.grid(row=6, column=3)
    
    def raz(self):
        print("On remet tout à Zéro")
        self.label_valeur.config(text=" ")
        self.entry_salaire.delete(0, tk.END)
    
    def set_command_calcul(self, fn):
        self.button_calcul.config(command=fn)
    
    def get_salaire(self):
        return float(self.entry_salaire.get())
    
    def set_allocation(self, v):
        self.label_valeur.config(text=v)

    def run(self):
        #
        # Boucle principale d'événements
        #
        self.win.mainloop()

def main():
    vc = ViewCaf()
    vc.run()


if __name__ == "__main__":
    main()